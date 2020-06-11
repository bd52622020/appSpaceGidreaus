import re

def is_ISBN(id_number): 
    pattern = "\d{1}-\d{3}-\d{5}-\d{1}"
    if re.search(pattern, id_number):
        print("ISBN", id_number, "is valid.")
    else:
        print("ISBN", id_number, "is not valid.")
print("Q3")     
is_ISBN("3-598-21508-2")    
is_ISBN("3-598-215048-2") 