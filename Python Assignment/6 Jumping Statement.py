# while loop

# 2). while loop
        # while loop is an entry control loop


status = True
sum = 0
while status:
    num = int(input("Enter a Number: "))
    sum += num
    choice = input("Do you want to add more number Y/N ")
    if choice == "n" or choice == "no" or choice == "N":
        status = False
    print("Total sum = ",sum)


import random

computer_guess = random.randint(1, 100)
status = True
while status:
    user_guess = int(input("Enter a number: "))
    if user_guess > computer_guess:
        print("HINT: guess lower number ")
    elif user_guess < computer_guess:
        print("HINT: guess higher number ")
    else:
        print("You Win")
status = False

import random

computer_guess = random.randint(1, 100)
status = True
for i in range(1, 6):
    user_guess = int(input("guess any number: "))
    if user_guess > computer_guess:
        print("HINT: guess lower number: ")
    elif user_guess < computer_guess:
        print("HINT: guess higher number: ")
    else:
        print("you win!!!")
else:
    print("Game Over")


# jumping statement

# Breack:
# Continue:
# Pass:

# * Breack * 

for i in range (1,6):
    if i == 3:
        break
    else:
        print(i)

# * Continue *

for i in range (1,6):
    if i == 3:
        continue
    else:
        print(i)

# * Pass *

for i in range (1,6):
    if i == 3:
        pass
    else:
        print(i)

# * Collection *

# - List
# - Tuple
# - Set
# - Dictionary

# List: list is orderable, indexable, list is mutable, changeble, list is represent by [], it can contain duplicate element

# creating blank list

shopping_list = []
print(shopping_list)

shopping_list = ["fruits","veges","bread","grocery"]
print(shopping_list)

shopping_list = ["fruits","veges","bread","grocery"]
for item in shopping_list:
    print(item)

subject_marks = [45,78,98,65,6]
for marks in subject_marks:
    print(marks)
print(f"maximum marks = {max(subject_marks)}")
print(f"minimum marks = {min(subject_marks)}")
print(f"total marks = {sum(subject_marks)}")

subject_marks = [45,78,98,65,6]
subject_marks.sort()
print(subject_marks)

subject_marks.sort(reverse = True) 
print(subject_marks)


