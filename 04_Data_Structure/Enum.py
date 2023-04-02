from enum import Enum, auto


class PizzaSize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12

choice = PizzaSize.MEDIUM
print(f"One order for {choice.value} inch pizza")

class Colors(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
print(f"One order for {Colors.GREEN.value} T-Shirt")

class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()

print(Role.MANAGER.value)