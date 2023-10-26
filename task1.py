class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")

    def distance(self, a, b):
        return b - a

    def distance2(self):
        return f"Расстояние от x до y: {self.distance(self.x, self.y)}."


first = Point3D(4, 5, 8)
second = Point3D(5, 7, 8)
thrid = Point3D(8, 7, 3)

first.info()
print(first.distance2())
