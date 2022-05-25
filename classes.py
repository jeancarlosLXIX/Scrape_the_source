from pages import Dzone, FreeCodeCamp, HashNode, TechCrunch, LobSte, HackerNews

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
    "Hacker news": HackerNews.HackerNews()
}

dict_classes["Tech Crunch"].print_lastest()