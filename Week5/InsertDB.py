import sqlite3

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

def delOrderID():
    cmd = "del"

    Order_id = input("Fill Order ID : ")

    param_select = [Order_id]

    sql_command = """SELECT OrderID, CustomerId, ShipRegion FROM Orders WHERE OrderID = ?"""

    Report(cmd,sql_command,param_select)

    select = input("Do you want to Delete data? [Y/N] : ").lower()

    # if select == "y":
    #     cmd = "del_y"
    #     sql_command = """UPDATE Suppliers
    #                      SET ContactName = ?
    #                      WHERE SupplierID = ?;
    #                      """
    # Report(cmd,sql_command,[])


    #รับข้อมูล Order ID ที่จะลบ
    #แสดงข้อมูล Order ID
    #ถามผู้ใช้ว่าจะลบไหม

def genDatabase():
    cmd = "create"
    sql_command = """CREATE TABLE `student` (
                     `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
                     `FIRSTNAME` TEXT UNIQUE,
                     `LASTNAME` TEXT,
                     `GENDER` TEXT);"""
    Report(cmd,sql_command,[])

if __name__ == '__main__':

    #addNewCategory()
    #changeSuppliers()
    delOrderID()



