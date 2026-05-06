#Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem. 
print("Do you want to enter your own values?")
print("If YES: enter values")
print("If NO: just press Enter")

a = input("Enter base (default = 2): ")
b = input("Enter height (default = 4): ")

a = float(a or 2)
b = float(b or 4)

c = (a**2 + b**2) ** 0.5
print("Length of hypotenuse =", c)

