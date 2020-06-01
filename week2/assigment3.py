import re
import math
from datetime import datetime
from datetime import timedelta


### Q1
def is_palindrome(string1):
    length = len(string1)
    for i in range(math.ceil(length/2)):
        if string1[i] != string1[length-i-1]:
            return False
    return True

print("Q1")
print("123454321", is_palindrome("123454321"))
print("Hello", is_palindrome("Hello"))

### Q2
print("\nQ2")
now = datetime.now()
print("Current date and time:", now) 
print("Current year:", now.year)
print("Current month:", now.month)
print("Current week:", now.strftime("%W"))
print("Current day of week:", now.strftime("%A"))
print("Current day of the year:",  now.strftime("%j"))
print("Current day of the month:",  now.strftime("%d"))
print("Current day of the week:", now.strftime("%w"))


### Q3
print("\nQ3")
print("Now - 30 days:", now + timedelta(-30))

### Q4
print("\nQ4")

def special_match(strg, search= re.compile(r'[^A-Z0-9a-z_]').search):
    if not bool(search(strg)):
        print("match found")
    else:
        print("no found match")
        
print(special_match("Hello"))
print(special_match("Hello_world"))
print(special_match("Hello_world!"))
    
    

        

