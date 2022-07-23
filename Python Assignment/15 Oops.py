# oops : object oriented programing system

# 1) class : class is a user defined data type which is contain data member and member function is single entity.

# syntax

# class <Classname>():
    # block of class

# 2) object : object is a variable of class using of object we can access properties of class.

#  we can create more than 1 object of class.

# syntax

# <objectname> = <classname>()
#
# class Student:
#     name = "Parth"
#     subject = "Python"
# class Feculty:
#     name = "Anjali"
#     subject = "Python"
# student = Student()
# print("Name = ",student.name)
# faculty = Feculty()
# print("Name = ",Feculty.name)

# difference between function and method

# function : which is declare outside the class

    #  ---> FUNCTION ARE INDEPENDENT

# print()
# input()
# len()

# method : which is declare inside the class

# method are dependent on class.

# .sort()
# .lower()
# .upper()

# self : here, self keyword represent current class properties

# class Student:
#     def student_info(self):
#         print("Welcome to 2022 batch")
# obj = Student()
# obj.student_info()

class Student:
    def setStudentname(self,name):
        self.name = name
    def display(self):
        print("student name = ",self.name)
Student = Student()
Student.setStudentname("Parth")
Student.display()
student2 = Student
student2.setStudentname("Arati")
student2.display()


class Factorial:
    def findFactorial(self,num):
        f = 1
        for i in range(1,num):
            f *= i
            return f
class Evenodd:
    def checkEvenodd(self,num):
        if num % 2 == 0:
            return "Even Number"
        else:
            return "Odd Number"
f = Factorial()
print(f.findFactorial(5))
e = Evenodd()
print(e.checkEvenodd(12))


class Car:
    def info(self,brandname,color,wheels):
        self.brandname = brandname
        self.coloe = color
        self.wheels = wheels
    def display(self):
        print("Car brandname = ",self.brandname)
        print("Car color = ",self.coloe)
        print("Car wheels = ",self.wheels)
class Bike:
    def info(self,brandname,color,wheels):
        self.brandname = brandname
        self.color = color
        self.wheels = wheels
    def display(self):
        print("Bike brandname = ",self.brandname)
        print("Bike color = ",self.color)
        print("Bike wheels = ",self.wheels)

car = Car()
car.info("Hundai","White",4)
car.display()

bike = Bike()
bike.info("Honda","Black",2)
bike.display()