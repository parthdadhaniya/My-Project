# kalyan jewellers :

# Firstname
# lastname

# purchase amount : 
# gender :
# age :
# Vaccination status : 

# making charges :

# > 1 lakh   > 2 lakh   > 3 lakh
    # 15%        25%        35%

# senior citizen female

# > 1 lakh   > 2 lakh   > 3 lakh
    # 20%        30%        40%

# citizen male

# > 1 lakh   > 2 lakh   > 3 lakh
    # 10%        20%        30%

# citizen female

# > 1 lakh   > 2 lakh   > 3 lakh
    # 15%        25%        35%

from functools import partialmethod


marks = int(input("Enter marks : "))
if marks >0 and marks <= 100: 
    if marks  >= 70:
        print("A grade")
    elif marks >= 60 and marks < 70:
        print("B grade")
    elif marks >= 50 and marks < 60:
        print("C grade")
    elif marks >= 40 and marks < 30:
        print("D grade")
    else:
        print("Fail")
else:
    print("Invalid input")

# looping statement

# 1). for loop :
        # for loop is sequence control loop
    # syntax
        # for var in sequence:
        # statement
    # range () : by default it will start from 0 and ending number
for i in range(6):
    print(i)

for i in range(1,6):
    print(i)    

# display 5 item hello

print("hello"*5)

for i in range (1,6):
    print(i,"hello")

for i in range (1,11,2):
    print(i,"hello")

firstname = "parth"
subject = "python"

# hello Parth your subject is python

print("Hello","your subject is",subject)
print(f"Hello {firstname} your subject is {subject} ")

for i in range (1,6):
    print(f"( {i} ) Hello")

# accept 5 numbers from user

for i in range(1,6):
    num=(input("Enter a number : "))


