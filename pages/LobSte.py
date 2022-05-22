from pages.BasicActions import BasicActions
from bs4 import BeautifulSoup
import pyinputplus as pyip


class LobSte(BasicActions):
    def __init__(self, link: str = 'https://lobste.rs/') -> None:
        super().__init__(link)

    def home_page(self):
        obj = self.get_response(self.BASE_URL, "span.u-repost-of > a.u-url", soup_or_obj=True)
        
        self.print_news(obj)

    def category_search(self):
        category = pyip.inputMenu(["Languages","OS","Practices","Platforms","Tools"], numbered=True)
        response = self.get_response(self.BASE_URL + f"/categories/{category}", "span.u-repost-of > a.u-url", soup_or_obj=True)

        self.print_news(response)

    def menu(self):
        option = pyip.inputMenu(["Home page", "Category", "Exit"], numbered=True)
        
        if option == "Home page":
            self.home_page()

        elif option == "Category":
            self.category_search()