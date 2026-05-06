'Find the greatest among the two numbers. If numbers are equal than print “numbers are equal."'
print("1. Compare two numbers")
choice = input("Enter 1 to continue: ")

if choice == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2:
        print("The greatest number is:", num1)
    elif num2 > num1:
        print("The greatest number is:", num2)
    else:
        print("Numbers are equal")
else:
    print("Invalid input. Try again.")

