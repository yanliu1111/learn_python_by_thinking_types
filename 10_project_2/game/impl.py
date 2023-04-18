from random import randint

from .models.superheros import SuperHeroModel
from .models.villains import VillainModel

from .schemas.player import Player
from .schemas.game_state import GameState

class Game:
    def __init__(self, player: Player)->None:
        self.player = player
        self.state = GameState.INITIALIZING
        self.superheros = SuperHeroModel() # Check back in models, there is no any argument in superheromodel
        self.villains = VillainModel()
    def __repr__(self) -> str:
        return "<class 'Game'>"
    def start(self)-> None:
        return f"Player: {self.player},\nState: {self.state},\nSuperheros: {self.superheros},\nVillains: {self.villains}"

#-------------------------Attact main logic/ move below code under the class-------------------------------
    def attack(self)-> None:
        for attack_num in range (3):
            hero_index = randint(0, 3)
            villain_index = randint (0, 2)
            current_superhero = get_superhero(hero_index)
            current_villain = get_villain(villain_index)

            if current_superhero and current_villain:
                simulate_attack(attack_num, current_superhero, current_villain)
            else:
                print("Invalid superhero or villain index.")

    def simulate_attack(self, attack_num: int, superhero: SuperHero, villain: Villain) -> None:         
        Life.inc_hero_life(superhero.life)
        Life.inc_villain_life(villain.life)
        
        print(
            f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villain.name}."
        )

        Life.dec_hero_life(villain.attack_power)
        Life.dec_villain_life(superhero.attack_power)

    print('='*70)
    def win_or_lose(self) -> None:
        #helper messages
        WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
        LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"
        if Life.hero_life>=Life.villain_life:
            print (WIN_MSG)
        else:
            print(LOST_MSG)

    