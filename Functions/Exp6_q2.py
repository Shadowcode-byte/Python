#2.	Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than 
# the specified number. 
def sum_cubes(n):
    total = 0
    for i in range(1, n):
        total += i**3
    return total


n = int(input("Enter n (default = 5): ") or 5)
print("Sum =", sum_cubes(n))