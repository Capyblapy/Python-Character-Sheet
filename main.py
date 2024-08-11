import os #os.system('cls')
from utils import *

from information.pages import pages
from information.classes import classes
from information.spells import spells
from information.features import features

selectedPage = 1
def initNewPage():
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

    pages[selectedPage]["Func"]()

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

initNewPage()