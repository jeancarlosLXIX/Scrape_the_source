from pages.BasicActions import BasicActions
import pyinputplus as pyip

class HackerNews(BasicActions):

    def __init__(self, link: str = 'https://news.ycombinator.com/news') -> None:
        super().__init__(link)

    def home_page(self,url):
        self.clean_terminal()
        posts = self.get_response(url, "a.titlelink")

        number = 1
        for key,value in posts.items():
            
            if "https" not in value: value = "https://news.ycombinator.com/" + value
            
            self.separator(number,'News')
            print(f"{number}) {key}\nLINK:{value}\n")
            number += 1

    def menu(self):
        # TODO: loop menu here?
        page = 1
        while True:
            self.home_page(url=f"https://news.ycombinator.com/news?p={page}")

            break_loop = self.display_menu(["Next", "Previous"],"Action")

            if break_loop == "Exit":
                break

            if break_loop == "Next":
                page += 1
            else:
                if page == 1: continue 
                page -= 1
