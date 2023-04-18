from __future__ import annotations

from random import randint
from .constants import NUM_ATTACKS, WIN_MSG, LOST_MSG
from .models.superheros import SuperHeroModel
from .models.villains import VillainModel

from .schemas.player import Player
from .schemas.game_state import GameState
from .schemas.superhero import SuperHero
from .schemas.villain import Villain
from .schemas.life import Life

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
    def attack(self)-> Game: # have to import annotations
        self.state = GameState.IN_PROGRESS
        print("Starting attack...")
        print(self.state)

        #Attack
        for attack_num in range (NUM_ATTACKS):
            hero_index = randint(0, len(self.superheros.all) - 1)
            villain_index = randint (0, len(self.villains.all) - 1)
            current_superhero = self.superheros.get_superhero(hero_index)
            current_villain = self.villains.get_villain(villain_index)

            if current_superhero and current_villain:
                self.__do_attack(attack_num, current_superhero, current_villain)
            else:
                print("Error, no superhero or villain to fight with.")
        return self
    
    def __do_attack(self, attack_num: int, superhero: SuperHero, villain: Villain) -> None:         
        Life.inc_hero_life(superhero.life)
        Life.inc_villain_life(villain.life)
        
        print(
            f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villain.name}."
        )

        Life.dec_hero_life(villain.attack_power)
        Life.dec_villain_life(superhero.attack_power)

    print('='*58)
    def win_or_lose(self) -> Game: # have to import annotations
        #helper messages
        
        if Life.hero_life>=Life.villain_life:
            self.state = GameState.WIN
            print (WIN_MSG)
        else:
            self.state = GameState.LOST
            print(LOST_MSG)
        return self

    