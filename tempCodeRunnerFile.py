class Base1(object):
    def __init__(self):
        print("Base 1 Class")
class Base2(object):
    def __init__(self):
        print("Base2 Class")
class Derived(Base1, Base2):
        pass
D = Derived()
        
        