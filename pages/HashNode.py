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
            for idx,post in enumerate(posts):
                title,views,hasDomain = post["title"], post["views"], post["publication"].get("domain","")
                userName = post["publication"]["username"]
                
                self.separator(idx + 1, "Blog")
                if not hasDomain:
                    print(f"Title: {title}\nLink: https://{userName+self.BASE_URL+post['slug']}")
                else:
                    print(f"Title: {title}\nLink: https://{hasDomain+'/'+post['slug']}")
                print(f"Views: {views}\n")
            
            _next = self.printing_menu(["Next page", "Previous page"])
            
            if _next == "Exit":
                break
            elif _next == "Next page":
                page += 1
            else:
                page -= 1
            self.clean_terminal()


# https://hashnode.com/api/feed/community?page=1