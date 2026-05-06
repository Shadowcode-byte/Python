'1.Check whether the given number is divisible by 3 and 5 both.'
while True:
    choice = input("Do you want to enter the number manually? (yes/no): ")
    if choice == "yes":
        num = int(input("Enter a number: "))
    else:
        num = 15   # Default value
        print("Using default number:", num)

    if num % 3 == 0 and num % 5 == 0:
        print("The number is only divisible by 3 and 5. Try again.")
    elif num % 3 == 0:
        print("The number is only divisible by 3. Try again.")
    elif num % 5 == 0:
        print("The number is only divisible by 5. Try again.")
    else:
        print("The number is not divisible by 3 or 5. Try again.")

    again = input("Do you want to check another number? (yes/no): ")
    if again != "yes":
        print("Program ended.")
        break

    