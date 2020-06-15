def is_right_traigle(a,b,c):
    sides = [a,b,c]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("Yes")
    else:
        print("No")

print("Sides:3,4,5", end =" ")      
is_right_traigle(3,4,5)
print("Sides:3,4,4", end =" ")    
is_right_traigle(3,4,4)  

