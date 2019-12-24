#เพิ่มนักเรียนกี่คน รับเท่านั้น ไอดี ชื่อ --> เก็บdb

import pymongo

def add():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("TNI")
    json_data = []

    get = int(input("How many data to add : "))

    for i in range(get):
        dic_data = {}

        get_id = input("New ID : ")
        get_name = input("New Name : ")

        print("-"*30)

        dic_data['id'] = get_id
        dic_data['name'] = get_name

        json_data.append(dic_data)

    print(json_data)

    rs = db.students.insert_many(json_data)

if __name__ == '__main__':
    add()

