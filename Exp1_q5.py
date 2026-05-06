#5.Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, perform addition, multiplication, division and subtraction on these two variables and Print out the result.
x = input("Enter x (default = 9): ")
y = input("Enter y (default = 7): ")

x = int(x or 9)
y = int(y or 7)

z = x + y
print("Addition =", z)

z = x * y
print("Multiplication =", z)

z = x / y
print("Division =", z)

z = x - y
print("Subtraction =", z)
