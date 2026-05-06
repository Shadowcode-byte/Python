#4.Take different data types and print values using print function.
a = input("Enter integer (default = 10): ")
b = input("Enter float (default = 3.14): ")
c = input("Enter string (default = Python): ")
d = input("Enter boolean (default = True): ")

a = int(a or 10)
b = float(b or 3.14)
c = c or "Python"
d = d or "True"

print(a)
print(b)
print(c)
print(d)
