import os
from bs4 import BeautifulSoup
import requests
import pyinputplus as pyip
import re
from rich.console import Console
from rich.table import Table

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
        self.clean_terminal()
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
        :param soup_or_obj: if for some reason you get problems getting the object just change the value
         to False return the soup

        '''
        response = requests.get(url)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        if soup_or_obj:
            return self.create_obj(soup=soup_obj, css_pattern=patter, clean= soup_or_obj)
        else:
            return soup_obj
    

    def display_menu(self, options: None, message:str ="_default" )-> str:
        '''
        Displays a menu with the necesary options
        :param options: A list with all the available choises
        :param message: optional, message that the user will see
        '''
        if options == None:
            return "Not options has been passed"

        if "Exit" not in options: options += ["Exit"] # To ensure an exit options

        option = pyip.inputMenu(options, numbered=True, prompt= message + "\n")

        return option
    

    def  separator(self, post_number:int, tipe:str):
        print(f"{20*'*'} {tipe} #{post_number} {20*'*'}\n")


    def next_page(self, func, arg:str, reg:str = "", replace_with:str = ""):
        '''
        Since some pages has in their link a "page=" argument this function will help you
        check them

        :param func: The function tha will be called in the loop
        :param arg: This is the argument that the function takes
        "param reg: a regex code to search the string (arg)
        :param replace_with: a string that will be used to replace the match string, by defaul is empty
        '''
        page = 1
        while True:
            self.clean_terminal()
            func(arg)

            break_loop = self.display_menu(["Next", "Previous"],"Action:")

            if break_loop == "Exit":
                break

            if break_loop == "Next":
                page += 1
            else:
                if page == 1: continue 
                page -= 1
                
            arg = re.sub(reg,replace_with,arg)  + str(page) # the match will be delete so we convert the number to string an add it

    def colored_table(self, objs:dict):

        table = Table(title="Free Code Camp")
        objs_keys = list(objs.keys())

        print(objs_keys)

        table.add_column("#", justify="right", style="cyan")
        table.add_column("TITLE", justify="right", style="green")
        table.add_column("LINK", justify="right", style="green")
        
        for x,value in enumerate(objs_keys):
            table.add_row(str(x+1), objs_keys[x], objs[objs_keys[x]])

        self.clean_terminal()
        console = Console()
        console.print(table)