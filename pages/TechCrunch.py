import json
import requests
from bs4 import BeautifulSoup
from pages.BasicActions import BasicActions



# CLASS TECHCRUNCH.COM
class TechCrunch(BasicActions):
    def __init__(self, url:str = 'https://techcrunch.com/') -> None:
        super().__init__(url)

    def print_lastest(self):
        '''
        This will printe the lastest news on the home page of Tech Crunch
        '''
        self.clean_terminal()
        n = 1
        self.print_response_json(f"https://techcrunch.com/wp-json/tc/v1/magazine?page={n}")


    def tech_plus(self):
        '''
        Tech Crunch plus content
        '''
        code_tag = { 
        "EVENTS": 576796352,
        "FUNDRAISING": 576796353,
        "GROWTH": 576796354,
        "INVESTOR-SURVEYS": 576796355,
        "MARKET-ANALYSIS": 576796356,
        "WORK": 576796357
        }
        option = self.display_menu(list(code_tag.keys()),"TechCrunch +:")
        
        self.print_category(code_tag[option])


    def get_response_tech(self, url: str, element:str, attribute = None) -> dict:
        '''
        Getting the object from Tech Crunch
        :param url: link to fecth
        :param element: this is your HTML element to look for
        :param attribute: accepts a list with to elements, first attribute and second is the value.
        '''
        response = requests.get(url)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        results = soup_obj.find_all(element, attrs={attribute[0]: attribute[1]})
        obj = {}

        for h2 in  results:
            # Now here we get the Key and value from h2 element who has an 'a' elements
            obj.update({h2.find('a').text.strip():h2.find('a').get('href')})
        
        return obj
    
    def print_category(self, category_number: int):
        url = f"https://techcrunch.com/wp-json/tc/v1/magazine?page=1&tc_ec_category={category_number}"
        response = requests.get(url).text
        posts = json.loads(response)

        for idx, post in enumerate(posts, start=1):
            print(f"{idx}){post['title']['rendered']}\nLINK:{post['link']}\n")

    def print_response_json(self,url):
        response = requests.get(url).text
        posts = json.loads(response)

        for idx, post in enumerate(posts, start=1):
            print(f"{idx}){post['title']['rendered']}\nLINK:{post['link']}\n")



    def menu(self):
        choices = ['LASTEST NEWS','TECH CRUNCH +']
        choice = self.display_menu(choices,"Tech Crunch: ")
        
        self.clean_terminal()
        if choice == choices[-1]:
            return True
        
        if choice == choices[0]:
            self.print_lastest()
        
        if choice == choices[1]:
            self.tech_plus()
        
        input("Press enter to continue...")
        self.clean_terminal()