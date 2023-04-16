class Box:
    box_type = "Packaging Carton"
    color = "Brown"

    def __init__(self, side_a:int, side_b:int)-> None:
        self.side_a = side_a
        self.side_b = side_b
    def __str__(self) -> str:
        return f"Side A: {self.side_a}, Side B: {self.side_b}"

# we dont have to create an instance to get back the data
b1 = Box(3, 4)
print(b1)
print(b1.box_type)
print(b1.color)