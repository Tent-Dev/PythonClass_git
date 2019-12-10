def Types_of_integer(*num):
    a = sorted(set(num))
    word = "Prime Number"
    for i in a:
        for j in range(2,i):
            #print("j>> {} i>> {}".format(j,i))
            if i%j == 0:
                word = "Composite Number"
                break

            elif i%j > 0 or i == 2:
                word = "Prime Number"


        print("{}\t : {}".format(i,word))

# Create function Types_of_integer to display result
if __name__ == '__main__': # จะทำงานภายใต้นี้หากูกเรียกด้วยตัววมันเอง
    Types_of_integer(10,9,22,32,45,9,2,103,71,45)
    Types_of_integer(49,37,14,37)
