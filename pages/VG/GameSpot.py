from pages.BasicActions import BasicActions

class GameSpot(BasicActions):
   
    def __init__(self, link: str = "https://www.gamespot.com/news") -> None:
        super().__init__(link)
    

    def lastest(self):
        response = self.get_response(self.BASE_URL,soup_or_obj=False)
        objs = self.create_obj(response,"a.card-item__link")
        titles = list(objs.keys())

        for idx,title in enumerate(titles):
            self.separator(idx + 1,"News")
            print(f"{title}\n{'https://www.gamespot.com' + objs[title]}\n")

    
    def menu(self):
        self.lastest()