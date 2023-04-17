def smart_divider(x: int, y:int) -> None:
    try:
        num = x / y
        print(num)
    except ZeroDivisionError:
        print("Can't divide by zero")
    except TypeError:
        print("Both x and y must be numbers")
    except Exception as e:
        print(f"Something went wrong: {e}")

smart_divider(10, 0)
smart_divider(10, 4)
smart_divider(10, "a")
#--------------------------------------------
def divider(x: int, y:int) -> None:
    try:
        num = x / y  
    except ZeroDivisionError:
        print("Can't divide by zero")
    except TypeError:
        print("Both x and y must be numbers")
    except Exception as e:
        print(f"Something went wrong: {e}")
    else:
        print("Else: Is executed only when try succeeds")
        print("Printing num....")
        print(num)
    finally:
        print("Finally: Is executed no matter what")

divider(10, 0)
divider(10, 4)
divider(10, "a")

#--------------------------------------------
def find_zohan(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    try:
        assert name in friends # assert is a keyword that checks if the condition is true
    except AssertionError:
        print(f"{name} not found!")
    else:
        print(f"Found {name}")
    finally:
        print("Goodbye")


find_zohan("Zohan")
find_zohan("Sara")

#--------------------------------------------
def find_zohan2(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    if name not in friends:
        raise ValueError(f"{name} not found!")
    else:
        print(f"Found {name}")


find_zohan2("Zohan")
find_zohan2("Sara")