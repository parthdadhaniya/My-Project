# input() : to accept values from user

# by default input() accept value in string format

# we can pass prompt mesage in input function

# type conversion : to convert one data type value in anothe data type

num1 = "45"
print(type(num1))
num2 = int(num1)
print(type(num2))

num3 = 45
num4 = str(num3)
print(type(num4))

num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))

print(num1 + num2)

# operator : if we want to perform some operation at that time we are using some specific symbol that symbol we called operator

# e.g a + b here, + is an operator

# a and b both are oprands

# type of operator :

    # 1). arithmetic operator: 
        
        # + - * / % ** //

num1 = int(input("Enter number 1 : "))
bun2 = int(input("Enter number 2 : "))

ans = num1 / num2
print(ans)
ans = num1 % num2
print(ans)

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

ans = num1**num2
print(ans) 

num1 = 36
num2 = 3
print(num1 / num2)
print(num1 // num2)

    # 2). assignment operator :
        
        # = num1 = 45

    # 3). relational operator : 

        # >, <, >=, <=, ==, !=

    # 4). membership operators

        # in
        # not in

    # 5). indentity operator

        # is
        # is not

# control statement : 

# 1). conditional statement

    # if
    # if..else
    # elif
    # nested if

age = int(input("Enter your age : "))
if age >= 18:
    print("you are eligible")
else:
    print("you are below 18")

num = int(input("Enter number : "))
if num > 0:
    print("Positive number")
else:
    print("nagetive number")

num = int(input("enter number"))
if num%2 == 0:
    print("Even number")
else:
    print("Odd number")

day = int(input("Enter day"))
if day == 1:
    print("Monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saterday")
elif day == 7:
    print("sunday")
else:
    print("invalid input")

# 2). looping statement 

    # for loop
    # while loop

# 3). jumping statement

    # break
    # continue
    # pass


