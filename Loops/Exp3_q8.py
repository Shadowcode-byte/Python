#8.	Convert all lower cases to upper case in a string.
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch >= 'a' and ch <= 'z':
        result = result + chr(ord(ch) - 32)
    else:
        result = result + ch

print("Uppercase string:", result)