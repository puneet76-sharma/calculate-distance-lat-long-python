# pip install geopy

from geopy.distance import geodesic

origin_loc = eval(input("enter the origin location lat,long: "))
destination_loc = eval(input("enter the destination location lat,long: "))

distance= geodesic(origin_loc, destination_loc).kilometers

print(distance, "km")

input()