#1.	Scan n values in range 0-3 and print the number of times each value has occurred.
n = int(input("Enter n (default = 5): ") or 5)

lst = []
print("Enter values (0–3):")
for i in range(n):
    lst.append(int(input() or 0))

count = [0, 0, 0, 0]

for num in lst:
    if 0 <= num <= 3:
        count[num] += 1

for i in range(4):
    print(i, "occurs", count[i], "times")