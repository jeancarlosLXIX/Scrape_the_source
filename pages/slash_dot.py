import json
import requests
import pyinputplus as pyip
from pages.parent import BasicActions


class Dzone(BasicActions):
    def __init__(self, url:str = "https://dzone.com") -> None:
        super().__init__(url)
    
    def lastest(self):
        '''
        This function will print the lastests news from Dzone
        '''
        self.category_or_lastest()
    
    def read_by_category(self):
        '''
        This will give you the user choose by his/her prefer topic
        '''
        categories = {
                "Java":1,
                "Agile":2,
                "Big Data": 3,
                "Cloud": 4,
                "Database":5,
                "DevOps":6,
                "Integration":7,
                "IoT":8,
                "Mobile":9,
                "Performance":10,
                "Web Dev":11,
                "Security":2001,
                "AI":4001,
                "Microservices":6001,
                "Open Source":7001
         }
        option = pyip.inputMenu(list(categories.keys()), numbered=True)
        self.category_or_lastest(categories[option])




    def category_or_lastest(self,code:int = 0):
        if code:
            url = f"https://dzone.com/services/widget/article-listV2/list?portal={code}&sort=newest"
        else: 
            url = "https://dzone.com/services/widget/article-listV2/list?page=1&sort=newest"

        response = requests.get(url).text 
        # This function returns a dict object and in the nodes key we have an array of posts
        posts = json.loads(response)["result"]["data"]["nodes"] 
        for idx, post in enumerate(posts):
            # Variables from the JSON request 
            title, date, views, link = post["title"], post["articleDate"], post["views"],(self.BASE_URL + post['articleLink'])
            self.articles_title(idx + 1)
            print(f"{title}\nLink: {link}\nViews: {views}\nPublish date: {date}\n")


    def  articles_title(self, article_number:int, simb: str = '*'):
        print(f"{20*simb} Article #{article_number} {20*simb}\n")




