from __future__ import annotations # for type hinting
# why have to in the beginning of the file?  https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
from enum import Enum, auto
from datetime import datetime
from typing import final # means no one can inherit from this class
class Role (Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()

class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname
        

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    # decrator, same as add instance fullname in __init__
    @property
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"
@final # means no one can inherit from this class
class Staff(Person):
    def __init__(self, fname: str, lname: str, staff_id: int, role: Role) -> None:
        super().__init__(fname, lname)
        self.staff_id = staff_id
        self.is_staff = True
        self.role = role
        self.__date_joined = datetime.now() # private variable
        # dynamic create & assign instance variable
        match role:
            case Role.ASSOCIATE:
                self.__salary: float = 15
            case Role.SUPERVISOR:
                self.__salary: float = 20
            case Role.MANAGER:
                self.__salary: float = 25
    def __str__(self) -> str:
        return f"{super().__str__()}, Staff ID: {self.staff_id}, Role: {self.role.name}, Salary: {self.__salary}"
    @classmethod # the purpose is to create a new instance of the class
    def new(cls, person: Person, staff_id: int, role: Role) -> Staff:
        # it takes 'class' as the first argument, and return a new instance of the class
        # replace Staff with cls
        return cls(person.fname, person.lname, staff_id, role)
    @property # want to see private variable, getter method, the concept is called getters and setters
    def date_joined(self) -> datetime:
        return self.__date_joined.strftime("%B %d, %Y")
    @staticmethod
    def is_manager(role: Role) -> bool:
        return role == Role.MANAGER
  
    # setter method
    @property
    def salary(self) -> float:
        return self.__salary
    @salary.setter
    def salary(self, amt: float) -> None:
        """`SETTER` sets salary after validation."""
        if self.role == Role.ASSOCIATE and amt < 15:
            print("Error! Associate cannot have salary less than $15/hr")
        elif self.role == Role.SUPERVISOR and amt < 20:
            print("Error! Supervisor cannot have salary less than $20/hr")
        elif self.role == Role.MANAGER and amt < 25:
            print("Error! Manager cannot have salary less than $25/hr")
        else:
            self.__salary = amt
            print(f"{self.fullname} now has a salary of ${self.salary}/hr")

p1 = Person ('Samwell', 'Tarly')
# print(p1)
# print(p1.fullname)
s1 = Staff.new(p1, 1234, Role.ASSOCIATE)
# print(s1)
# print(s1.date_joined.strftime("%B %d, %Y"))
# print(s1.salary)

print("is_manager", Staff.is_manager(Role.ASSOCIATE))

s1.salary = 17

s2 = Staff('John', 'Snow', 1123, Role.MANAGER)
print(s2)

# ------------------FINALCLASS------------------
class HR(Staff):
    pass