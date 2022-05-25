import pyinputplus as pyip
from classes import dict_classes # Dictionary with all the classes

pages = list(dict_classes.keys()) + ["Exit"]

while True:
    option = pyip.inputMenu(pages, numbered=True)
    if option == "Exit": break
    dict_classes[option].clean_terminal()
    dict_classes[option].menu()
