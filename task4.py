class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, a, b):
        return b - a

    def distance2(self):
        return self.distance(self.x, self.y)

    def perimetr(self, a, b, c):
        a = self.distance2(self.a)
        b = self.distance2(self.b)
        c = self.distance2(self.c)
        res = a + b + c
        return res


a = Point(2, 4)
b = Point(6, 9)
c = Point(6, 0)
print(a.distance2() + b.distance2() + c.distance2())
