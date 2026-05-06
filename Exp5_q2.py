#2.	Create a tuple to store n numeric values and find average of all values.
n = int(input("Enter n (default = 4): ") or 4)

lst = []
for i in range(n):
    lst.append(int(input("Enter number: ") or 10))

t = tuple(lst)

avg = sum(t) / len(t)

print("Tuple:", t)
print("Average =", avg)