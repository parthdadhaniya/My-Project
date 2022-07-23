# -----> exception handling

# exception : which disturb the normal flow of the program

# to handle exception we need to user try and except block

# syntax

# try:
    # block
# except:
    # error message

# print(a)

# Traceback (most recent call last):
#   File "C:\Users\PARTH\Desktop\Python Training\Lecture 14.py", line 14, in <module>
#     print(a)
# NameError: name 'a' is not defined

# try:
#     print(a)
# except:
#     print("Something went wrong")

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
try:
    ans = num1 / num2
    print(ans)
except:
    print("Cannot be devide by zero")

try:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    ans = num1 / num2
    print(ans)
except ValueError:
    print("Invalid input - need to enter numbers only")
except ZeroDivisionError:
    print("Cannot be devide by zero")

import sys

try:
    print(a)
except:
    print("Erro type",sys.exc_info()[0])
    print("Erro type",sys.exc_info()[1])

try:
    print(a)
except Exception as a:
    print("Message",e)
