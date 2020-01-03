import pymongo

def insertData():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("TNI")

    #.insert_one , .insert_many
    #rs = db.students.insert_one({'id':'01111111','name':'Tent'}) #รับข้อมูลเป็น dic ชุดเดียว

    rs  = db.students.insert_many([{'id':'02','name':'Tent'},{'id':'03','name':'Tent'}])
    for e in rs.inserted_ids:
        print('{}'.format(e))

def selectData():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("MobileShop")

    rs = db.Products.find({'pprice':{'$gt':20000}}).sort([('pprice',pymongo.DESCENDING),('pname',pymongo.ASCENDING)])

    print('Found {} records'.format(rs.count()))
    j = 1
    for e in rs:
        print("{}). {} - {} - {}".format(j, e['pid'], e['pname'], e['pprice']))
        j+=1

def selectData_choice(min,max):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("MobileShop")

    rs = db.Products.find({'$and':[{'pprice':{'$gte':min}},{'pprice':{'$lte':max}}]}).sort([('pprice',pymongo.DESCENDING),('pname',pymongo.ASCENDING)])

    print('Found {} records'.format(rs.count()))
    j = 1
    for e in rs:
        print("{}). {} - {} - {}".format(j, e['pid'], e['pname'], e['pprice']))
        j+=1


if __name__ == '__main__':

    get_min = int(input("Input Min value : "))
    get_max = int(input("Input Max value : "))
    print("-"*10)
    selectData_choice(get_min,get_max)

    #insertData()
    #selectData()
