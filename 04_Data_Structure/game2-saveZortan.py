from random import randint
from typing import Final

Character = dict[str, str|int]
IRONMAN: Final[Character] = {"name": "Ironman", "attack_power":250,"life":1000}
BLACKWIDOW: Final[Character] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[Character] = {"name": "Hulk", "attack_power": 300, "life": 1100}

THANOS: Final[Character] = {"name": "Thanos", "attack_power": 400, "life": 1500}
REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800}

superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
villains: list[Character] = [THANOS, REDSKULL, PROXIMA]

hero_life = 0
villain_life = 0

#helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

for attack in range (3):
    hero_index = randint(0, 3)
    villain_index = randint (0, 2)
    current_superhero = superheros [hero_index]
    current_villain = villains [villain_index]

    hero_life += current_superhero['life']
    villain_life += current_villain['life']
    print(
        f"Attack: {attack + 1} => {current_superhero['name']} is going to fight with {current_villain['name']}."
    )

    hero_life -= current_villain["attack_power"]
    villain_life -= current_superhero["attack_power"]
print('='*70)

if hero_life>=villain_life:
    print (WIN_MSG)
else:
    print(LOST_MSG)