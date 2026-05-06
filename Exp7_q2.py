'''2.	Store integers in a file.
a.	Find the max number
b.	Find average of all numbers
c.	Count number of numbers greater than 100
'''
with open("num.txt", "w") as f:
    f.write("10 200 30 150 80")

with open("num.txt", "r") as f:
    nums = list(map(int, f.read().split()))

# a) Max
print("Max =", max(nums))

# b) Average
print("Average =", sum(nums)/len(nums))

# c) Count > 100
count = 0
for n in nums:
    if n > 100:
        count += 1

print("Numbers > 100 =", count)