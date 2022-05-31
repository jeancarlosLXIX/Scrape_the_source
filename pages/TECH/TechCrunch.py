import json
import requests
from bs4 import BeautifulSoup
from pages.BasicActions import BasicActions



# CLASS TECHCRUNCH.COM
class TechCrunch(BasicActions):
    def __init__(self, url:str = 'https://techcrunch.com/') -> None:
        super().__init__(url)

    def print_lastest(self,url):
        '''
        This will printe the lastest news on the home page of Tech Crunch
        '''
        self.clean_terminal()
        n = 1
        self.print_response_json(url)


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

        self.next_page(
            func=self.print_category,
            arg= f"https://techcrunch.com/wp-json/tc/v1/magazine?tc_ec_category={code_tag[option]}&page=1",
            reg="page=\d*",
            replace_with="page="
        )

    
    def print_category(self, url:str):
        '''
        this function is special for the tech_plus it's easear to read and makes it better for calling the next_page
        function.
        
        '''
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
            self.next_page(
            func=self.print_lastest,
            arg="https://techcrunch.com/wp-json/tc/v1/magazine?page=1",
            reg="page=\d*",
            replace_with="page=")
        
        if choice == choices[1]:
            self.tech_plus()
            