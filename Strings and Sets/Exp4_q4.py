#4.	WAP to enter a string and a substring. 
# String traversal will take place from left to right, not from right to left.
s = input("Enter string (default = ABCDCDC): ") or "ABCDCDC"
sub = input("Enter substring (default = CDC): ") or "CDC"

count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count += 1

print(count)