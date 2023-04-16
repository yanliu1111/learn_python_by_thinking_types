"""
Higher Order Functions:
"""
from typing import Callable


def hello() -> None:
    print("Hello")

hello2 = lambda:"Hello world";


# print (hello)
# print (type(hello))
# print (id(hello))

greet: Callable[[], None] = hello
#greet()

def zola(name: str) -> str:
    return f"Hello, {name}!"
zola2 = lambda name: f"Hello, {name}!"

def good_morning(name: str) -> str:
    return f"Good morning, {name}!"
def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

def universal_greeter(name: str, greeter: Callable[[str], str]) -> None:
    msg: str = greeter(name)
    print(msg)

universal_greeter("Cece", zola)
universal_greeter("Roko", good_morning)
universal_greeter("Chiko", goodbye)


"""
Functions returning functions!!
"""
def add_by_5(num: int) -> Callable[[], int]:
    def by_5() -> int:
        return num + 5
    return by_5
sum = add_by_5(5)
#print(sum())

'''
lambda functions
'''
add: Callable[[int,int], int] = lambda x, y: x + y
substract: Callable[[int,int], int] = lambda x, y: x - y
multiply: Callable[[int,int], int] = lambda x, y: x * y

def calc(num1: int, num2: int, operation: Callable[[int,int], int]) -> int:
    return operation(num1, num2)
print(calc(5, 4, add))
print(calc(5, 4, substract))
print(calc(5, 4, multiply))