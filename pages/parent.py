import os
from bs4 import BeautifulSoup
import requests

# Since some things will be a repetition I think it's a good idea to create a clase
# with some common operations
class BasicActions:

    def __init__(self, link: str) -> None:
        self.BASE_URL = link


    def print_news(self,objs:dict, url:str = ''):
        '''
        This class will print the news of the current page
        :param objs: it takes a dictionary where the key is the title of the post and the value its link
        :param url: optional paramiter in case the link of the page isn't complete, we use the base link 
        and add it to the url if provided.
        '''
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
        :param clean: this specific parameter is to separe the loop and slice the firsts elements to avoid conflicts with the /news
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

    def get_response(self,url:str, patter: str, soup_or_obj: bool = True)-> dict:
        '''
        Returns a Beautiful obj base on the link
        :param soup_or_obj: if for some reason you get problems getting the object just return the soup

        '''
        response = requests.get(url)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        if soup_or_obj:
            return self.create_obj(soup=soup_obj, css_pattern=patter)
        else:
            return soup_obj