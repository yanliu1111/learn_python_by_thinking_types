"""
Clinent side:
This module can be logically thought as a 'client' as it consumes our API 'game.py'.

"""
from game import Game, Player
def main() -> None:
    p1 = Player("John", "Snow")
    game1 = Game(p1)
    print(game1.start())
    print(game1.state)
    game1 = game1.attack().win_or_lose()
    print(game1.state)
    

main()