"""
Clinent side:
This module can be logically thought as a 'client' as it consumes our API 'game.py'.

"""
from game import Game, Player
def main() -> None:
    p1 = Player("John", "Snow")
    game1 = Game(p1)
    print(game1.state)
    print(game1.start())
    game1.attack()
    game1.win_or_lose()


main()