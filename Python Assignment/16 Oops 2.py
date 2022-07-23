# __init__() method

# which is similar like constructor : by default it will invoke when object of class create

# __init__.py : if any folder contain

# __init__.py then that folder become package


class Sample:
    def __init__(self):
        print("Welcome to sample class")
    def display(self):
        print("This is display method")
obj = Sample()
obj.display()

# encapsulation : which is contain different different data member and member function in single entity.

# e.g class

# if we want to prevent current class data.

# encapsulation : access modifier or visibility modes there are 3 types of access modifier:

# 1). private : only current can access property

#       need to add prefix __(single underscore) with property name

# 2). protected : which is access by own class and child class.

#       we need to add prefix _(single underscore) with propertyb name

# 3). public : it can be access by own class and outside the class.

class product:
    def __init__(self):
        self.mobile = 5000
        self.__laptop__ = 25000 #this is private data
        # private datamember and member function can only access within class.
    def display(self):
        print("Mobile : ",self.mobile)
        print("laptop : ",self.__laptop__)
mobile = int(input("Enter mobile price : "))
laptop = int(input("Enter laptop price : "))
obj = product()
obj.display()

obj.mobile = 7000
obj.__laptop__ = 65000
obj.display()

# using of encapsualation getter and setter

class Student:
    def setName(self,name):  # setter for name
        self.name = name
    def getName(self):
        return self.name
obj = Student()
obj.setName("Parth")
print(obj.getName())

# inheritance : inheritance - parent and child relationship

# inheritance which is provide reusability and reduce our code

# there are 5 types inheritance

#            A (parent, super, base)
#           |
#            V
#            B (child, sub, derived)

# in inheritance concept always create object of derived class (child class)

class A:
    def inputData(self):
        self.num1 = int(input("Enter Number 1 : "))
        self.num2 = int(input("Enter Number 2 : "))
class B(A):
    def display(self):
        print("Num1 = ",self.num1)
        print("Num2 = ",self.num2)
class C(B):
    def display(self):
        print("Sum = ",self.num1 + self.num2)
obj = C()
obj.inputData()
obj.display()