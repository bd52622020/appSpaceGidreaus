import calendar
import re


### Q1
def print_prime(limit):
   
    for num in range(1, limit+1): 
            if (num == 2) :
                print(num, end= " ");
                continue
            is_prime = True
            for i in range(2,num):
                if (num % i) == 0: 
                    is_prime = False
                    break       
            if is_prime:
                print(num, end= " ") 
print("Q1")            
print_prime(15)

### Q2
def check_leap_year(year):
    if calendar.isleap(year):
        print(year, " is a leap year.")
    else:
        print(year, " is not a leap year.")

print("\nQ2")         
check_leap_year(1990)
check_leap_year(2000)   

### Q3
def is_ISBN(id_number): 
    pattern = "\d{1}-\d{3}-\d{5}-\d{1}"
    if re.search(pattern, id_number):
        print("ISBN", id_number, "is valid.")
    else:
        print("ISBN", id_number, "is not valid.")
print("Q3")     
is_ISBN("3-598-21508-2")    
is_ISBN("3-598-215048-2") 

### Q4

def check_list(num_list):
    if num_list[0] == num_list[-1]:
        return True
    else:
        return False

print("Q4")     
print("[1,2]:", check_list([1,2]))
print("[3]:", check_list([3]))
print("[3,5,3]:", check_list([3,4,3]))     



