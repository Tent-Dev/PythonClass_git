def mulTable(mynum):
    for num in range(1,13):
        sum = mynum*num
        print("{} x {} = {}".format(mynum,num,sum))

for x in range(10):
    print("{}".format(x))

mynum = int(input("Your number : "))

mulTable(mynum)
