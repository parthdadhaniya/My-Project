# if we want to store element in existing list we have three methods

# 1). append() : to add single element

# syntax : list.append(element)

# add element in existing list

from secrets import choice


shopping_cart = []
for i in range (1,6):
    item = input("Enter item : ")
    shopping_cart.append(item)
print(shopping_cart)

# dynamic add element in list

shopping_cart = []

status = True
while status:
    item = input("Enter item : ")
    shopping_cart.append(item)
    choice = input("do you want to add more item Y/N : ")
    if choice == "n" or choice == "no" or choice == "N":
        status = False
print("----- Shopping Cart -----")
print(f"\n you have added {len(shopping_cart)} item in shopping cart \n")
for item in shopping_cart:
    print(item)

# insert () : to add element at specific position (index)

# syntax : list.insert(index,element)

# extend practical

list_1 = [12,23,43]
list_2 = [101,102,103]
list_1.extend(list_2)
print(list_1)

shopping_cart = ["fruits","veges","medicines"]
cart = ["apple","mangoes","banana"]
shopping_cart.extend(cart)
print(shopping_cart)

# extend () : to add more than one element in existing list

# syntax : list.extend(list2) or
         # list.extend([element1,element2,element3......])

# insert practical

shopping_cart = ["fruits","veges","medicines"]
shopping_cart.insert(1,"Milk")
print(shopping_cart)

# remove elements from list

# 1). remove () : remove specific element from the existing list

# syntax : list.remove(element)

shopping_list = ["apple","mangoes","banana", "kiwi","mangoes"]
print(shopping_list)
shopping_list.remove("mangoes")
print(shopping_list)


# 2). pop () : by default it will remove last index element

# syntax : list.pop()  or
        #  list.pop(index) <- it will remove element from specific index

shopping_list = ["apple","mangoes","banana", "kiwi","mangoes"]
print(shopping_list)
shopping_list.pop()
print(shopping_list)

# 3). clear () : it will remove all elements from the existing list (empty list)

# syntax : list.clear()

shopping_list = ["apple","mangoes","banana", "kiwi","mangoes"]
print(shopping_list)
shopping_list.clear()
print(shopping_list)


# 4). del : it will destroy list from the memory

# syntax : del.list()

shopping_list = ["apple","mangoes","banana", "kiwi","mangoes"]
print(shopping_list)
del shopping_list
print(shopping_list)

# return index position element wise

shopping_list = ["apple","mangoes","banana", "kiwi","mangoes"]
print(shopping_list.index("banana"))

# remove duplicate element from the list

# find unique element from the list

shopping_list = ["apple","mangoes","banana", "kiwi","mangoes"]
list_1 = []
for i in shopping_list:
    if item not in list_1:
        list_1.append(item)
print(list_1)

# shuffle

import random

value = random.randint(1,100)
print(value)
list_1 = [23,3,6,87,23,9]
print(list_1)

random.shuffle(list_1)
print(list_1)

# Nested list

list_1 = [12,23,34,[45,76,101,201,[4,5,6],75,1,20,9],[1001,1002,30004],707,708,709,[201,202,203]]

print(list_1[2])
print(list_1[3][2])
print(list_1[3][4][1])