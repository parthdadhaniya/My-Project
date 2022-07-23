# Function: function is a
# block
# of
# code
# that
# code
# are
# used
# to
# again and again.
#
# syntax:
#
# there
# 3
# steps
# to
# implement
# function
#
# but in python
# there is 2
# steps
# for function implementation
#     -------------------------------------------------------
# 1) function
# defination:
#
# syntax:

# def <funname > ():
#
#
# block
# of
# code
# block
# of
# code
# .
# .
#
# 2) function
# calling:
#
# syntax: < funname > ()
#
#           == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =


def menu():
    data = """
                        MENU 
                press 1 for addition 
                press 2 for multiplication 
                press 3 for division

            """
    print(data)

    choice = int(input("Enter your choice : "))
    if choice == 1:
        addition()
    elif choice == 2:
        mul()
    elif choice == 3:
        pass


def addition():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    ans = num1 + num2
    print(ans)


def mul():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    ans = num1 * num2
    print(ans)
menu()

# == == == == == == == == == == == == == == == == == == == == == == == == == =
# function
# with parameter:
#
# syntax:
#
#
# def <funname > (parameter1, parameter2):

#
# block
# of
# code
#
# calling
# syntax:
#
# < funname > (parameter1, parameter2)
# == == == == == == == == == == == == == == == == == == == == == == == == =

def greetings(msg):
    print("msg : ", msg)


message = input("Enter your greeting message : ")
greetings(message)

# == == == == == == == == == == == == == == == == == == == == == == == == =

def menu(Appname):
    print(Appname)
    data = """
                        MENU 
                press 1 for addition 
                press 2 for multiplication 
                press 3 for division

            """
    print(data)
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    choice = int(input("Enter your choice : "))
    if choice == 1:
        addition(num1, num2)
    elif choice == 2:
        mul(num1, num2)
    elif choice == 3:
        pass


def addition(num1, num2):
    ans = num1 + num2
    print(ans)


def mul(num1, num2):
    ans = num1 * num2
    print(ans)


menu("CAL C - 2022")

# TASK: KB
# 5
# star
#
# 1) Question
#
# A)
# B)
# C)
# D)
# -> right
# answer + 50
# -> wrong
# answer - 20
#
# HINT: Function, if ..else or nested if, loop -
# while - for loop
# list or dictionary

# ----------------------
















