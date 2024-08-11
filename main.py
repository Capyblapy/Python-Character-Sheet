import os
os.system('cls')

from utils import *

from information.pages import pages
from information.classes import classes
from information.spells import spells
from information.features import features

characterFileName = None
def Start():
    global characterFileName
    
    characters = {}
    os.system('cls')

    index = 1
    for filename in os.listdir('characters'):
        f = os.path.join('characters', filename)

        # checking if it is a file and is json
        if os.path.isfile(f) and f.lower().endswith(('.json')):
            characters[index] = getData(str(index))
            index += 1
    
    for _index in characters:
        data = characters[_index]

        string = f"{color.BOLD}[{color.RED}{str(_index)}{color.END}] - {data['name']}{color.END}"
        print(string)
    print(f"{color.BOLD}[{color.RED}{str(index)}{color.END}] - Make a new character{color.END}")
    
    selectedCharacter = input(f"Character [{color.RED}#{color.END}] - ")
    try:
        if characters.get(int(selectedCharacter)):
            data = characters[int(selectedCharacter)]
        elif int(selectedCharacter) == index:
            data = "new"
        else:
            Start()
            return
    except:
        Start()
        return
    
    if data == "new":
        print("insert character creator here")
    else:
        characterFileName = selectedCharacter
        Header()

selectedPage = 1
def Header():
    global selectedPage

    os.system('cls')

    charNum = 2 # Set this to how many EXTRA - you want.
    for page in pages:
        pageInfo = pages[page]

        if page == selectedPage:
            string = f"{color.BOLD}[{color.RED}{str(page)}{color.END}] - {color.RED}{pageInfo['Name']}{color.END}{color.END} "
        else:
            string = f"[{str(page)}] - {pageInfo["Name"]} "

        charNum += len('['+str(page)+'] - '+pageInfo["Name"])
        print(string, end=' ')

    print("")
    for _ in range(charNum):
        print("-",end='')
    print("")

    args = {
        "overview": {
            1: characterFileName
        }
    }
    pages[selectedPage]["Func"](args)

    # Test code to test if basic code worked or not!
    #print("")
    #newPage = input("Page #: ")
    #
    #try:
    #    pages[int(newPage)] # checking if its valid lol
    #    selectedPage = int(newPage)
    #except:
    #    selectedPage = selectedPage
    #initNewPage()

Start()