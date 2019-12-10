import math

point1 = (5,5)
point2 = (2,1)

#Find distanct between 2 point

ans = math.sqrt(math.pow(point2[0]-point1[0],2)+math.pow(point2[1]-point1[1],2))

print("Distance between two points = {}".format(ans))
