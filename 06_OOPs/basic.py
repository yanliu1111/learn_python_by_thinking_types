#dunder in the front and dunder in the back, __init__  nameing convention by python, not special, just a convention regular function
# first argument is always self, self is a reference to the current instance of the class, and is used to access variables that belongs to the class
# creating an instance variable called first name

class Person:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
    def __repr__(self) -> str:
        """offical representation of the class"""
        return '<class "Person">'
    def __str__(self) -> str:
        """this magic method provides a string representation of an instance."""
        return f"Person: {self.first_name} {self.last_name}"
    def greet(self) -> None:
        """Method that prints a greeting message"""
        print(f"{self.first_name} says Hello 👋")

# Every instance has different memory address
p1=Person("Peter", "Parker")
p2=Person("Tony", "Stark")
# print(p1)
# print(p2)
# print (f"p1 is located at {hex(id(p1))}")
# print (f"p2 is located at {hex(id(p2))}")

# not recommended to use __repr__ and __str__ in the same class
print(p1.__str__())

#p1.greet()
#p2.greet()