class Box:
    def __init__(self, side_a: int, side_b:int) -> None:
        self.side_a = side_a
        self.side_b = side_b
    
    @property
    def area(self) -> int:
        return self.side_a * self.side_b

    def __repr__(self) -> str:
        return "<class 'Box'>"
    
    def __str__(self) -> str:
        return f"Box({self.side_a}, {self.side_b})"
    
    def __contains__(self, num: object) -> bool:
        if not isinstance(num, int):
            raise NotImplementedError # not binary operator
        return num in [self.side_a, self.side_b]
    
    def __eq__(self, box: object) -> bool:
        if not isinstance(box, Box):
            raise NotImplemented # IT IS binary operator, binary operator includes +, -, *, /, //, %, **, <, >, <=, >=, ==, !=, &, |, ^, >>, <<, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=, @=, ->, in, not in, is, is not, and, or, not
        return self.side_a == box.side_a and self.side_b == box.side_b
    
    def __lt__(self, box: object) -> bool:
        if not isinstance(box, Box):
            raise NotImplemented
        return self.area < box.area
    def __le__(self, box: object) -> bool:
        if not isinstance(box, Box):
            raise NotImplemented
        return self.area <= box.area
# we dont have to create greater and greater equal methods, because they are already defined in python behind after less than and less equal methods created

# floor divison always returns float, float to int conversion using //
    def __truediv__(self, box: object) -> float:
        if not isinstance(box, Box):
            raise NotImplemented
        return self.area / box.area
    def __floordiv__(self, box: object) -> int:
        if not isinstance(box, Box):
            raise NotImplemented
        return self.area // box.area

b1 = Box(3, 4)
b2 = Box(2, 5)

# print(b1)
# print(b2)

# print(b1 == b2)
# print(4 in b1)
# print(4 in b2)
# print("a" in b1)

# print (b1 < b2)
# print (b1 > b2)
# print (b1 <= b2)
# print (b1 >= b2)

print (b1 / b2)
print (b1 // b2)