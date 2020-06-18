
if __name__ == '__main__':
    
    latitude1 = int(input("Please give first point latitude :"))
    longitude1 = int(input("Please give first point longitude :"))
    latitude2 = int(input("Please give second point latitude :"))
    longitude2 = int(input("Please give second point longitude :"))
    
    print("Latitude distance:", abs(latitude1 -latitude2) )
    print("Longitude distance:", abs(longitude1 - longitude2) )