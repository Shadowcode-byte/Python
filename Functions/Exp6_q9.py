#9.	Write a program to create two lists and generate a dictionary with keys from list1 and values from list2
list1 = (input("Enter keys: ") or "a b c").split()
list2 = list(map(int, (input("Enter values: ") or "1 2 3").split()))

d = dict(zip(list1, list2))

print("Dictionary =", d)