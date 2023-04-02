from typing import Final

MAX_FLYING_WEIGHT: Final[float] = 15

def calc_weight( weight: float) -> float:
    return (weight + 32) / 8

def can_fly(weight: float) -> bool:
    return weight <= MAX_FLYING_WEIGHT

def flying_friends(friends: dict[str, float]) -> None:
    for name, earth_weight in friends.items():
        zortan_weight = calc_weight(earth_weight)
        if can_fly(zortan_weight):
            print(f"{name}: {zortan_weight} kgs can fly on Zortan!")
        else:
            print(f"{name}: {zortan_weight} kgs can only walk on Zortan.")

def main():
    friends: dict[str, float] = {
        "Cece": 54,
        "Roko": 88,
        "Chiko": 50,
        "Niko": 102,
        "Ziko": 90,
    }
    flying_friends(friends)

main()