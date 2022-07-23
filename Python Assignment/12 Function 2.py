# function: block
# of
# code
#
# -> syntax:
#
# function
# defination

#
# def funname():
#     statement
#
#
# function
# calling
#
# funname()
#
# == == == == == == == == == == == == == == == == == == == == =
# function
# categories:
#
# 1) function
# without
# parameters and function
# without
# return type:
#
# syntax:


# def funname():
#     statement
#
#
# 2) function
# with parameter and function without
# return type:
#
# syntax:
#
#
# def funname(parameter):
#     statement
#
#
# 3) function
# without
# parameter and function
# with
#     return type

# syntax:
#
#
# def funname():
#     return statement
#
#
# 4) function
# with parameter and function with
# return type:
#
# syntax:
#
#
# def funname(parameter):
#     return statement
#
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

def menu():
    data = """
                            MENU 

                press 1 for factorial number 
                press 2 for even and odd number 

            """

    print(data)

    choice = int(input("Enter your choice : "))
    if choice == 1:
        num = int(input("Enter a number : "))
        print(factorial(num))
    elif choice == 2:
        num = int(input("Enter a number : "))
        print(checkEvenOdd(num))
    else:
        print("invalid input")


def factorial(number):
    # 5  : 5*4*3*2*1
    f = 1
    for i in range(1, number + 1):
        f *= i

    return f


def checkEvenOdd(number):
    if number % 2 == 0:
        return "even number"
    else:
        return "odd number"


menu()

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

# lambda function: function
# with out any name
#
# lambda function can
# contain
# multiple
# parameters
# but
# return only
# single
# statement
#
# syntax:
#
# lambda: statement

# lambda function
x = lambda a: a + a  # here, x is a variable , a parameter after :  a + a is expression or statement

print(x(10))


# normal function
def sum(num):
    ans = num + num
    return ans


print(sum(10))
#
# == == == == == == == == == == == == == == == == == == == == == == == == == =
# *args and ** kwargs
#
# args: arguments or tuple as a
# parameter
# kwargs: key
# with arguments or dictionary as a parameter
#
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

# normal parameterize function
def sum(num1, num2):
    ans = num1 + num2
    print(ans)


sum(1, 3)


# args : with arguments
def addition(*num):
    sum = 0
    for i in num:
        sum += i
    print(sum)


addition(12, 23, 5, 7, 3, 8, 2)
# -------------------------------------------------------------------
# dictionary as a
# parameter:
#

# dictionary as a parameter

def student(**d):
    for k, v in d.items():
        print(f"{k} = {v}")


student(name="AAAA", subject="Python", marks=78)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# module : collection of logics or function

# there are lots of modules available in python

import random

num = random.randint(1, 100)
print(num)
# == == == == == == == == == == == == == == == == == == == ==
# module : collection of logics or function

# there are lots of modules available in python

import math

print(math.pi)
print(math.factorial(5))
print(math.ceil(5.4))
print(math.floor(5.4))
print(math.cos(4.8))
print(math.pow(2, 3))  # 2*2*2

# == == == == == == == == == == == == == == == == == == ==
from math import factorial, pow

print(factorial(6))

from math import *  # it will import all functions from the math module

print(pi)




















