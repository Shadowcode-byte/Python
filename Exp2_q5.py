'5.Check whether the quadratic equation has real roots or imaginary roots. Display the roots.'
while True:
    choice = input("Do you want to enter values manually? (yes/no): ")
    if choice == "yes":
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))
    else:
        a = 1
        b = -3
        c = 2
        print("Using default values: a=1, b=-3, c=2")

    if a == 0:
        print("Invalid input! 'a' cannot be 0 in a quadratic equation.")
        print("Try again.\n")
    else:
        D = b*b - 4*a*c
        print("Discriminant =", D)
        if D > 0:
            root1 = (-b + D**0.5) / (2*a)
            root2 = (-b - D**0.5) / (2*a)
            print("Roots are Real and Different")
            print("Root 1 =", root1)
            print("Root 2 =", root2)

        elif D == 0:
            root = -b / (2*a)
            print("Roots are Real and Equal")
            print("Root =", root)

        else:
            print("Roots are Imaginary")
        break