#3. Create programs to implement different types of inheritances.
#Single Level:
class A:
    def show(self):
        print("Parent class")
class B(A):
    def display(self):
        print("Child class")
x = B()
x.show()
x.display()

#Multilevel
class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(B):
    def c(self):
        print("C")
o = C()
o.a()
o.b()
o.c()