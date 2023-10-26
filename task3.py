class Delta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        area = 0.5 * self.a * self.b
        return area

    def perimeter(self):
        z = (self.a**2 + self.b**2) ** 0.5
        perimeter = self.a + self.b + z
        return perimeter


test = Delta(3, 5)

print(test.area())
print(test.perimeter())
