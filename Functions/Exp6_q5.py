#5.	Write a lambda function to find volume of cone.
import math

cone_volume = lambda r, h: (1/3) * math.pi * r*r * h

r = float(input("Enter radius (default = 3): ") or 3)
h = float(input("Enter height (default = 5): ") or 5)

print("Volume =", cone_volume(r, h))