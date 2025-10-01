def validate_name(name):
    if name.strip()=="":
        print("Please enter a valid name,it cannot be empty")
        return False
    return True

def validate_email(email):
    if "@" not in email or "." not in email:
        print("Please enter a valid email")
        return False
    return True

def validate_password(password):
    if len(password)==0:
        print("No password entered,please provide a valid password")
        return False
    return True

def registration_form():
    name=input("Please enter your name:")
    email=input("Please enter your email:")
    password=input("Please eneter your password:")


    if not validate_name(name):
        return
    if not validate_email(email):
        return
    if not validate_password(password):
        return
    
    print("Login/Registration is successful!")


registration_form()