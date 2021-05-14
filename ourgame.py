# class Character:

#     def __init__(self, health, power, name):
#         pass

#     def attack(self, target):
#             if isinstance(target, Zombie):
#                 print("The attack doesn't seem to have any effect.")
#             else:
#                 target.health -= self.power
#                 print("%s does %d damage to %s!" % (self.name, self.power, target.name))

#     def sleep(self, target):
#         self.health -= target.power
#         print("%s does %d damange to %s!" % (target.name, target.power, self.name))

#     def alive(self):
#         if (self.health > 0):
#             return True
#         elif (self.health <= 0):
#             print("RIP in peace, %s..." % self.name)
#             print()
#         elif (target.health <= 0):
#             print("RIP in peace, %s..." % target.name)
#             print()

#     def print_status(self):
#         print("%s has %d health and %d power." % (self.name, self.health, self.power))





###CLASSES
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

class Super_Villian(Villian):
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health


###FIGHTER LIBRARY
fighters = {}

# fighters["Hero"] = hero_choice 
# fighers["Villian"] = villian_choice


###INSTANCES
#HEROS
wolverine = Hero(70, 25, "Wolverine")
spider_man = Hero(70, 25, "Spider-Man")
captain_america = Hero(80, 55, "Captain America")
deadpool = Hero(60, 40, "Deadpool")
#VILLIANS
green_goblin = Villian(30, 15, "Green Goblin")
venom = Villian(60, 35, "Venom")
loki = Villian(20, 50, "Loki")
red_skull = Villian(50, 35, "Red Skull")
#BOSS
thanos = Super_Villian(200, 200, "Thanos")


###INTRO SCREEN
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


###HERO MENU
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


###VILLIAN SELECTION SCREEN
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


###BATTLE
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


###GLOBAL FUNCTIONS
def main():

    #INTRO
    intro_screen()

    #HERO SELECTION
    hero_menu()
    user_input = input()
    if user_input == "Wolverine":
        print()
        print("You've chosen Wolverine as your super hero!")
        print()
        pause = input("Press ENTER to select your VILLIAN!!! >:( ")
        print()
        print("\033c")
    elif user_input == "Captain America":
        print()
        print("You've chosen Captain America as your super hero!")
        print()
        pause = input("Press ENTER to select your VILLIAN!!! >:( ")
        print()
        print("\033c")
    elif user_input == "Spider-Man":
        print()
        print("You've chosen Spider-Man as your super hero!")
        print()
        pause = input("Press ENTER to select your VILLIAN!!! >:( ")
        print()
        print("\033c")
    elif user_input == "Deadpool":
        print()
        print("You've chosen Deadpool as your super hero! (But is he really though...?)")
        print()
        pause = input("Press ENTER to select your VILLIAN!!! >:( ")
        print()
        print("\033c")
    else:
        print("Who is that???")

    #VILLIAN SELECTION
    villian_menu()
    user_input = input()
    if user_input == "Green Goblin":
        print()
        print("You've chosen Green Goblin as your villian...")
        print()
        pause = input("PRESS ENTER TO FIGHT!")
        print()
        print("\033c")
    elif user_input == "Loki":
        print()
        print("You've chosen Loki as your villian...")
        print()
        pause = input("PRESS ENTER TO FIGHT!")
        print()
        print("\033c")
    elif user_input == "Venom":
        print()
        print("You've chosen Venom as your villian...")
        print()
        pause = input("PRESS ENTER TO FIGHT!")
        print()
        print("\033c")
    elif user_input == "Red Skull":
        print()
        print("You've chosen Red Skull as your villian...")
        print()
        pause = input("PRESS ENTER TO FIGHT!")
        print()
        print("\033c")
    else:
        print("Who is that???")
    




#####OLD CODE
    # satine.print_status()
    # monstera.print_status()

    # while monstera.alive() and satine.alive():

    #     print()
    #     print("Whatchu gonna do mf-er?!")
    #     print("1. FIGHT!")
    #     print("2. sleeeep")
    #     print("3. Ah ShIT! (Run)")
    #     print(">",)
    #     user_input = input()

    #     if user_input == "1":
    #             print()
    #             print("~Final Fantasy Battle Music Ensues~")
    #             print()
    #             satine.attack(monstera)
    #             monstera.attack(satine)
       
    #     elif user_input == "2":
    #         print()
    #         print("Sleepy baby... B O N K")
    #         print()
    #         satine.sleep(monstera)
    #         print()
        
    #     elif user_input == "3":
    #         print()
    #         print("See ya later Weenie Hut Jr!")
    #         print()
    #         break
        
    #     else:
    #         print("Wtf is %r???" % user_input)

main()