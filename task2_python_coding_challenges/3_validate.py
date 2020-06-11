import re

def validate_password(password):
    if len(re.findall("[a-z]", password))  == 0:
        print("Password:", password, " doesn't contain any lower letter.")
        return False
    elif len(re.findall("[A-Z]", password))  == 0:
        print("Password:", password, "doesn't contain any upper letter.")
        return False
    elif len(re.findall("[0-9]", password))  == 0:
        print("Password:", password, "doesn't contain any number.")
        return False
    elif len(re.findall("[$#@]", password))  == 0:
        print("Password:", password, "doesn't contain [$#@].")
        return False
    elif len(password) < 6:
        print("Password:", password, "doesn't have 6 characters.")
        return False
    elif len(password) > 14:
        print("Password:", password, "has more than 14 characters.")
        return False
    else:
        print("Password is valid")
        return True
    
password = input("Please enter a password: ")
validate_password(password)
