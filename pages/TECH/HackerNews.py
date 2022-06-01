from pages.BasicActions import BasicActions
import pyinputplus as pyip
import requests
from bs4 import BeautifulSoup
import re # to replace the numbers

class HackerNews(BasicActions):

    def __init__(self, link: str = 'https://news.ycombinator.com/news') -> None:
        super().__init__(link)

    def home_page(self,url):
        self.clean_terminal()

        self.print_news_ycombinator(url)
    

    def job_hunting(self):
        print("JUST FIRST PAGE:\n")
        self.print_news_ycombinator("https://news.ycombinator.com/jobs")


    def print_news_ycombinator(self, url):
        response = requests.get(url)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        posts = {}

        for a in soup_obj.select("a.titlelink"):
            posts[a.get_text().strip()] = self.has_https_in_linK(a.get("href"))

        number = 1
        for key,value in posts.items():            
            self.separator(number,'News')
            print(f"{number}) {key}\nLINK:{value}\n")
            number += 1
    

    def has_https_in_linK(self,url:str) -> str:
        '''
        Some of the links of Hacker news are from the page itself, so they just have the route and ID
        we need to add the url
        '''
        if "https" not in url or "http" not in url: # Some links are not secure so this prevents a conflict
             return "https://news.ycombinator.com/" + url
        else:
             return url
    

    def menu(self):
        page = 1
        lookin_for = pyip.inputMenu(["News", "Jobs"], numbered=True)
        if lookin_for == "News":
            self.next_page(self.home_page,"https://news.ycombinator.com/news?p=1", "[0-9]")
        else:
            self.job_hunting()
