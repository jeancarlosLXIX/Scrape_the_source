from unittest.util import _MIN_COMMON_LEN
from urllib import response
from pages.BasicActions import BasicActions
import json
import requests

class HashNode(BasicActions):
    def __init__(self, link: str = ".hashnode.dev/") -> None:
        super().__init__(link)

    def comunity(self):
        page = 1
        while True:
            response = requests.get(f"https://hashnode.com/api/feed/community?page={page}").text 
            posts = json.loads(response)["posts"]
            self.print_hashnode(posts)
            
            _next = self.display_menu(["Next page", "Previous page"], "HashNode:")
            
            if _next == "Exit":
                break
            elif _next == "Next page":
                page += 1
            else:
                page -= 1
            self.clean_terminal()
    
    def categories(self):
        '''
        Display your blogs by category. (hashnode.com)
        '''
        categories = [
        "Javascript","Web-development", "Reactjs", 
        "Beginners", "Python", "CSS",
        "Programming-blogs", "Tutorials", "Developer"
        ]
        option = self.display_menu(categories,"Choose topic:") 

        posts = self.getting_posts(f"https://hashnode.com/api/feed/tag/{option.lower()}?type=hot&page=1")
        self.print_hashnode(posts)



    def trending(self) -> None:
        '''
        This function allows the user to select a current trend and see what he/she likes.
        
        '''
        trending = requests.get("https://hashnode.com/api/tag/trending?limit=6&category=week").text
        objs = json.loads(trending)["tags"]
        
        choices = []
        for obj in objs:
            # add the choice with a count
            choices.append(f'{obj["node"]["slug"]}: {obj["count"]}') 

        option = self.display_menu(choices,message="Select trending:").split(':')[0]

        if option == "Exit": return

        posts = self.getting_posts(f"https://hashnode.com/api/feed/tag/{option}?type=hot&page=1")

        self.print_hashnode(posts)



    def getting_posts(self, url:str) -> dict:
            response = requests.get(url).text 
            return json.loads(response)["posts"]

    def print_hashnode(self, posts: None):
        '''
        This function will be printing the blogs of HashNode
        :param posts: a list of dictionaries with the information that will be printed
        
        '''
        self.clean_terminal() 
        for idx,post in enumerate(posts):
                title,views =    post["title"], post["views"]
                has_domain  =    post["publication"]
                
                if has_domain != None: # Checking if the publication attrb exist
                    has_domain = has_domain.get("domain","")
                    user_name   =    post["publication"]["username"]
                
                self.separator(idx + 1, "Blog")
                # This is in case the blog is in another domain and not in hasnode domain
                if not has_domain: 
                    print(f"Title: {title}\nLink: https://{user_name+self.BASE_URL+post['slug']}")
                else:
                    print(f"Title: {title}\nLink: https://{has_domain+'/'+post['slug']}")
                print(f"Views: {views}\n")
    
    def menu(self):
        options = ["Comunity (lastest post)","See what's trending", "Categories"]
        option = self.display_menu(options,message="HashNode.com: \n")

        if option == options[-1]: # the function above add "Exit" to the list if doesn't exist
            return True
        
        if option == options[0]:
            self.comunity()
        if option == options[1]:
            self.trending()
        if option == options[2]:
            self.categories()
