#4.	Write a recursive function to print Fibonacci series upto n terms.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(input("Enter terms (default = 6): ") or 6)

for i in range(n):
    print(fib(i), end=" ")