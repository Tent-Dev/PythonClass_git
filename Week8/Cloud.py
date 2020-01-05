import pymongo

def insertToMongoDbCloud():
    # try:
    #     client = pymongo.MongoClient("mongodb+srv://chutipas:TaTent591220306@cluster0-94rnq.mongodb.net/test?retryWrites=true&w=majority")
    #     db = client.test
    # except Exception as e:
    #     print(e)

    client = pymongo.MongoClient("mongodb+srv://chutipas:TaTent591220306@cluster0-94rnq.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("MobileShop")
    rs = db.Products.insert_one({"pid":"p003","pname":"Motion","pbrand":"BlackBerry","pprice":9000,"psize":4.5})

    print("{}".format(rs.inserted_id))
    #print("วันนี้ไม่น่ามาเรียนเลย222")


if __name__ == '__main__':
    print("วันนี้ไม่น่ามาเรียนเลย")
    insertToMongoDbCloud()
