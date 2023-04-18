from random import randint
from typing import Final
from enum import Enum, auto

# Enum is a class that has a set of constants
class CharacterType(Enum):
    SUPERHERO = auto()
    VILLAIN = auto()

class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life
    def __str__(self) -> str:
        return f"name: {self.name}, attack power: {self.attack_power}, life: {self.life}"   

class SuperHero(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.SUPERHERO
    def __str__(self) -> str:
        return (
        f"Superhero => name: {self.name}, attack power: {self.attack_power}, "  
        f"life: {self.life}" 
        )
class Villain (Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLAIN
    def __str__(self) -> str:
        return (
        f"Villain => name: {self.name}, attack power: {self.attack_power}, "  
        f"life: {self.life}" 
        )


#-------------------------BEFORE-------------------------------

class Life:
    hero_life = 0
    villain_life = 0

    @staticmethod # static method is a method that does not use the instance, we can call static method from the class itself
    # other example, if have common functionality such as datetime.now() or datetime.today(), we dont need to create new instance
    # static method is does not take a self argument because it works directly with the class and not on the instance
    def inc_hero_life(life: int) -> None:
        Life.hero_life += life
    @staticmethod
    def dec_hero_life(life: int) -> None:
        Life.hero_life -= life
    @staticmethod
    def inc_villain_life(life: int) -> None:
        Life.villain_life += life

    @staticmethod
    def dec_villain_life(life: int) -> None:
        Life.villain_life -= life

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

    villains: list[Villain] = [thanos, redskull, proxima]
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