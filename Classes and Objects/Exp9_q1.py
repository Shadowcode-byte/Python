"""1.Create a class of student (name, sap id, marks[phy,chem,maths] ). 
Create 3 objects by taking inputs from the user and display details of all students.
"""
class Student:
    def get(self):
        self.name = input("Enter name: ")
        self.sap = input("Enter sap id: ")
        self.phy = int(input("Enter phy: "))
        self.chem = int(input("Enter chem: "))
        self.maths = int(input("Enter maths: "))
    def show(self):
        print("Name:", self.name)
        print("SAP:", self.sap)
        print("Marks:", self.phy, self.chem, self.maths)
        print()
# making 3 objects
s1 = Student()
s2 = Student()
s3 = Student()
print("Student 1")
s1.get()
print("Student 2")
s2.get()
print("Student 3")
s3.get()
print("\nDetails:")
s1.show()
s2.show()
s3.show()