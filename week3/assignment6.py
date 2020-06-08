import operator
import re
from password import password


### Q1
def get_sorted_list(x):
    return [a[1] for a in sorted(x.items(), key = operator.itemgetter(1))]

stud_dict = {"B_student":"B_name", "A_student":"A_name", "L_student":"L_name","W_student":"W_name", "C_student":"C_name"}

print("Q1")
print("Dictonary:", stud_dict)
print("Sorted values:", get_sorted_list(stud_dict))


### Q2

class User:
    
    strng = ""
    
    def __init__(self, strng):
        self.strng = strng
        
    def get_String(self,strng):
        self.strng = strng
    
    def print_String(self):
        print(self.strng)
        
print("Q2")       
us = User("")
us.get_String("string")
print(us.print_String())


### Q3

pattern2 ="[0-9]"
pattern3 = re.compile("[$#@]")


def validate_password(password):
    if len(re.findall("[a-z]", password))  == 0:
        print("Password:", password, " doesn't contain any lower letter.")
        return False
    elif len(re.findall("[A-Z]", password))  == 0:
        print("Password:", password, "doesn't contain  any upper letter.")
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
        return True
    
print("Q3") 
print( validate_password("pass"))         
print( validate_password("PasS"))  
print( validate_password("pasS4"))  
print( validate_password("psS#4"))  
print( validate_password("psS#4"))  
print( validate_password("psS#45555555555555555")) 
print( validate_password("psS#455")) 


### Q3      
print("Q4",end="\n\n") 

def construnct_pattern():
    
    d, sym_qnt = 1, 0
    
    for i in range(9):
        
        sym_qnt += d
        if sym_qnt ==5:
            d = -1
        for i in range(sym_qnt):
            print("*", end="")
        print("")

construnct_pattern()

        