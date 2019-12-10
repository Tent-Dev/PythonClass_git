def underline():  # function underline
    print("-" * 30)


def set_underline(ch):  # function underline with set char by owner
    print("{}".format(ch) * 30)


def set_underline2(ch, num):  # function underline with set number of char & char by owner
    print("{}".format(ch) * num)


price = float(input("Enter Price of Product  : "))
amount = int(input("Enter Amount of Product : "))
set_underline2("*", 30)

print("PRICE        :   {:10,.2f}  Bath".format(price))
print("AMOUNT       :   {:10} ".format(amount))

subtotal = price * amount

print("SUBTOTAL     :   {:10,.2f}  Bath".format(subtotal))
set_underline2("-", 30)

vat = subtotal * 7 / 100
sum = vat + subtotal

print("VAT (7%)     :   {:10,.2f}  Bath".format(vat))
print("GRAND TOTAL  :   {:10,.2f}  Bath".format(sum))
set_underline2("/", 30)
