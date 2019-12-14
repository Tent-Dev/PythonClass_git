import sqlite3

def text_hello(other):
    try:
        print("-" * 100)
        if other == 0:
            print("*\t\t\t\033[0;34;43mSelect Homework below !!!\033[0;0m\t\t\t*")
        else:
            print("*\t\t\t\033[0;34;43mSelect Other Homework below !!!\033[0;0m\t\t\t*")
        print("-" * 100)
        select_quiz = input("Fill Name Of Homework ([create] [add] [change] [delete] or [all] for Autorun) for Check : ")
        print("-" * 100)
        select_to_run(select_quiz)
    except Exception as e:
        print("-" * 100)
        print("\033[0;31;40m ERROR !!!\033[0;0m >>>>>>>>>> {}".format(e))
        text_hello(0)

def Report(cmd,sql_command,param_select):

    myDatabase = "AppData/Sqlite_Northwind.sqlite3"
    with (sqlite3.connect(myDatabase)) as conn:
        conn.row_factory = sqlite3.Row

        if cmd == "add":
            conn.executescript(sql_command)  # executescript ทำหลายคำสั่ง แต่รบ Parameter ได้แค่ 1

        elif cmd == "edit":
            cursor = conn.execute(sql_command, param_select)
            for i in cursor:
                print("Data --> {}".format(i["ContactName"]))

        elif cmd == "edit_y":
            conn.execute(sql_command, param_select)

        elif cmd == "del":
            cursor = conn.execute(sql_command, param_select)
            for i in cursor:
                print("Data --> {} | {}".format(i["CustomerId"],i["ShipRegion"]))

        if cmd == "del_y":
            conn.executescript(sql_command)

        elif cmd == "create":
            conn.executescript(sql_command)



def addNewCategory():
    cmd = "add"
    cate_name = input("Insert Category name : ")
    cate_desc = input("Insert Category description : ")

    sql_command = """BEGIN;
                     INSERT INTO Categories (CategoryName, Description)
                     VALUES ({}, {});
                     COMMIT;""".format(cate_name,cate_desc) #ต้อง COMMIT ถึงจะเข้า DB จริงๆ

    Report(cmd,sql_command)

def changeSuppliers():
    cmd = "edit"
    Sup_id = input("Fill Supplier ID : ")

    param_select = [Sup_id]

    sql_command = """SELECT ContactName FROM Suppliers WHERE SupplierID = ?"""

    Report(cmd,sql_command,param_select)

    select = input("Do you want to Edit data? [Y/N] : ").lower()

    if select == "y":
        cmd = "edit_y"
        Sup_new_contactname = input("Fill New contact name : ")
        sql_command = """UPDATE Suppliers
                         SET ContactName = ?
                         WHERE SupplierID = ?;
                         """
        Report(cmd,sql_command,[Sup_new_contactname,Sup_id])
    else:
        print("*" * 20)
        print("Exit this function")
        print("*" * 20)

def delOrderID():
    cmd = "del"

    Order_id = input("Fill Order ID : ")

    param_select = [Order_id]

    sql_command = """SELECT OrderID, CustomerId, ShipRegion FROM Orders WHERE OrderID = ?"""

    Report(cmd,sql_command,param_select)

    select = input("Do you want to Delete data? [Y/N] : ").lower()

    if select == "y":
        cmd = "del_y"
        sql_command = """BEGIN TRANSACTION;
                         DELETE FROM OrdersDetails
                         WHERE OrderId= {};
                         DELETE FROM Orders
                         WHERE OrderID= {};
                         ROLLBACK;""".format(Order_id,Order_id)
        Report(cmd,sql_command,[])
        print("*"*100)
        print("Delete Success! ===[next]===> Rollback to default database by ROLLBACK function")
        print("*" * 100)
    else:
        print("*" * 20)
        print("Exit this function")
        print("*" * 20)

def genDatabase():
    cmd = "create"
    sql_command = """CREATE TABLE `student` (
                     `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
                     `FIRSTNAME` TEXT UNIQUE,
                     `LASTNAME` TEXT,
                     `GENDER` TEXT);"""
    Report(cmd,sql_command,[])

def select_to_run(select_quiz):
    try:
        if select_quiz == "all":
            addNewCategory()
            changeSuppliers()
            delOrderID()
            genDatabase()

        elif select_quiz == "add":
            addNewCategory()

        elif select_quiz == "change":
            changeSuppliers()

        elif select_quiz == "delete":
            delOrderID()
        elif select_quiz == "create":
            genDatabase()

        text_hello(1)
    except Exception as e:
        print("-"*100)
        print("\033[0;31;40m ERROR !!!\033[0;0m >>>>>>>>>> {}".format(e))
        text_hello(0)

if __name__ == '__main__':
    text_hello(0)



