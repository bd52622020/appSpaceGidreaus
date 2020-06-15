
if __name__ == '__main__':
    my_dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
    
    my_list = []
    for key, value in my_dict.items():
        if value < 5000:
            my_list.append(key.upper())
            
    print(my_list)