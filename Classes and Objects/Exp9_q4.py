#4.Create a class to implement method Overriding.
class A:
    def show(self):
        print("This is parent")

class B(A):
    def show(self):
        print("This is child")

obj = B()
obj.show()