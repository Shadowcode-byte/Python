#10.Write a program to swap two numbers without taking additional variable.
a = input("Enter a (default = 2): ")
b = input("Enter b (default = 5): ")

a = int(a or 2)
b = int(b or 5)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

