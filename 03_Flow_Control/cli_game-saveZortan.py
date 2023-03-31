from typing import Final

IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life = 1500
choice = 0
attack_num = 0

#helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"
MSG = """
---------------------------------------------------------------------
Zortan is under attack, choose the pairs no. that will attack Thanos
1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
---------------------------------------------------------------------
"""
while True:
        if thanos_life <= 0 and attack_num <= 3:
                print(WIN_MSG)
                break
        elif thanos_life > 0 and attack_num == 3:
                print(LOST_MSG)
                break
        print(MSG)

        choice = int (input ("Enter your pair no. >>> "))

        if choice == 1:
                print("Ironman & Black Widow are attacking Thanos....")
                
                thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
                attack_num = attack_num + 1
                print (f"Thanos life is {thanos_life} now")  
        elif choice == 2:
                print("Black Widow & Spiderman are attacking Thanos...")
                thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
                attack_num += 1
                print (f"Thanos life is {thanos_life} now")       
        elif choice == 3:
                print("Spiderman & Hulk are attacking Thanos....")
                thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
                attack_num += 1
                print (f"Thanos life is {thanos_life} now")
        elif choice == 4:
                print("Hulk & Ironman are attacking Thanos....")
                thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
                attack_num += 1
                print (f"Thanos life is {thanos_life} now")