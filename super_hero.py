#INSTANCES
#HERO'S
def hero_menu():
    pause = input("WHO DO YOU WANT CHOOSE")
    print("\033c")

wolverine = Hero(70, 25, "Wolverine")
spider_man = Hero(70, 25, "Spider Man")
captain_America = Hero(80, 55, "Captain America")
deadpool = Hero(60, 40, "Deadpool")

#VILLIAN
def villian_menu():
    pause = input("CHOOSE YOUR VILLIAN")
    print("\033c")

green_goblin = villian(30, 15, "Green Goblin")
venom = villian(60, 35, "Venom")
loki = villian(20, 50, "Loki")
red_skull(50, 35, "Red Skull")

#BOSS
thanos = super_villian(200, 200, "Thanos")
#BOSS Print Out
    print()
    print("""

        ,----,                                                                 
      ,/   .`|       ,--,                        ,--.    ,----..               
    ,`   .'  :     ,--.'|   ,---,              ,--.'|   /   /   \   .--.--.    
  ;    ;     /  ,--,  | :  '  .' \         ,--,:  : |  /   .     : /  /    '.  
.'___,/    ,',---.'|  : ' /  ;    '.    ,`--.'`|  ' : .   /   ;.  \  :  /`. /  
|    :     | |   | : _' |:  :       \   |   :  :  | |.   ;   /  ` ;  |  |--`   
;    |.';  ; :   : |.'  |:  |   /\   \  :   |   \ | :;   |  ; \ ; |  :  ;_     
`----'  |  | |   ' '  ; :|  :  ' ;.   : |   : '  '; ||   :  | ; | '\  \    `.  
    '   :  ; '   |  .'. ||  |  ;/  \   \'   ' ;.    ;.   |  ' ' ' : `----.   \ 
    |   |  ' |   | :  | ''  :  | \  \ ,'|   | | \   |'   ;  \; /  | __ \  \  | 
    '   :  | '   : |  : ;|  |  '  '--'  '   : |  ; .' \   \  ',  / /  /`--'  / 
    ;   |.'  |   | '  ,/ |  :  :        |   | '`--'    ;   :    / '--'.     /  
    '---'    ;   : ;--'  |  | ,'        '   : |         \   \ .'    `--'---'   
             |   ,/      `--''          ;   |.'          `---`                 
             '---'                      '---'                                  
    
""")
print()
boss_transition()                                                                               
