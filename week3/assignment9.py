import os
import platform

### Q1    
print("Q1")         
print(platform.platform())  

### Q2
def is_right_traigle(a,b,c):
    sides = [a,b,c]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("Yes")
    else:
        print("No")

print("Q2")   
print("Sides:3,4,5", end =" ")      
is_right_traigle(3,4,5)
print("Sides:3,4,4", end =" ")    
is_right_traigle(3,4,4)  
### Q3
print("Q3") 
a = {1:10, 2:20} 
b ={3:30, 4:40} 
c = {5:50,6:60}

conc_dict = dict(a)
[conc_dict.update(d) for d in [b,c]]

print("Dicts:", a, b, c, ". Concatenated dictionary:", conc_dict)

### Q4
def is_key_exists(key, dict_):
    if key in dict_.keys():
        print("Key", key, "exists in a given dictionary.")
    else:
        print("Key", key, "doesn't exist in a given dictionary.")

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

is_key_exists(5, d)
is_key_exists(10, d)

