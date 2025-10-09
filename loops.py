# n=7
# i=1 
# while i<n:
#     print(i)
#     i=i+1



# count=5
# while count>0:
#     print(count)
#     count=count-1 
    
# Break Statments

# n=7
# i=1
# while i<n:
#     print(i)
#     i=i+1
#     if i==4:
#         break
# else:
#     print("This will be excuted the while is run successfully without any break")


# Continue Statements
# n=7
# i=1
# while i<n:
#     i=i+1
#     if i==3:
#         continue
#     print(i)
# else:
#     print("This will be excuted when the while is run successfully without the break")

# For Loop

# l=[1,2,"Ajay","pwskills"]
# for i in l:
#     print(i)

row=1
while row<=4:
    col=1
    while col<=row:
        print("*",end=" ")
        col=col+1
    print()
    row=row+1\
    

for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
