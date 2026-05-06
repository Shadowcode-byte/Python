#Count total number of vowels in a given string.
s = input("Enter string (default = Hello): ") or "Hello"

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels =", count)