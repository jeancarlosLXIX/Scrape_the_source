from pages.BasicActions import BasicActions

class HackerNews(BasicActions):

    def __init__(self, link: str = 'https://news.ycombinator.com/news') -> None:
        super().__init__(link)

    def home_page(self):
        self.clean_terminal()
        posts = self.get_response(self.BASE_URL, "a.titlelink")

        number = 1
        for key,value in posts.items():
            
            if "https" not in value: value = "https://news.ycombinator.com/" + value
            
            self.separator(number,'News')
            print(f"{number}) {key}\nLINK:{value}\n")
            number += 1

    def menu(self):
        # TODO: loop menu here?
        page = 1
        self.home_page()
