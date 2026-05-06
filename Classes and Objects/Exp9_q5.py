#5.Create a class for operator overloading which adds two Point Objects 
#where Point has x & y values.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def show(self):
        print("(", self.x, ",", self.y, ")")

p1 = Point(10, 20)
p2 = Point(12, 15)
p3 = p1 + p2
print("P1:", end=" ")
p1.show()
print("P2:", end=" ")
p2.show()
print("P3:", end=" ")
p3.show()