from pages.TECH import Dzone, FreeCodeCamp, HashNode, TechCrunch, LobSte, HackerNews
from pages.VG import GameSpot 

list_of_classes = [
    Dzone.Dzone, FreeCodeCamp.FCC,HashNode.HashNode,
    TechCrunch.TechCrunch, LobSte.LobSte, HackerNews.HackerNews
]

list_of_instances = [_instance() for _instance in list_of_classes]

dict_classes = {
    "Dzone": Dzone.Dzone(),
    "Free Code Camp": FreeCodeCamp.FCC(),
    "Hash Node": HashNode.HashNode(),
    "Tech Crunch": TechCrunch.TechCrunch(),
    "LobSte": LobSte.LobSte(),
    "Hacker news": HackerNews.HackerNews(),
    "Game Spot": GameSpot.GameSpot()
}

if __name__ == "__main__":
    # Here you can test every instance  individually
    dict_classes["Free Code Camp"].menu()