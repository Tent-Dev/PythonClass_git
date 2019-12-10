def checkNumber(*num,see):  #*num คือ ให้มอง num เป็น Tuple
    if see =="max-min":
        x = max(num)
        y = min(num)
        return x,y

    elif see =="ab-bl-av":
        x = 0
        y = 0

        avg = sum(num)/len(num)

        for j in num:
            if j > avg:
                x +=1
            elif j < avg:
                y +=1

        return x,y


x,y = checkNumber(17,22,35,55,67,38,98,109,10,5,77,see="max-min")
print("MAXIMUM = {0}\nMINIMUM = {1}".format(x,y))
x,y = checkNumber(12,99,34,67,21,98,13,see="ab-bl-av")
print("ABOVE AVERAGE = {0}\nBELOW AVERAGE = {1}".format(x,y))
