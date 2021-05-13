#CLASSES
class Character:
    def __init__(self, health, power, name):
        pass
    def attack(self, target):
            if isinstance(target, Zombie):
                print("The attack doesn’t seem to have any effect. ")
            else:
                target.health -= self.power
                print(“%s does %d damage to %s!” % (self.name, self.power, target.name))
    def sleep(self, target):
        self.health -= target.power
        print(“%s does %d damange to %s!” % (target.name, target.power, self.name))
    def alive(self):
        if (self.health > 0):
            return True
        elif (self.health <= 0):
            print(“RIP in peace, %s...” % self.name)
            print()
        elif (target.health) <= 0:
            print(“RIP in peace, %s...” % target.name)
            print()
        elif transition():
            start = input("BOSS BATTLE n/ THANOS ")
            print(("/033c"))


    def print_status(self):
        print(“%s has %d health and %d power.” % (self.name, self.health, self.power))

    
class Hero(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
class Goblin(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
class Zombie(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
#INSTANCES
satine = Hero(10, 5, “Satine”)
monstera = Goblin(10, 2, “Monstera”)
zombie = Zombie(666, 100, “Dead Dude”)


def transition():
    pause = input(“PRESS ENTER TO CONTINUE...“)
    print(“\033c”)
#GLOBAL FUNCTIONS
def main():
    print()
    print("""
**************************************
**************************************
**                                  **
***   Welcome to the THUNDERDOME   ***
**                                  **
**************************************
**************************************
    """)
    print()
    transition()
    satine.print_status()
    monstera.print_status()
    while monstera.alive() and satine.alive():
        print()
        print(“Whatchu gonna do mf-er?!“)
        print(“1. FIGHT!“)
        print(“2. sleeeep”)
        print(“3. Ah ShIT! (Run)“)
        print(“>”,)
        user_input = input()
        if user_input == “1":
                print()
                print(“~Final Fantasy Battle Music Ensues~“)
                print()
                satine.attack(monstera)
                monstera.attack(satine)
        elif user_input == “2”:
            print()
            print(“Sleepy baby... B O N K”)
            print()
            satine.sleep(monstera)
            print()
        elif user_input == “3”:
            print()
            print(“See ya later Weenie Hut Jr!“)
            print()
            break
        else:
            print(“Wtf is %r???” % user_input)
main()