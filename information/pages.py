from utils import *

# This section is for all of the page related storage.
def overviewPage():
    characterData = getData()
    if characterData == False:
        print("Error Loading data!")
        return

    print(characterData)

pages = {
    1: {
        "Name": "Overview",
        "Func": overviewPage,
    },
}