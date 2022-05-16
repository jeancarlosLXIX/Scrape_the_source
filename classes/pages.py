import os
from bs4 import BeautifulSoup
import requests
import pyinputplus as pyip

# Since some things will be a repetition I think it's a good idea to create a clase
# with some common operations
class BasicActions:

    def __init__(self, link: str) -> None:
        self.BASE_URL = link


    def print_news(self,objs:dict, url:str = ''):
        post_n = 0
        for k,v in objs.items():
            post_n += 1
            print(f"{post_n}) {k.upper()}")
            print(f"LINK: {url + v}\n")
    
    def clean_terminal(self):
        '''
        This method will clean the terminal base on the OS
        '''
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def create_obj(self, soup: BeautifulSoup = None, css_pattern: str = '', clean:bool = True):
        '''
        This function will create the object used to print the news
        :param css_pattern: the parameter used in the select method of the soup
        :param clean: this specify parameter is to separe the loop and slice the firsts elements to avoid conflicts with the /news
        in the FCC link
        '''
        obj_to_return = {}
        if clean:
            for a in soup.select(css_pattern): # return a list of a elements
                obj_to_return[a.get_text().strip()] = a.get('href')[5:]  # this slice is to avoid conflics with the route /news in base url
        else:
            for a in soup.select(css_pattern): 
                obj_to_return[a.get_text().strip()] = a.get('href')
                
        return obj_to_return

    def get_response(self,url:str, patter: str)-> dict:
        '''
        Returns a Beautiful obj base on the link
        '''
        response = requests.get(url)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        return self.create_obj(soup=soup_obj, css_pattern=patter)

# FREECODECAMP.COM
class FCC(BasicActions):
    
    def __init__(self, url:str = 'https://www.freecodecamp.org/news') -> None:
        super().__init__(url)

    def base_on_tag(self)->None:
        '''
        Prints a dictionary object based on the tag the user choose
        '''
        tag = pyip.inputMenu(
            ['programming','tech','javascript','web-development',
            'technology','react','startup','software-development',
            'design','python','life-lessons','productivity',
            'self-improvement','youtube', 'css'],
            numbered=True)

        obj_response = self.get_response(self.BASE_URL + f'/tag/{tag}','.post-card-title > a')
        self.print_news(obj_response,self.BASE_URL)

    def show_trending(self)-> None:
        '''
        Show the elements in the trending footer
        '''
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        obj = {} # this will save the keys and values for printing
        
        obj.update(self.create_obj(soup, css_pattern='.trending-guides-row > .footer-col-1 > a',clean=False))
        obj.update(self.create_obj(soup, css_pattern='.trending-guides-row > .footer-col-2 > a',clean=False))
        obj.update(self.create_obj(soup, css_pattern='.trending-guides-row > .footer-col-3 > .footer-left > a',clean=False))
        obj.update(self.create_obj(soup, css_pattern='.trending-guides-row > .footer-col-3 > .footer-right > a',clean=False))
        self.print_news(obj)


    def menu(self,base_link:str):
        '''
        This fuction display the Menu of the current web site
        '''

        self.clean_terminal()
        print("FREE CODE CAMP CONTENT: ")
        menu = ['Home page news (First 25)', 'Base on tag (First 25)', 'What\'s trending', 'Exit']
        option = pyip.inputMenu(choices=menu, numbered=True)
        self.clean_terminal()
        if option == menu[len(menu)-1]:
            return True
        if option == menu[0]:
            self.print_news(self.get_response(base_link,'.post-card-title > a'), base_link)
        elif option == menu[1]:
            self.clean_terminal()
            self.base_on_tag()
        elif option == menu[2]:
            self.show_trending()


# CLASS TECHCRUNCH.COM
class TechCrunch(BasicActions):
    def __init__(self, url:str = 'https://techcrunch.com/') -> None:
        super().__init__(url)

    def print_lastest(self):
        # response = requests.get(self.BASE_URL)
        # soup_obj = BeautifulSoup(response.text, 'html.parser')
        # h2s = soup_obj.find_all('h2', attrs={'class': 'post-block__title'}) # List with all h2 with that class
        # obj = {}
        
        # for h2 in  h2s:
        #     # Now here we get the Key and value from h2 element who has an 'a' elements
        #    obj.update({h2.find('a').text.strip():h2.find('a').get('href')})
           
        self.print_news(self.get_response_tech(self.BASE_URL,'h2', ['class', 'post-block__title']))
    
        

    def tech_videos(self):
        pass

    def get_response_tech(self, url: str, element:str, attribute = None) -> dict:
        '''
        Getting the object from techCrunch
        '''
        response = requests.get(url)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        results = soup_obj.find_all(element, attrs={attribute[0]: attribute[1]}) # List with all h2 with that class
        obj = {}

        for h2 in  results:
            # Now here we get the Key and value from h2 element who has an 'a' elements
           obj.update({h2.find('a').text.strip():h2.find('a').get('href')})
        
        return obj