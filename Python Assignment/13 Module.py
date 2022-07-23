# my module


#
import mymodule
#
# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
#
# print(mymodule.sum(num1,num2))
#
# from mymodule import mul
#
# print(mul(12,3))
import datetime

d = datetime.datetime.now()
print(d)

print(d.date())
print(d.day)
print(d.month)
print(d.year)

print(d.strftime("%A"))
print(d.strftime("%a"))
print(d.strftime("%B"))
print(d.strftime("%C"))

import platform

print(platform.system())

# r : read
# w : write
# a : append
# x : create new file

# read

f = open("myfile.txt","r")
print(f.read())
print(f.readline())
print(f.readline())

f = open("myfile.txt","r")
l1 = f.readline()
print(l1[1])
print(l1)

# create file

f = open("myfiles.txt","w")
f.write("my firt created filr by python")
f.write("Hello Users")
f.close()

f = open("myfiles.txt","w")
name = input("Enter your name : ")
subject = input("Enter your subject : ")
f.write("\nname = " + name)
f.write("\nsubject = " + subject)

# append

f = open("myfiles.txt","a")
for i in range(1,6):
    name = input("Enter your Name : ")
    f.write("\nname = " + name)
f.close()













# Task

# import datetime
# from datetime import date
#
# # datetime.datetime.now() to get
# # current date as filename.
# filename = datetime.datetime.now()
#
# # create empty file
# def create_file():
#     # Function creates an empty file
#     # %d - date, %B - month, %Y - Year
#     with open(filename.strftime("%d %B %Y") + ".txt", "w") as file:
#         file.write("")
# # Driver Code
# create_file()
# datef = datetime.datetime.now()
# status = True
# while status:
#     filename = open("20 May 2022.txt","a")
#     # first_name = input("Enter your first name : ")
#     # last_name = input("Enter your last name : ")
#     # age = int(input("Enter your age : "))
#     # v_status = input("Enter your vaccination status 1 Dose/2 Dose : ")
#     filename.write(str(datef))
#     filename.write("\n firstname = " + input("Enter your first name : "))
#     filename.write("\n lastname = " + input("Enter your last name : "))
#     filename.write("\n ages = " + str(int(input("Enter your age : "))))
#     filename.write("\nvaccination status = " + input("Enter your vaccination status 1 Dose/2 Dose : "))
#     choice = input("Do you want to add more person Y/N ? : ")
#     if choice == "N" or choice == "n" or choice == "No" or choice == "no" or choice == "NO" : status = False
#         # print("ok")










