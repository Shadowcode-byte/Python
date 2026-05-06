'''7.	Write functions to explain mentioned concepts:
a.	Keyword argument
b.	Default argument
c.	Variable length argument
'''
def student(name, age):
    print(name, age)

student(age=20, name="Kamal")
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Kamal")
def total(*nums):
    s = 0
    for n in nums:
        s += n
    print("Sum =", s)

total(1, 2, 3, 4)