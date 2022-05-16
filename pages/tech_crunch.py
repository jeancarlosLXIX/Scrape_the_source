import requests
from bs4 import BeautifulSoup
from pages.parent import BasicActions


# CLASS TECHCRUNCH.COM
class TechCrunch(BasicActions):
    def __init__(self, url:str = 'https://techcrunch.com/') -> None:
        super().__init__(url)

    def print_lastest(self):
           
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

    def menu(self):
        self.print_lastest()