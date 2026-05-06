'''7.	Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a)	Fruits which are in both sets s1 and s2
b)	Fruits only in s1 but not in s2
c)	Count of all fruits from s1 and s2
'''
n = int(input("Enter number of fruits (default = 3): ") or 3)

print("Enter fruits for set 1:")
s1 = set()
for i in range(n):
    s1.add(input() or "apple")

print("Enter fruits for set 2:")
s2 = set()
for i in range(n):
    s2.add(input() or "banana")

# a) Common fruits
print("Common fruits:", s1 & s2)

# b) Only in s1
print("Only in s1:", s1 - s2)

# c) Total count
print("Total fruits:", len(s1 | s2))