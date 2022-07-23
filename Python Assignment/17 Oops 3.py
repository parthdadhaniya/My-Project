# 2).  Multi-level inheritance :

#           Calss A
#                 |
#                 V
#                 B
#                 |
#                 V
#                 C


class TATA:
    def display(self):
        print("Welcome to TATA MOTORS")
class Vehicle(TATA):
    def warranty(self):
        print("6 Years warranty")
class Car(Vehicle):
    def specification(self,color):
        print("color : ",self,color)
car = Car()
car.display()
car.specification("Black")
car.warranty()


# 3). Multi-ple inheritance:

#     A                     B
#     |                     |
#     ----------------------
#               |
#               C

class A:
    a = 10
class B:
    b = 20
class C(A,B):
    def display(self):
        print("Sum : ",self.a + self.b)

obj = C()
obj.display()


# 4). Hierarchical inheritance :

#               A
#               |
#               V
#       ----------------
#       |               |
#       B               C

class RBI:
    def rule(self):
        print("KYC is Mandotary")
class SBI(RBI):
    def display(self):
        print("Welcome to SBI")
class BOI(RBI):
    def display(self):
        print("Welcome to BOI")
sbi = SBI()
boi = BOI()


#                     Vehicle
#                        |
#       ---------------------------------
#       |                |               |
#      Car             Bike            Truck


class Vehicle:
    def _display(self):
        print("Welcome to vehicle")
    def specification(self,color,brand,wheels):
        self.color = color
        self.brand = brand
        self.wheels = wheels
class Car(Vehicle):
    def display(self):
        print("Color : ",self.color)
        print("Brand : ",self.brand)
        print("Wheels : ",self.wheels)
class Bike(Vehicle):
    def display(self):
        print("Color : ",self.color)
        print("Brand : ",self.brand)
        print("Wheels : ",self.wheels)

car = Car()
car._display()
car.specification("Blue","Tata",4)
car.display()

bike = Bike()
bike._display()
bike.specification("Black","Honda",2)
bike.display()




# polymorphism : poly means many and morphism means forms

# polymorphism is derived from greek word one named method has different forms

# there are two types of polymorphism

# 1). method overloading (python does not support)

#       one class have more than 1 same name method

# 2). method overriding :

#       parent and child both have same name property

sbi.rule()
sbi.display()

boi.rule()
boi.display()

