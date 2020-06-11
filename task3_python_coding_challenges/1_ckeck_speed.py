def ckeck_speed(speed):
     
    points = int((speed-70) / 5)
    if speed <= 70:
        print("Ok")
    elif points > 12:
        print("Licence suspended")
    else:
        print("Points:", points)
        
ckeck_speed(68)    
ckeck_speed(88)
ckeck_speed(136)


