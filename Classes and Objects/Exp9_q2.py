"""2. Add constructor in the above class to initialize student details of n students and implement following methods:
a)	Display() student details
b)	Find Marks_percentage() of each student
c)	 Display result() [Note: if marks in each subject >40% than Pass else Fail]
d)	Write a Function to find average of the class.
"""
class Student:
    def __init__(self, n, s, p, c, m):
        self.name = n
        self.sap = s
        self.phy = p
        self.chem = c
        self.maths = m
    def display(self):
        print(self.name, self.sap, self.phy, self.chem, self.maths)
    def per(self):
        return (self.phy + self.chem + self.maths) / 3
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            print("Pass")
        else:
            print("Fail")

n = int(input("Enter number of students: "))
lst = []
for i in range(n):
    print("Enter data")
    name = input("Name: ")
    sap = input("SAP: ")
    phy = int(input("Phy: "))
    chem = int(input("Chem: "))
    maths = int(input("Maths: "))
    obj = Student(name, sap, phy, chem, maths)
    lst.append(obj)
# display
total = 0
for i in lst:
    i.display()
    p = i.per()
    print("Percentage:", p)
    i.result()
    total = total + p
    print()
print("Class average =", total/n)