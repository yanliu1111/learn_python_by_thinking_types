from typing import Any

fname, lname = ("Louis", "Zappa")
print(fname)
print(lname)

first, *rest = ["Cece", "Roko", "Chiko", "Niko"]
print(first)
print(rest)

specs = {"type": "dynamic", "optional": "static typing", "found": "everywhere"}
lang = {"name": "python", **specs}
print(lang)

# the argument is going to be of the type of Tuple, (*args: str) means the variable of args is a tuple and the data type inside the Tuple is the type of string
def unknown_friends(*args: str) -> None:
    for friend in args:
        print(friend)

unknown_friends("Cece", "Roko", "Chiko", "Niko", "Jake", "Mario")

# keyword argument

def unknown_product(**kwargs: Any) -> None:
    """Accepts and prints variable keyword argument"""
    # keyword args are always packed as dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")


unknown_product(name="pizza", price=3.99, topping="olives", extra_cheese=True)

def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)


invoice(
    "sneakers",
    "black",
    "white",
    brand="Nike",
    category="Air Jordans",
    price=899.99,
    in_stock=False,
)