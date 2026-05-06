#8.Write a program to find area of triangle when length of sides are given.
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2  # semi-perimeter
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron's formula
print("Area of the triangle is:", area)
