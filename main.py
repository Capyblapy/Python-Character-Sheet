import os #os.system('cls')
from information import pages
from information import classes
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def getInput(inputString, type):
    newInput = input(inputString)

    if type == float:
        try:
            value = float(newInput)
            return value
        except:
            print("You did not give a number!")
            return getInput(inputString, type)
    elif type == int:
        try:
            value = int(newInput)
            return value
        except:
            print("You did not give a intiger!")
            return getInput(inputString, type)    
    elif type == str:
        try:
            value = str(newInput)
            return value
        except:
            print("You did not give a string!")
            return getInput(inputString, type)

selectedPage = 1
def initNewPage():
    global selectedPage

    os.system('cls')

    for page in pages:
        pageInfo = pages[page]

        if page == selectedPage:
            print(color.BOLD + '[' + color.RED + str(page) + color.END + '] - ' + color.RED + pageInfo["Name"] + color.END + color.END + " ", end=' ')
        else:
            print('[' + str(page) +'] - ' + pageInfo["Name"] + " ", end=' ')

    print("")
    print("---------------------------")
    print("")

    pages[selectedPage]["Func"]()

    print("")
    newPage = getInput("Page: ", int)

    try:
        pages[newPage] # checking if its valid lol
        selectedPage = newPage
    except:
        selectedPage = selectedPage
    initNewPage()

initNewPage()