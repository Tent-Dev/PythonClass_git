import csv
import os.path

def writeProduct_csv(filename, data, mode):

    with open(filename, mode, newline="", encoding="utf8") as f:
        fw = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
        fw.writerows(data)

def ReadProduct_csv(filename):
    with open(filename, "r", newline="", encoding="utf8") as f:
        fr = csv.reader(f)
        total = 0
        for row in fr:
            total += (float(row[1]) * float(row[2]))
            print("{:10}{:10,.{}f}".format(row[0], float(row[1]) * float(row[2]),dic["decimal_places"]))

        print("{}".format(dic["line"]) * 30)
        print("Total Value {:10,.{}f} {}".format(total, dic["decimal_places"], dic["currency_unit"]))


dic = {}

with open("Configuration/appConfig.ini", mode="r") as config:
    get_config = config.read().splitlines()

    for i, j in enumerate(get_config):
        key_value = j.split("=")
        dic[key_value[0]] = key_value[1]


my_file = "TextFile/products.csv"
Exist = os.path.exists(my_file)

number = int(input("Enter number of new product : "))
ListofData=[]
DetailsOfData =[]

for i in range(number):
    print("Product Number [{}]".format(i + 1))
    print("=" * 30)

    name = input("\nEnter product name  : ")
    price = float(input("Enter product price : "))
    stock = int(input("Enter product stock : "))

    DetailsOfData.append(name)
    DetailsOfData.append(price)
    DetailsOfData.append(stock)
    DetailsOfData.append(price*stock)
    ListofData.append(DetailsOfData)
    DetailsOfData=[]

if Exist:
    writeProduct_csv(my_file, ListofData, "a")

else:
    writeProduct_csv(my_file, ListofData, "x")

ReadProduct_csv(my_file)

