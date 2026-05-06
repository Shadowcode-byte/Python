'4.Find the greatest among three numbers assuming no two values are same. '
choice = input("Do you want to enter numbers manually? (yes/no): ")

if choice == "yes":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
else:
    num1 = 10
    num2 = 25
    num3 = 15
    print("Using default numbers:", num1, num2, num3)

if num1 > num2 and num1 > num3:
    print("The greatest number is:", num1)

elif num2 > num1 and num2 > num3:
    print("The greatest number is:", num2)

else:
    print("The greatest number is:", num3)

    