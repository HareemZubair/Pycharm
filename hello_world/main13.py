#   OOP

class Employee:
    name = None
    age = 0

    def __init__(self,n,a):
        self.name = n
        self.age = a

    def setname(self,n):
        self.name=n
    def getname(self):
        return self.name
    def setage(self,a):
        self.age=a
    def getage(self):
        return self.age

harry = Employee('hareem',12)
print(harry.getage())
print(harry.getname())