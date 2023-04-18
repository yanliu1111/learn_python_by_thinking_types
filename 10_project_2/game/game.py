from random import randint
from typing import Final

def get_all_superheros() -> list[SuperHero]:
    ironman = SuperHero(name="Ironman", attack_power=250, life=1000)
    blackwidow = SuperHero(name="Blackwidow", attack_power=180, life=800)
    spiderman = SuperHero(name="Spiderman", attack_power=190, life=700)
    hulk = SuperHero(name="Hulk", attack_power=300, life=1100)
    
    superheros: list[SuperHero] = [ironman, blackwidow, spiderman, hulk]
    return superheros
def get_superhero(index: int) -> SuperHero | None:
    """Returns a superhero based on the index"""
    superheros = get_all_superheros()
    if index < 0 or index >= len(superheros):
        return None
    return superheros[index]

def get_all_villains() -> list[Villain]:
    thanos = Villain(name="Thanos", attack_power=400, life=1500)
    redskull = Villain(name="Redskull", attack_power=300, life=800)
    proxima = Villain(name="Proxima", attack_power=320, life=800)

    villains: list[Character] = [thanos, redskull, proxima]
    return villains

def get_villain(index: int) -> Villain | None:
    """Returns a villain based on the index"""
    villains = get_all_villains()
    if index < 0 or index >= len(villains):
        return None
    return villains[index]

#-------------------------main logic-------------------------------
def attack()-> None:
    for attack_num in range (3):
        hero_index = randint(0, 3)
        villain_index = randint (0, 2)
        current_superhero = get_superhero(hero_index)
        current_villain = get_villain(villain_index)

        if current_superhero and current_villain:
            simulate_attack(attack_num, current_superhero, current_villain)
        else:
            print("Invalid superhero or villain index.")

def simulate_attack(attack_num: int, superhero: SuperHero, villain: Villain) -> None:         
    Life.inc_hero_life(superhero.life)
    Life.inc_villain_life(villain.life)
    
    print(
        f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villain.name}."
    )

    Life.dec_hero_life(villain.attack_power)
    Life.dec_villain_life(superhero.attack_power)

print('='*70)
def win_or_lose() -> None:
    #helper messages
    WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"
    if Life.hero_life>=Life.villain_life:
        print (WIN_MSG)
    else:
        print(LOST_MSG)

def main() -> None:
    attack()
    win_or_lose()

if __name__ == "__main__": # if this file is run directly
    main()