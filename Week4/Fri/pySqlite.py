import sqlite3

def showReport(sql_command,select_db,up,sort_command):
    myDatabase = "AppData/Sqlite_Northwind.sqlite3"
    try:
        with (sqlite3.connect(myDatabase)) as conn: #ติดต่อ db
            conn.row_factory = sqlite3.Row #ช่วยเรื่องการอ้างอิงด้วย ชื่อ ของ คอลัมได้
            if sql_command is None:
                sql_command = """select * from """+"{}".format(select_db)+"""
                                 where unitprice between ? and  ?
                                 order by unitprice"""+" {}".format(sort_command) # ใช้ """ เพื่อต่อสตริงหลายบรรทัด
                cursor = conn.execute(sql_command, up) #ค่าที่ส่งต้งเป็น list
                #found = len(conn.execute(sql_command, up).fetchall()) #หาจำนวนแถว
            j = 1
        for i in cursor:
            print("{}). {:35}: {} Bath".format(j,i["productname"],i[5])) # Tuple
            j+=1

    except Exception as e:
        print("Error {}".format(e))

def Practice336():
    select_table = "products"
    start = int(input("Enter Start price do you want to see : "))
    end =   int(input("Enter End price do you want to see : "))
    while end < start:
        print(">>End price should be more than start price<<")
        start = int(input("Enter Start price do you want to see : "))
        end =   int(input("Enter End price do you want to see : "))

    print("Sort price : [1] Ascending [2] Descending")
    sort_select = int(input("Select [1] or [2] : "))

    if sort_select == 1:
        sort_select = "asc"
    else:
        sort_select = "desc"

    param_select = [start,end]
    showReport(select_table,param_select,sort_select)

def Practice338():
    select_table = "products"
    select_cate = input("Enter your category name to see : ")
    sql_command = """select ProductName, UnitPrice from categories
                     join products
					 on Products.CategoryId = Categories.CategoryID
                     where CategoryName like \""""+"{}".format(select_cate)+"""\"
					 Order by Productname"""

    print(sql_command)


    #showReport(myDatabase,select_table,param_select,sort_select)

if __name__ == '__main__':
    Practice336()
    Practice338()


