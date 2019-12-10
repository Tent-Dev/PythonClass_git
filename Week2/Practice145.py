#find statistic value from tuple

weight = (62.5,78,50,42,84,65.5,48,53.5,43)
num_s = 0
equal_avg = 0
above_avg = 0
below_avg = 0

max = max(weight)
min = min(weight)

avg = sum(weight)/len(weight)

for num in weight:
    if num == avg:
        equal_avg+=1
    elif num > avg:
        above_avg+=1
    elif num < avg:
        below_avg+=1

print("Maximum weight of 9 persons = {}".format(max))
print("Minimum weight of 9 persons = {}".format(min))
print("Average weight of 9 persons = {:,.2f}".format(avg))
print("No. of weight above average = {}".format(above_avg))
print("No. of weight below average = {}".format(below_avg))
print("No. of weight equal to average = {}".format(equal_avg))
