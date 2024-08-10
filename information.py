# This section is for all of the page related storage.
def overviewPage():
    print("This is the overview page!")
    print(r"""
                    /)
            /\___/\ ((
            \`@_@'/  ))
            {_:Y:.}_//
    ----------{_}^-'{_}----------
    """)

def editPage():
    print(":P (got lazy no art!)")

pages = {
    1: {
        "Name": "Overview",
        "Func": overviewPage,
    },
    2: {
        "Name": "Edit",
        "Func": editPage,
    },
}

# This section is for all of the class related storage.
classes = {
    "Druid": {
        "Spellcasting": {
            "Save": "8 + prof bonus + wis modifier",
            "Attack": "prof bonus + wis modifier",
            "SpellList": {
            
            },
        },
        "Levels": {
            1: {
                "Features": {
                    "Druidic",
                    "Spellcasting",
                },
                "CantripCount": 2,
                "Spellslots": {
                    1: 2,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                    6: 0,
                    7: 0,
                    8: 0,
                    9: 0,
                },
            },
            2: {
                "Features": {
                    "Wild Shape",
                    "Druid Circle",
                },
                "CantripCount": 2,
                "Spellslots": {
                    1: 3,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                    6: 0,
                    7: 0,
                    8: 0,
                    9: 0,
                },
            },
        },
        "SubclassPrefix": "Circle of {name}",
        "Subclasses": {
            "Spores" : {
                2: {
                    "Features": {
                        "Halo of Spores",
                        "Symbiotic Entity",
                    },
                    "Cantrips": {
                        "Chill Touch",
                    },
                    "Spells": {},
                }
            }
        },
    }
}

# This section is for all of the class features
features = {

}

# This section is for all of the spells
spells = {
    
}