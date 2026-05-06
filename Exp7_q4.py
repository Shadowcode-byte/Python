#4.	 Input two values from user where the first line contains N, the number of test cases. 
# The next N lines contain the space separated values of a and b. 
# Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError. 

n = int(input("Enter number of test cases (default = 3): ") or 3)

for i in range(n):
    try:
        a, b = input("Enter a and b: ").split()
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)