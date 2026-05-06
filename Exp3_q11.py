#11.	Write a program to print the sum of the following series
#1+ ½ + 1/3 + ¼ +….+1/n


n = int(input("Enter value of n: "))
sum = 0

for i in range(1, n+1):
    sum = sum + 1/i

print("Sum of series =", sum)  