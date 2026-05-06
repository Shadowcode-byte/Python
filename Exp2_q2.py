'2.Check whether a given number is multiple of five or not.'
print("1. Check a single number")
print("2. Detailed analysis in a range")

option = int(input("Enter your choice (1 or 2): "))

if option == 1:
    num = int(input("Enter a number: "))

    if num % 5 == 0:
        print("The number is a multiple of 5.")
    else:
        print("The number is NOT a multiple of 5.")

elif option == 2:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    print("Multiples of 5 in the given range are:")

    num = start
    while num <= end:
        if num % 5 == 0:
            print(num)
        num = num + 1

else:
    print("Invalid choice.")


    