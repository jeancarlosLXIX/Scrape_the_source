from bs4 import BeautifulSoup
import requests
import pyinputplus as pyip


BASE_URL = 'https://www.freecodecamp.org/news'

def print_news(objs:dict, url:str = ''):
    post_n = 0
    for k,v in objs.items():
        post_n += 1
        print(f"{post_n}) {k.upper()}")
        print(f"LINK: {url + v}\n")

def create_obj(soup: BeautifulSoup = None, css_pattern: str = '', clean:bool = True):
    obj_to_return = {}
    if clean:
        for a in soup.select(css_pattern): # return a list of a elements
            obj_to_return[a.get_text().strip()] = a.get('href')[5:]  # this slice is to avoid conflics with the route /news in base url
        return obj_to_return
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
    trendings = {}
    col_number = 1 # the trending class is divided in 3 parts but the last one is different
    while col_number <= 2:
        for trending in soup.select(f'.trending-guides-row > .footer-col-{col_number} > a'):
            trendings[trending.get_text().strip()] = trending.get('href')
        col_number += 1
    

    print('ALL TRENDING')
    print_news(trendings)


#print_news(get_response(BASE_URL),BASE_URL)

def main(base_link:str):
    menu = ['Home page news (First 25)', 'Base on tag (First 25)', 'What\'s trending', 'Exit']
    option = pyip.inputMenu(choices=menu, numbered=True)

    if option == menu[len(menu)-1]:
        return True
    if option == menu[0]:
        print_news(get_response(base_link), base_link)
    elif option == menu[1]:
        base_on_tag(base_link)
    elif option == menu[2]:
        print("ENTRA")
        show_trending(base_link)

    


if __name__ == "__main__":

    while True:
        exit_loop = main(BASE_URL)
        if exit_loop:
            break
        input("Press enter to continue.")

        #TODO: show trending apply function create_obj