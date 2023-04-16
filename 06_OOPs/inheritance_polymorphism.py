class Animal:
    def __init__(self, name: str, age: int, num_legs:int) -> None:
        self.name = name
        self.age = age
        self.num_legs = num_legs
    def __str__(self) -> str:
        return f"Name: {self.name}"
    def talk(self) -> None:
        print(f"{self.name} cannot talk yet!")

# inheritance
class Dog(Animal):
    def __init__(self, name: str, age: int, num_legs:int, breed: str) -> None:
        # Take the commin features and pass to the parent (super) class
        super().__init__(name, age, num_legs)
        # create additional instance variables
        self.breed = breed
        self.type = "Dog"
    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"
    # polymorphism
    def talk(self) -> None:
        print(f"{self.name} says Woof!")
    def sniff(self, item:str) -> None:
        print(f"{self.name} is sniffing out {item}.")


a1 = Animal ("Rio",2, 4) 
# print(a1)
# a1.talk()
d1 = Dog("Rio", 2, 4, "German Shepherd")
# print(d1)
# d1.talk()
# d1.sniff("bone")

#-------------------------CAT-------------------------------
class Cat(Animal):
    def __init__(self, name: str, age: int, num_legs:int, breed: str) -> None:
        # Take the commin features and pass to the parent (super) class
        super().__init__(name, age, num_legs)
        # create additional instance variables
        self.breed = breed
        self.type = "Cat"
    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"
    # polymorphism
    def talk(self) -> None:
        print(f"{self.name} says I like pizza!")

c1 = Cat("Garffy", 2, 4, "Persian Cat")
# print(c1)
# c1.talk()

#-------------------------Dinosour-------------------------------
class Dino(Animal):
    def __init__(self, name: str, age: int, num_legs:int, breed: str) -> None:
        # Take the commin features and pass to the parent (super) class
        super().__init__(name, age, num_legs)
        # create additional instance variables
        self.breed = breed
        self.type = "Dino"
    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"
    # polymorphism
    def talk(self) -> None:
        print(f"{self.name} says I am a Dino!")
    def hunt(self)-> None:
        print(f"{self.name} is hunting for food.")

dino1 = Dino("BigMac", 8, 2, "T-Rex")
# print(dino1)
# dino1.talk()
# dino1.hunt()

#-------------------------Some tricky------------------------------
print (isinstance (d1, Animal))
# because class of dog is inheriting from class of animal
print (isinstance (d1, Dog))
print (isinstance (c1, Cat))