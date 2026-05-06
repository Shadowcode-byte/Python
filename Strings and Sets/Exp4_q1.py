#Write a program to count and display the number of capital letters in a given string.
s = input("Enter string (default = HelloWorld): ") or "HelloWorld"

count = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        count += 1

print("Capital letters =", count)