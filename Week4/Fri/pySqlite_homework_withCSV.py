import sqlite3
import csv
import os.path

def write_csv(filename, data, mode):
    print("----->",data)
    with open(filename, mode, newline="", encoding="utf8") as f:
        fw = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
        fw.writerows(data)

def text_hello(other):
    try:
        print("-" * 100)
        if other == 0:
            print("*\t\t\t\033[0;34;43mSelect Homework below !!!\033[0;0m\t\t\t*")
        else:
            print("*\t\t\t\033[0;34;43mSelect Other Homework below !!!\033[0;0m\t\t\t*")
        print("-" * 100)
        select_quiz = int(input("Select No. Of Homework (1-10 or 0 for Autorun) for Check : "))
        print("-" * 100)
        select_to_run(select_quiz)
    except Exception as e:
        print("-" * 100)
        print("\033[0;31;40m ERROR !!!\033[0;0m >>>>>>>>>> {}".format(e))
        text_hello(0)

def showReport(cmd, sql_command, param_select):
    myDatabase = "AppData/Sqlite_Northwind.sqlite3"
    try:
        with (sqlite3.connect(myDatabase)) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(sql_command, param_select)  # ค่าที่ส่งต้งเป็น list
            j = 1

        if cmd == "pracSqlExtra1":
            for i in cursor:
                print("{}). {:35}: {} Bath".format(j, i["productname"], i[5]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra2":
            for i in cursor:
                print("{}). {:35}: {} Bath".format(j, i["productname"], i["UnitPrice"]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra3":
            print("Supplier From \t\t\t No. of Company")
            print("-"*40)
            for i in cursor:
                print("{:30} {}".format(i["Country"], i["NoOfCompany"]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra4":
            print("Show Customers by Region")
            print("-" *50)
            print("Region \t\t\t\t\t Country \t\t City")
            print("-" *50)
            for i in cursor:
                print("{:30} {} {:10}".format(i["Region"], i["NoOfCountry"],i["NoOfCity"]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra5":
            for i in cursor:
                print("ID = {}\nProduct Name = {}\nSTOCK VALUE = {:,.2f}".format(i["ProductId"], i["ProductName"],i["StockValue"]))  # Tuple
                print("-" * 50)
                j += 1

        elif cmd == "pracSqlExtra6":
            found = len(conn.execute(sql_command, param_select).fetchall())
            print("Found {} Category(s)".format(found))
            for i in cursor:
                print("{}). {:20} {} PD. {:20,.2f} Bath".format(j,i["CategoryName"], i["SumOfName"],i["StockValue"]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra7":
            found = len(conn.execute(sql_command, param_select).fetchall())
            print("Found {} Category(s)".format(found))
            for i in cursor:
                print("{}). {} ,{} {:20}".format(j,i["Name"], i["TitleOfCourtesy"],i["Number"]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra8":
            for i in cursor:
                print("{} ({}) No. of Product = {} (Average price = {:,.2f})".format(i["Com"], i["CategoryName"],i["NoOfProduct"],i["Average"]))  # Tuple
                j += 1

        elif cmd == "pracSqlExtra9":
            get_data = []
            total_price = 0
            for i in cursor:
                get_data.append("{}). {:30} {:,.2f}".format(j,i["ProductName"],i["Price"]))
                total_price += i["Price"]
                j += 1

            print("Order ID\t : {}\nOrder Date\t : {}\nCustomer\t : {}".format(i["OrderId"], i["OrderDate"],i["Customer"]))
            print("-" * 50)
            for data in get_data:
                print(data)
            print("-" * 50)
            print("\t\t\t\t\t\tTOTAL PRICE\t : {:,.2f}".format(total_price))
            print("\t\t\t\t\t\tVAT (7%)\t : {:,.2f}".format((total_price*7)/100))
            print("\t\t\t\t\t\tNET PRICE\t : {:,.2f}".format(((total_price * 7) / 100)+total_price))
            print("-" * 50)
            print("Send by : {}".format(i["SendBy"]))

            my_file = "pracSql9_export.csv"
            param_select.append(((total_price * 7) / 100)+total_price)
            Exist = os.path.exists(my_file)

            if Exist:
                write_csv(my_file, param_select, "a")

            else:
                write_csv(my_file, param_select, "x")

        elif cmd == "pracSqlExtra10":
            print("Show Customers by Sale")
            print("-"*100)
            print("Country\t\t\t\tNo.Of Order\t\t\t\tNET Price\t\t\t\tPrice/Order")
            print("-" * 100)
            for i in cursor:
                print("{:15} {:10} {:25,.2f} {:25,.2f}".format(i["Country"], i["NoOfOrder"],i["NetPrice"],i["PricePerOrder"]))  # Tuple
                j += 1

    except Exception as e:
        print("Error {}".format(e))

def Practice336():
    cmd = "pracSqlExtra1"
    start = int(input("Enter Start price do you want to see : "))
    end = int(input("Enter End price do you want to see : "))
    while end < start:
        print(">>End price should be more than start price<<")
        start = int(input("Enter Start price do you want to see : "))
        end = int(input("Enter End price do you want to see : "))

    print("Sort price : [1] Ascending [2] Descending")
    sort_select = int(input("Select [1] or [2] : "))

    if sort_select == 1:
        sort_select = "asc"
    else:
        sort_select = "desc"

    sql_command = """select * from products
                     where unitprice between ? and  ?
                     order by unitprice""" + " {}".format(sort_select)

    param_select = [start, end]
    showReport(cmd ,sql_command, param_select)

def Practice338():
    cmd = "pracSqlExtra2"
    select_cate = input("Enter your category name to see : ")
    sql_command = """select ProductName, UnitPrice from categories
                     join products
					 on Products.CategoryId = Categories.CategoryID
                     where CategoryName like ?
					 Order by Productname"""

    param_select = [select_cate]
    showReport(cmd, sql_command, param_select)

def pracSqlExtra3():
    cmd = "pracSqlExtra3"
    sql_command = """select Country, count(CompanyName) as NoOfCompany from Suppliers
                     GROUP by Country
                     ORDER by NoOfCompany DESC"""

    param_select = []
    showReport(cmd, sql_command, param_select)

def pracSqlExtra4():
    cmd = "pracSqlExtra4"
    sql_command = """select Region, count(DISTINCT(Country)) as NoOfCountry, count(DISTINCT(City)) as NoOfCity from Customers
                     GROUP by Region
                     ORDER by NoOfCity DESC"""
    param_select = []
    showReport(cmd, sql_command, param_select)

def pracSqlExtra5():
    cmd = "pracSqlExtra5"

    select = int(input("Show Stock value more than : "))

    sql_command = """select ProductId, ProductName,UnitPrice*UnitsInStock as StockValue from Products
                     WHERE StockValue > ?
                     ORDER by StockValue DESC"""
    param_select = [select]
    showReport(cmd, sql_command, param_select)

def pracSqlExtra6():
    cmd = "pracSqlExtra6"

    select = int(input("See value of Stock by Category > : "))

    sql_command = """select CategoryName, count(ProductName) as SumOfName,sum(UnitPrice*UnitsInStock) as StockValue from Products
                     JOIN Categories
                     on Categories.CategoryId = Products.CategoryId
                     GROUP by CategoryName
                     HAVING StockValue > ?
                     ORDER by StockValue"""
    param_select = [select]
    showReport(cmd, sql_command, param_select)

def pracSqlExtra7():
    cmd = "pracSqlExtra7"

    sql_command = """select (FirstName || " " || LastName) as Name, TitleOfCourtesy, Orders.EmployeeId, count(*) as Number from Orders
                     JOIN Employees on Employees.EmployeeID = Orders.EmployeeId
                     Group by Orders.EmployeeId
                     ORDER by Number"""
    param_select = []
    showReport(cmd, sql_command, param_select)

def pracSqlExtra8():
    cmd = "pracSqlExtra8"

    sql_command = """select DISTINCT Suppliers.CompanyName as Com, CategoryName,count(Products.ProductID) as NoOfProduct, avg(Products.UnitPrice) as Average from Products
                     join Suppliers
                     on Products.SupplierId = Suppliers.SupplierID
                     join Categories
                     on Categories.CategoryID = Products.CategoryId
					 GROUP by Products.CategoryID , Products.SupplierId
					 Order by Com"""
    param_select = []
    showReport(cmd, sql_command, param_select)

def pracSqlExtra9():
    cmd = "pracSqlExtra9"

    select = int(input("Please Fill Your Order ID to check  : "))

    sql_command = """SELECT Orders.OrderId, OrderDate, ShipName as Customer, Shippers.CompanyName as SendBy, ProductName, (OrdersDetails.UnitPrice*OrdersDetails.Quantity) as Price FROM Orders
                     join Shippers
                     on Orders.ShipVia = Shippers.ShipperID
                     join OrdersDetails
                     on OrdersDetails.OrderId = Orders.OrderID
                     join Products
                     on Products.ProductId = OrdersDetails.ProductId
                     WHERE Orders.OrderId = ?"""
    param_select = [select]
    showReport(cmd, sql_command, param_select)

def pracSqlExtra10():
    cmd = "pracSqlExtra10"

    sql_command = """SELECT Country, count(OrdersDetails.OrderId) as NoOfOrder, (sum((OrdersDetails.UnitPrice*OrdersDetails.Quantity)* (1-OrdersDetails.Discount) * 1.07)) as NetPrice, (sum((OrdersDetails.UnitPrice*OrdersDetails.Quantity)* (1-OrdersDetails.Discount) * 1.07)/count(OrdersDetails.OrderId)-OrdersDetails.Discount*100) as PricePerOrder FROM Customers
                     JOIN Orders
                     ON Orders.CustomerId = Customers.CustomerID
                     JOIN OrdersDetails
                     ON OrdersDetails.OrderId = Orders.OrderID
                     GROUP by Country
                     ORDER by PricePerOrder DESC"""
    param_select = []
    showReport(cmd, sql_command, param_select)

def select_to_run(select_quiz):
    try:
        if select_quiz == 0:
            Practice336()
            Practice338()
            pracSqlExtra3()
            pracSqlExtra4()
            pracSqlExtra5()
            pracSqlExtra6()
            pracSqlExtra7()
            pracSqlExtra8()
            pracSqlExtra9()
            pracSqlExtra10()

        elif select_quiz == 1:
            Practice336()

        elif select_quiz == 2:
            Practice338()

        elif select_quiz == 3:
            pracSqlExtra3()
        elif select_quiz == 4:
            pracSqlExtra4()

        elif select_quiz == 5:
            pracSqlExtra5()

        elif select_quiz == 6:
            pracSqlExtra6()

        elif select_quiz == 7:
            pracSqlExtra7()

        elif select_quiz == 8:
            pracSqlExtra8()

        elif select_quiz == 9:
            pracSqlExtra9()

        elif select_quiz == 10:
            pracSqlExtra10()

        text_hello(1)
    except Exception as e:
        print("-"*100)
        print("\033[0;31;40m ERROR !!!\033[0;0m >>>>>>>>>> {}".format(e))
        text_hello(0)

if __name__ == '__main__':
    text_hello(0)


