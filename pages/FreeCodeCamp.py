import pyinputplus as pyip
import requests
from bs4 import BeautifulSoup
from pages.BasicActions import BasicActions


# FREECODECAMP.COM
class FCC(BasicActions):
    
    def __init__(self, url:str = 'https://www.freecodecamp.org/news') -> None:
        super().__init__(url)

    def base_on_tag(self)->None:
        '''
        Prints a dictionary object based on the tag the user choose
        '''
        tag = self.display_menu(['programming','tech','javascript','web-development',
            'technology','react','startup','software-development',
            'design','python','life-lessons','productivity',
            'self-improvement','youtube', 'css'],"FreeCodeCamp: \n")

        obj_response = self.get_response(self.BASE_URL + f'/tag/{tag}','.post-card-title > a')
        # self.colored_table(obj_response)
        # return
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
            self.print_news(self.get_response(self.BASE_URL,'.post-card-title > a'), self.BASE_URL)
        elif option == menu[1]:
            self.base_on_tag()
        elif option == menu[2]:
            self.show_trending()
