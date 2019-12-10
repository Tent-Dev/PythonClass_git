from chutipas.myLibrary import checkPrice

price = int(input("Input Price of car : "))
deprecate = int(input("Depreciation per year (%) : "))
year = int(input("How many year you want to see : "))

print("Price of Car = {:,.2f} BATH".format(price))

checkPrice(price,deprecate,year)


