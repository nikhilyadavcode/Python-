def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def pow(num1,num2):
    return num1**num2

def greet(name):
    print("Hi",name)

def check_even_or_odd(numbers):
    for num in numbers:
        if num % 2==0:
            print(num,"is even")
        else:
            print(num,"is odd")

def check_if_even_odd(number_list):
    try:
        for i in range(0,len(number_list)):
            if i % 2==0:
                print(i,"This is an even number")

            else:
                print(i,"This is an odd number")
    except Exception as e:
        print(f"This is an error {str(e)}")


number_list=[1,2,3,4,5,6,7,8,9,10]
result=check_if_even_odd(number_list)
print(result)

def check_guess(secret,user_input):
    if user_input==secret:
        return "Correct!"
    else:
        return "Wrong"


