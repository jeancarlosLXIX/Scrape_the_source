import json
import requests
from pages.BasicActions import BasicActions


class Dzone(BasicActions):
    def __init__(self, url:str = "https://dzone.com") -> None:
        super().__init__(url)
    
    def lastest(self, url):
        '''
        This function will print the lastests news from Dzone
        '''
        response = requests.get(url).text 
        posts = json.loads(response)["result"]["data"]["nodes"]
        for idx, post in enumerate(posts):
            views, link = post["views"],(self.BASE_URL + post['articleLink'])
            self.separator(idx + 1,'Article')
            print(f"{post['title']}\nLink: {link}\nViews: {views}\nPublish date: {post['articleDate']}\n")
    
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
        option = self.display_menu(list(categories.keys()),"Choose category:")
        if option != "Exit":
            self.next_page(
                func=self.category,
                arg=f"https://dzone.com/services/widget/article-listV2/list?portal={categories[option]}&sort=newest&page=1",
                reg="page=\d*",
                replace_with="page="
            )


    def category(self,url):
        self.clean_terminal()

        response = requests.get(url).text 
        # This function returns a dict object and in the nodes key we have an array of posts
        posts = json.loads(response)["result"]["data"]["nodes"]
        for idx, post in enumerate(posts):
            views, link = post["views"],(self.BASE_URL + post['articleLink'])
            self.separator(idx + 1,'Article')
            print(f"{post['title']}\nLink: {link}\nViews: {views}\nPublish date: {post['articleDate']}\n")



    def menu(self):
        choices = ["Lastest news","Category"]
        option = self.display_menu(choices, "DZone: ")

        if option not in choices:
            return

        if option == choices[0]:
            url = "https://dzone.com/services/widget/article-listV2/list?sort=newest&page=1"
            self.next_page(self.lastest,arg=url, reg="page=\d*", replace_with="page=" )
        if option == choices[1]:
            self.read_by_category()