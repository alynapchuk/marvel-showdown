### INTRO SCREEN
def intro_screen():
    print("""
                               ,,,, 
                         ,;) .';;;;',
             ;;,,_,-.-.,;;'_,|I\;;;/),,_
              `';;/:|:);{ ;;;|| \;/ /;;;\__
                  L;/-';/ \;;\',/;\/;;;.') ;
                  .:`''` - \;;'.__/;;;/  . _'-._ 
                .'/   \     \;;;;;;/.'_7:.  '). \_
              .''/     | '._ );}{;//.'    '-:  '.,L
WITH GREAT  .'. /       \  ( |;;;/_/         \._./;\   _,
POWER,       . /        |\ ( /;;/_/             ';;;\,;;_,
COMES GREAT             )__(/;;/_/                (;;'''''
RESPONSIBILITY        _;:':;;;;:';-._             );
                     /   \  `'`   --.'-._         \/
                   .'     '.  ,'         '-,
                  /    /   r--,..__       '.
                .'    '  .'        '--._     ]
                (     :.(;>        _ .' '- ;/
                |      /:;(    ,_.';(   __.'
                 '- -'"|;:/    (;;;;-'--'
                       |;/      ;;(
                       ''      /;;|
                               \;;|
                                \/
""")
    pause = input("""
      PRESS ENTER TO PLAY!
""")
    print("\033c")


### HERO MENU
def hero_menu():
    print("""
--------------------------------------
| ***** CHOOSE YOUR SUPER HERO ***** |
--------------------------------------
|                                    |
|   Wolverine           Spider-Man   |
|                                    |
|   Captain America     Deadpool     |
|                                    |
--------------------------------------

WHO DO YOU CHOOSE?
""")


### VILLIAN SELECTION SCREEN
def villian_menu():
    print("""
--------------------------------------
| ****** CHOOSE YOUR VILLIAN ******* | 
--------------------------------------
|                                    |
|   Green Goblin       Venom         |
|                                    |
|   Loki               Red Skull     |
|                                    |
--------------------------------------

WHO WILL YOUR SUPER HERO FIGHT?
""")


### CLASSES
class Hero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

class Villian:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health


### INSTANCES
# HEROS
wolverine = Hero("Wolverine", 25, 70)
spider_man = Hero("Spider-Man", 25, 70)
captain_america = Hero("Captain America", 55, 80)
deadpool = Hero("Deadpool", 40, 60)
# VILLIANS
green_goblin = Villian("Green Goblin", 15, 30)
venom = Villian("Venom", 35, 60)
loki = Villian("Loki", 50, 20)
red_skull = Villian("Red Skull", 35, 50)


### FIGHTER LIBRARY
# HEROS
hero_fighters = [
    {
        "name": "Captain America",
        "alias": "Steve Rogers",
        "gear": ["Shield", "Super Strength"],
    },
    {
         "name": "Spider-Man",
        "alias": "Peter Parker",
        "gear": ["Mechanical Arms", "Spider-Web"],
    },
    {
        "name": "Wolverine",
        "alias": "James Howlett aka Logan",
        "gear": ["Claws", "Daggers"],
    },
    {
        "name": "Deadpool",
        "alias": "Wade Wilson",
        "gear": ["Sarcasim", "Killer Humor", "Regeneration", "Katanas"]

    }
]

# VILLIANS
villian_fighters = [
     {
         "name": "Green Goblin",
         "alias": "Norman Osborn",
         "gear": ["Hoverboard", "Pumpkin Bombs"]
     },
     {
         "name": "Loki",
         "alias": "God of Mischief",
         "gear": ["Dagger", "Shape Shifter"]
     },
     {
         "name": "Venom",
         "alias": "Eddie Brock",
         "gear": ["Undetectable by Spiderman", "Super Strength",]
     },
     {
         "name": "Red Skull",
         "alias": "Johann Schmidt",
         "gear": ["Willpower", "Reality Warp"]
     }
]

hero_input = hero_fighters
villian_input = villian_fighters


### BATTLE
def status(self, villian):
    print("%s has %s health." % (self.name, self.health))

def attack(self, villian):
    villian.health -= self.power

def block(self, villian):
    self.health -= villian.power/2

def dead(self, villian):
    if (self.health > 0):
        return True
    elif (self.health <= 0):
        print("%s has been defeated!" % self.name)
        print()
    elif (villian.health <= 0):
        print("%s has been defeated!" % villian.name)
        print()


### GLOBAL FUNCTIONS
def main():

    # INTRO
    intro_screen()

    # HERO SELECTION
    hero_menu()
    hero_input = input()
    if hero_input == "Wolverine":
        print("\033c")
    elif hero_input == "Captain America":
        print("\033c")
    elif hero_input == "Spider-Man":
        print("\033c")
    elif hero_input == "Deadpool":
        print("\033c")
    else:
        print("Who is that???")

    # VILLIAN SELECTION
    villian_menu()
    villian_input = input()
    if villian_input == "Green Goblin":
        print("\033c")
    elif villian_input == "Loki":
        print("\033c")
    elif villian_input == "Venom":
        print("\033c")
    elif villian_input == "Red Skull":
        print("\033c")
    else:
        print("Who is that???")

    # READY TO BATTLE?
    print("""
Super Hero Selection:
Name:
Power:
Health:
""")
    print()
    print("""
Villian Selection:
Name:
Power:
Health:
""")

main()