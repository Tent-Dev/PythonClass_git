def set_underline2(ch, num):  # function underline with set number of char & char by owner
    print("{}".format(ch) * num)


set_underline2("*", 30)
print("C or c Area of Circle")
print("S or s Area of Rectangle")
set_underline2("*", 30)

select = input("Enter Your Choice : ")

if select == "c" or "C":
    radius_cricle = float(input("Please Input Radius : "))
    calculate = (22/7)*(radius_cricle**2)
    print("AREA = {:,.2f}".format(calculate))
