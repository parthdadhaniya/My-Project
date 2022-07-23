# accept 5 number from users and count positive number and nagative number

from secrets import choice


p_counter = 0
n_counter = 0

for i in range (1,6):
    num = int(input("Enter a number : "))
    if num > 0:
        print("positive number")
        p_counter = p_counter + 1
    else:
        print("negative number")
        n_counter = n_counter + 1
print("Positive Number : ",p_counter)
print("Negative Number : ",n_counter)

# accept 5 student marks and check number of passing student and fail student

p_student = 0
f_student = 0

for i in range (1,6):
    num = int(input("Enter your marks : "))
    if num >= 35:
        print("You are pass")
        p_student = p_student + 1
    else:
        print("you are fail")
        f_student = f_student + 1
print("Pass student is : ",p_student)
print("Fail student is : ",f_student)

# accept 5 number from user check total even number and total odd number

e_number = 0
o_number = 0

for i in range (1,6):
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("Even Number")
        e_number = e_number + 1
    else:
        print("Odd Number")
        o_number = o_number + 1
print("Even Number is : ",e_number)
print("Odd Number is : ",o_number)

# Nested for loop

for i in range (1,6):
    for j in range (1,6):
        print("*",end=" ")
    print()

for i in range (1,6):
    for j in range (1,i+1):
        print("*",end= " ")
    print()

for i in range (1,6):
    for j in range (1,i+1):
        print(i,end= " ")
print()

for i in range (1,6):
    for j in range (1,i+1):
        print(j,end= " ")
    print()

# Nested while loop

ticket = 5
while ticket > 0:
    print("Inside the game")
    ticket = ticket - 1

status = True

while status:
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd number")
    choice = int(input("Do you want to add more number press 1 for yes and press 2 for no : "))
    if choice == 1:
        status = True
    else:
        status = False

        