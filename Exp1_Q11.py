#11.Write a program to find sum of first n natural numbers.
n = input("Enter n (default = 10): ")
n = int(n or 10)

sum = n * (n + 1) // 2
print("Sum =", sum)
