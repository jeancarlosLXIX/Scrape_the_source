import pyinputplus as pyip
import requests
from bs4 import BeautifulSoup
from pages.BasicActions import BasicActions


# FREECODECAMP.COM
class FCC(BasicActions):
    
    def __init__(self, url:str = 'https://www.freecodecamp.org/news') -> None:
        super().__init__(url)

    def home_page(self):
        # response = requests.get(self.BASE_URL)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # objs = {}
        # objs.update(self.create_obj_FCC(soup,"h2.post-card-title > a",False))
        # self.print_news(objs, self.BASE_URL)

        posts = self.obj_filler(self.BASE_URL,['h2.post-card-title > a'])
        self.print_news(posts, self.BASE_URL[:28]) # [:28] to remove the "/news" from base_url

    def base_on_tag(self)->None:
        '''
        Prints a dictionary object based on the tag the user choose
        '''
        tag = self.display_menu(['programming','tech','javascript','web-development',
            'technology','react','startup','software-development',
            'design','python','life-lessons','productivity',
            'self-improvement','youtube', 'css'],"FreeCodeCamp:")

        soup = self.get_response(self.BASE_URL + f'/tag/{tag}',soup_or_obj= False)
        posts = self.create_obj_FCC(soup, '.post-card-title > a', slic=False)
        
        self.print_news(posts,self.BASE_URL)

    def show_trending(self)-> None:
        '''
        Show the elements in the trending footer
        '''
        patterns = [
            '.trending-guides-row > .footer-col-1 > a',
            '.trending-guides-row > .footer-col-2 > a',
            '.trending-guides-row > .footer-col-3 > .footer-left > a',
            '.trending-guides-row > .footer-col-3 > .footer-right > a'
        ]
        
        self.print_news(self.obj_filler(self.BASE_URL, patterns))
    

    def obj_filler(self,url:str, patters:None) -> dict:
        '''This function will return an dict with the link and title
            :param url: The link tha will be used
            :param patters: a list with the css selector(s)
        '''
        if patters == None:
            print("second argument must be list.")
            return
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        obj = {} # this will save the keys and values for printing

        for patter in patters:
            obj.update(self.create_obj_FCC(soup, css_pattern=patter))
        
        return obj

    
    def create_obj_FCC(self, soup: BeautifulSoup = None, css_pattern: str = '', slic:bool = True):
        obj_to_return = {}
        if slic:
            for a in soup.select(css_pattern): # return a list of a elements
                obj_to_return[a.get_text().strip()] = a.get('href')
        else:
            for a in soup.select(css_pattern):
                obj_to_return[a.get_text().strip()] = a.get('href')[5:]  # this slice is to avoid conflics with the route /news in base url
        
        return obj_to_return

    
    def menu(self):
        '''
        This fuction display the Menu of the current web site
        '''

        self.clean_terminal()
        
        menu = ['Home page news (First 25)', 'Base on tag (First 25)', 'What\'s trending', 'Exit']
        option = self.display_menu(menu, "FREE CODE CAMP CONTENT: ")

        self.clean_terminal()
        if option == menu[len(menu)-1]:
            return True
        if option == menu[0]:
            self.home_page()
        elif option == menu[1]:
            self.base_on_tag()
        elif option == menu[2]:
            self.show_trending()
