class Square:
    def __init__(self, x):
        self.x = x

    def area(self):
        result = self.x * self.x
        return f"square: {result}"

    def perimeter(self):
        result = self.x * 4
        return f"perimetr: {result}"


test = Square(5)


print(test.area())
print(test.perimeter())
