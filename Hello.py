# print("Hello World")

# print("Welcome to python Programming")

# print("Hello I am Nikhil yadav")
# print("I am learning python")


# name="Ajay"
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])\


# Nested if else

x=1
y=6
if x>5:
    if y>5:
        print("x is greater than 5 and y is greater than 5")
    else:
        print("x is greater than 5 and y is less than 5");
else:
    print("x is not greater than 5")


is_vip=False
age=15
if is_vip:
    if age>=18:
        if age<65:
            print("Welcome to vip customer")
        else:
            print("You are vip and very important.You are eligible for senior citizen")
    else:
        print("Vip status is only for adult")
else:
    print("You are not vip customer and will be chrged a regular price")