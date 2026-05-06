#2.Create a variable to store your age and print its type using type().
age = input("Enter your age (default = 18): ")
age = int(age or 18)

print("Age =", age)
print("Type =", type(age))
