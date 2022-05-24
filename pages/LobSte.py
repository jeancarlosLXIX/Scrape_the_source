from pages.BasicActions import BasicActions


class LobSte(BasicActions):
    def __init__(self, link: str = 'https://lobste.rs/') -> None:
        super().__init__(link)

    def home_page(self):
        obj = self.get_response(self.BASE_URL, "span.u-repost-of > a.u-url", soup_or_obj=True)
        
        self.print_news(obj)

    def category_search(self):
        category = self.display_menu(["Languages","OS","Practices","Platforms","Tools"])
        response = self.get_response(self.BASE_URL + f"/categories/{category}", "span.u-repost-of > a.u-url", soup_or_obj=True)

        self.print_news(response)

    def menu(self):
        option = self.printing_menu(["Home page", "Category"])
        
        if option == "Home page":
            self.home_page()

        elif option == "Category":
            self.category_search()