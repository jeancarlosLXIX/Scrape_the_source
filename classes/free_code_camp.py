from bs4 import BeautifulSoup
import requests
import pyinputplus as pyip
import os



BASE_URL = 'https://www.freecodecamp.org/news'

def print_news(objs:dict, url:str = ''):
    post_n = 0
    for k,v in objs.items():
        post_n += 1
        print(f"{post_n}) {k.upper()}")
        print(f"LINK: {url + v}\n")

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_obj(soup: BeautifulSoup = None, css_pattern: str = '', clean:bool = True):
    '''
    This function will create the object used to print the news
    :param css_pattern: the parameter used in the select method of the soup
    :param clean: this specify parameter is to separe the loop and slice the firsts elements to avoid conflicts with the /news
    '''
    obj_to_return = {}
    if clean:
        for a in soup.select(css_pattern): # return a list of a elements
            obj_to_return[a.get_text().strip()] = a.get('href')[5:]  # this slice is to avoid conflics with the route /news in base url
    else:
         for a in soup.select(css_pattern): 
            obj_to_return[a.get_text().strip()] = a.get('href')
            
    return obj_to_return


def get_response(url: str)-> dict:
    response = requests.get(url)
    soup_obj = BeautifulSoup(response.text, 'html.parser')
    return create_obj(soup=soup_obj, css_pattern='.post-card-title > a')
    # for a in soup_obj.select('.post-card-title > a'): # return a list of a elements
    #     obj_to_return[a.get_text().strip()] = a.get('href')[5:]  # this slice is to avoid conflics with the route /news in base url
    # return obj_to_return
    

def base_on_tag(url:str)->None:
    '''
    Prints a dictionary object base on the tag the user choose
    '''
    tag = pyip.inputMenu(
        ['programming','tech','javascript','web-development',
        'technology','react','startup','software-development',
        'design','python','life-lessons','productivity',
        'self-improvement','youtube', 'css'],
        numbered=True)
    obj_response = get_response(url + f'/tag/{tag}')
    print_news(obj_response,url)

def show_trending(url: str)-> None:
    '''
    Show the elements in the trending footer
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    obj = {}
    


    print('COL-HEADER')
    obj.update(create_obj(soup, css_pattern='.trending-guides-row > .footer-col-1 > a',clean=False))
    obj.update(create_obj(soup, css_pattern='.trending-guides-row > .footer-col-2 > a',clean=False))
    obj.update(create_obj(soup, css_pattern='.trending-guides-row > .footer-col-3 > .footer-left > a',clean=False))
    obj.update(create_obj(soup, css_pattern='.trending-guides-row > .footer-col-3 > .footer-right > a',clean=False))
    print_news(obj)
    


#print_news(get_response(BASE_URL),BASE_URL)

def main(base_link:str):
    menu = ['Home page news (First 25)', 'Base on tag (First 25)', 'What\'s trending', 'Exit']
    option = pyip.inputMenu(choices=menu, numbered=True)
    clean_terminal()
    if option == menu[len(menu)-1]:
        return True
    if option == menu[0]:
        print_news(get_response(base_link), base_link)
    elif option == menu[1]:
        base_on_tag(base_link)
    elif option == menu[2]:
        show_trending(base_link)

    


if __name__ == "__main__":

    while True:
        exit_loop = main(BASE_URL)
        if exit_loop:
            break
        input("Press enter to continue.")

        #TODO: show trending apply function create_obj