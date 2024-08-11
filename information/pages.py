from utils import *

# This section is for all of the page related storage.
def overviewPage(args):
    args = args["overview"]

    characterData = getData(args[1])
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