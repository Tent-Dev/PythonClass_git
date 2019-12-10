# Find the area of triangle from 3 positions (use tuple in list)

p1x, p1y = input("Point 1 (x,y) : ").split(" ")
p2x, p2y = input("Point 2 (x,y) : ").split(" ")
p3x, p3y = input("Point 3 (x,y) : ").split(" ")

Point1 = (int(p1x),int(p1y))
Point2 = (int(p2x),int(p2y))
Point3 = (int(p3x),int(p3y))

Pointsum = [Point1,Point2,Point3]

Ans = 0.5*abs(
                (Pointsum[0][0]*(Pointsum[1][1]-Pointsum[2][1])) -
                (Pointsum[1][0]*(Pointsum[0][1]-Pointsum[2][1])) +
                (Pointsum[2][0]*(Pointsum[0][1]-Pointsum[1][1]))
            )
print(Pointsum)
print(Ans)

