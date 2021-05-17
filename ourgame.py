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
# HERO CLASS
class Hero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def alive(self):
        if (self.health > 0):
            return True
        elif (self.health <= 0):
            print("%s has been defeated!" % (self.name))
            print()

    def attack(self, villian):
        if (self, villian):
            villian.health -= self.power
            print()
            print("%s does %d damage to %s!" % (self.name, self.power, villian.name))
            print()

    def block(self, villian):
        self.health -= villian.power/2
        print("%s does %d damage to %s!" % (villian.name, villian.power/2, self.name))
        print()
        
#VILLIAN CLASS
class Villian:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def alive(self):
        if (self.health > 0):
            return True
        elif (self.health <= 0):
            print("%s has been defeated!" % (self.name))
            print()

    def attack(self, hero):
        if (self, hero):
                hero.health -= self.power
                print("%s does %d damage to %s!" % (self.name, self.power, hero.name))
                print()


### INSTANCES
# HEROS
wolverine = Hero("Wolverine", 25, 70)
spider_man = Hero("Spider-Man", 20, 75)
captain_america = Hero("Captain America", 30, 80)
deadpool = Hero("Deadpool", 35, 60)
# VILLIANS
green_goblin = Villian("Green Goblin", 15, 40)
venom = Villian("Venom", 20, 60)
loki = Villian("Loki", 30, 55)
red_skull = Villian("Red Skull", 25, 50)


### GLOBAL FUNCTIONS
def main():

    # INTRO
    intro_screen()


    # HERO SELECTION
    hero_menu()
    hero_input = input()
    if hero_input == "Wolverine":
        hero = wolverine
        print("\033c")
    elif hero_input == "Captain America":
        hero = captain_america
        print("\033c")
    elif hero_input == "Spider-Man":
        hero = spider_man
        print("\033c")
    elif hero_input == "Deadpool":
        hero = deadpool
        print("\033c")
    else:
        print("Who is that???")


    # VILLIAN SELECTION
    villian_menu()
    villian_input = input()
    if villian_input == "Green Goblin":
        villian = green_goblin
        print("\033c")
    elif villian_input == "Loki":
        villian = loki
        print("\033c")
    elif villian_input == "Venom":
        villian = venom
        print("\033c")
    elif villian_input == "Red Skull":
        villian = red_skull
        print("\033c")
    else:
        print("Who is that???")


    # READY TO BATTLE?
    print("""Super Hero Selection:
Name: %s
Power: %d
Health: %d
""" % (hero.name, hero.power, hero.health))

    print("""Villian Selection:
Name: %s
""" % (villian.name))

    pause = input("""PRESS ENTER TO FIGHT!!!
""")
    print("\033c")


# MOVE SELECTION
    while hero.alive() and villian.alive():
        print("""CHOOSE YOUR MOVE:
1. Attack
2. Block
3. Quit
    """)
        user_input = input()

        if user_input == "1":
            hero.attack(villian)
            villian.attack(hero)

        elif user_input == "2":
            hero.block(villian)

        elif user_input == "3":
            print()
            print("Loooooser!")
            print()
            break

        else:
            print()
            print("Not a valid selection")
            print()


main()