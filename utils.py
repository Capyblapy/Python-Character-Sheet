# Save data helper
import json
import os

#filename = "character.json"
writing = False

template = {
    "name": "N/A",
    "inventory": {},

    "hp": 0,
    "stats": {
        "strength": 0,
        "dexterity": 0,
        "consitution": 0,
        "intelligence": 0,
        "wisdom": 0,
        "charisma": 0
    },

    "classes": {},
    "cantrips": {},
    "spells": {},
    "spell-slots": {}
}

def checkForCharacter(filename):
    # Checks for file if not exist make one!
    if not os.path.exists('characters/'+filename+'.json'):
        _file = open('characters/'+filename+'.json', 'w')
        json.dump(template, _file)
        _file.close()

    return True

def getData(filename):
    # Make it return not saved if its already being written!!
    global writing
    if writing == True:
        return False
    
    if checkForCharacter(filename) == True:
        _file = open('characters/'+filename+'.json', 'r')
        data = json.load(_file)
        _file.close()

        return data
    else:
        return False

# JSON utils not done i need to write a setData function

# Other utils
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