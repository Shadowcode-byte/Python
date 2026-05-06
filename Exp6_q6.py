#6.	Write a lambda function which gives tuple of max and min from a list.
lst = list(map(int, (input("Enter list: ") or "10 6 8 90 12 56").split()))

result = (lambda x: (max(x), min(x)))(lst)

print(result)