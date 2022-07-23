# set

# set : set is a collection data type which is contain unique values, which is represent by {} - set is unorderable, unindexable, immutable

s = {12,34,7,1,7,12,5}
print(s)

# remove duplicate element from the list

list1 = [12,56,87,9,45,3,12,3]
s = set(list1) # type casting list into set
list1 = list(s) # type casting list
print(list1)

list1 = [12,56,87,9,45,3,12,3]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


# dictionary : dictionary is a collection data type

# dictionary contain key and value in pair

# key are always unique in dictionary 

# dictionary always represent by {}

student = {
    "name" : "Parth",
    "subject" : "pythone",
    "marks" : 90,
}
print(student)

student = {
    "name" : "Parth",
    "subject" : "python",
    "marks" : 90,
}
# print(student["name"])
# print(student["subject"])

student = {
    "name" : "Parth",
    "subject" : "pythone",
    "marks" : 90,
}
for i in student.keys():
    print(i)
for j in student.values():
    print(j)

student = {
    "name" : "Parth",
    "subject" : "python",
    "marks" : 90,
}
for i,j in student.items():
    print(f"{i} = {j}")

student = {
    "name" : "Parth",
    "subject" : "pythone",
    "marks" : 90,
    "parth" : {
        "web" : "python",
        "mobile" : "android",
        "cross" : "flutter",
    }
}

quiz = {
    1 : {
        "que" : "Who is prime minister of india ?",
        "ans" : "Narendra Modi",
    },
    2 : {
        "que" : "Most popular language ?",
        "and" : "python"
    }
}
for i in range(1,3):
    print(quiz[i]["que"])
    ans = input("\nEnter your ans : ")
    if ans == quiz[i]["ans"]:
        print("Right answer !!!")
    else:
        print("Wrong answer !!!")

# Task

# JAY BHAVANI

    # MENU :
    # Vadapav 30
    # Bhel 70
    # Dabeli 30

# Enter product do you want : vadapav

# number of qty : 4

# Total cost : 4 * 30 = 120

# do you want to purchase more item : Y/N
