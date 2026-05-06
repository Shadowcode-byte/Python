#3.	Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
def print_n(n):
    if n == 0:
        return
    print_n(n-1)
    print(n, end=" ")


n = int(input("Enter n (default = 5): ") or 5)
print_n(n)