import os.path

number = int(input("Enter number of new product : "))

openfile = "TextFile/products.csv"
Exist = os.path.exists(openfile)
txt = ""
for i in range(number):
    print("Product Number [{}]".format(i + 1))
    print("=" * 30)

    name = input("\nEnter product name  : ")
    price = float(input("Enter product price : "))
    stock = int(input("Enter product stock : "))
    txt += "{},{:.2f},{:}\n".format(name,price,stock)

print(txt)
if Exist:
    fp = open(openfile, "a", encoding="utf-8")

else:
    fp = open(openfile, "x")

fp.write(txt)

fp.close()

