from math import sin, cos, sqrt, atan2, radians

if __name__ == '__main__':
    R = 6373.0

    lat1 = int(input("Please give first point latitude :"))
    lon1 = int(input("Please give first point longitude :"))
    lat2 = int(input("Please give second point latitude :"))
    lon2 = int(input("Please give second point longitude :"))
	
    dlon = latitude2 - latitude1
    dlat = longitude2 - longitude1    

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    print("Distance:", distance)

