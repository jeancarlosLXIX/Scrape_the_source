from urllib import response
import requests
from bs4 import BeautifulSoup
from pages.parent import BasicActions

class SlashDot(BasicActions):
    def __init__(self, url:str = 'https://dzone.com/') -> None:
        super().__init__(url)
    
    def lastest_articles(self):
        pass # /list