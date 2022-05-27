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

if __name__ == "__main__":
    # Here I test every instance I want individually
    dict_classes["Dzone"].menu()