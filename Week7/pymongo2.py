import pymongo

def insertData():
    print(pymongo)
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("TNI")

    #.insert_one , .insert_many
    #rs = db.students.insert_one({'id':'01111111','name':'Tent'}) #รับข้อมูลเป็น dic ชุดเดียว

    rs  = db.students.insert_many([{'id':'02','name':'Tent'},{'id':'03','name':'Tent'}])

    for e in rs.inserted_ids:
        print('{}'.format(e))
if __name__ == '__main__':
    insertData()
