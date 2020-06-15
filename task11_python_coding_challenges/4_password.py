import string
import random


def generate_password():
    alfabet = string.ascii_letters + string.digits + str("!@#$%^&*")
    pass_len = random.randint(8,16)
    return "".join(random.choice(alfabet) for i in range(pass_len))


if __name__ == "__main__":
    
    ans = input("Do you want generate a new password?\n")
    while(ans.lower() in ["y", "yes"]):
        print(generate_password())
        ans = input("Do you want generate a new password?\n")
    