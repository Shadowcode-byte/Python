#7.Write a program to find simple interest.
print("Press Enter to use default values")

p = input("Enter principal (default = 1000): ")
r = input("Enter rate (default = 5): ")
t = input("Enter time (default = 2): ")

p = float(p or 1000)
r = float(r or 5)
t = float(t or 2)

si = (p * r * t) / 100
print("Simple Interest =", si)
