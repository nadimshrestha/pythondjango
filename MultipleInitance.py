# Python example to show the working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
    print("Base")
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
class Derived(Base1, Base2):
    def __init__(self):
        #Calling constructors of Base1
        #and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printStrs(self):
        print(self.str1, self.str2)
ob = Derived()
ob.printStrs()
#Single inheritance

#multiple inheritance

#multilevel inheritance


class Base(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    def getAge(self):
        return self.age
class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
    def getAddress(self):
            return self.address
g = GrandChild("Geek1", 23 , "Noida")
print(g.getName(), g.getAge(), g.getAddress())


