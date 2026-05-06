#5.	Given a string containing both upper and lower case alphabets.
#  Write a Python program to count the number of occurrences of each alphabet and display the same.
s = input("Enter string (default = ABaBCbGc): ") or "ABaBCbGc"

s = s.upper()
visited = ""

for ch in s:
    if ch not in visited:
        count = 0
        for c in s:
            if c == ch:
                count += 1
        print(count, ch)
        visited += ch