# Regular Expression

# a regular expression is a special

# sequence of characters that helps

# you match or find other strings

# or sets of string, using a specialized

# syntax held in a pattern

# find and search in editor

# \d : search all digit from the file

# \D : except all digit

import re

data = """
        Ram is 78, Jay is 56, Komal is 55, Ravi is 24
        
        """
age = re.findall(r"\d{1,3}",data)
print(data)

names = re.findall(r"[A-Z][a-z]*",data)
print(names)

my_dict = {}
count = 0

for name in names:
    my_dict[name]=age[count]
    count += 1
print(my_dict)

data = "Python is most popular programing language"
name = input("Enter name what you want to search : ")
if re.search(name,data):
    print("Serching....")
else:
    print("Search not found")

data = "Python is most popular programing language"
name = input("Enter name what you want to search : ")
print(re.search(name,data))

data = "Python is most popular programing language"
name = input("Enter name what you want to search : ")
if re.match(name,data):
    print("Searching.....")
else:
    print("Search not found")
