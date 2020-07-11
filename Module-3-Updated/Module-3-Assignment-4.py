# Write a program to find distancebetween two locations when
# their latitude and longitudes are given.

#ANSWER
import math
R = 6373.0 #radius of the Earth
lat1 = math.radians(52.2296756) #coordinates
lat2 = math.radians(52.406374)

lon1 = math.radians(21.0122287)
lon2 = math.radians(16.9251681)

dlon = lon2 - lon1 #change in coordinates
dlat = lat2 - lat1
a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2 #Haversine formula
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = R * c

print("Distance is ", distance)