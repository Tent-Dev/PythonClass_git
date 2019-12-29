import os.path
import sqlite3
PostCode_db = [] # จาก database thai_location
def read_database(sql_command, param_select):
    myDatabase = "Database/Thai.db"
    with (sqlite3.connect(myDatabase)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(sql_command, param_select)
        for i in cursor:
            PostCode_db.append(i["PostalCode"])

with open("Text/RawAddressData.txt", mode="r",encoding="utf-16") as rf:
    addr_data = rf.read().splitlines()
    json_data = {}
    Postcode_list = []
    for i in range(len(addr_data)):
        word_sp = addr_data[i].split(" ")
        word_sp = list(filter(None, word_sp))
        json_data[i] = {}
        for j in range(len(word_sp)):

            if word_sp[j].isnumeric() and len(word_sp[j]) == 5:
                json_data[i]["Postcode"] =  word_sp[j]
                Postcode_list.append(word_sp[j])
                #print("------->{}".format(word_sp[j]))

            if "/" in word_sp[j] or "-" in word_sp[j] or (word_sp[j].isnumeric() and word_sp[j] not in Postcode_list):
                json_data[i]["No"] =  word_sp[j]
                #print("------->{}".format(word_sp[j]))

            if "ต." in word_sp[j] or "แขวง" in word_sp[j] or "ตำบล" in word_sp[j]:
                if j + 1 < len(word_sp) and word_sp[j+1]:
                    word_sp[j+1] = word_sp[j+1].rsplit('อ.',1)[0].rsplit('อ .',1)[0].rsplit('ซ.',1)[0].rsplit('จ.',1)[0].rsplit('เขต',1)[0].rsplit('เขต.',1)[0].rsplit('อำเภอ',1)[0].rsplit('จังหวัด',1)[0]
                    word_sp[j] = word_sp[j].rsplit('อ.',1)[0]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))

                json_data[i]["District"] =  word_sp[j]

            if "อ." in word_sp[j] or "เขต" in word_sp[j] or "อำเภอ" in word_sp[j]:
                if j + 1 < len(word_sp) and word_sp[j+1]:
                    word_sp[j+1] = word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))

                json_data[i]["Zone"] =  word_sp[j]

            if "จ." in word_sp[j]:
                if j + 1 < len(word_sp) and (not word_sp[j+1].isnumeric()):
                    word_sp[j+1] = word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))
                json_data[i]["Country"] =  word_sp[j]

            if "ซ." in word_sp[j]:
                if j + 1 < len(word_sp):
                    word_sp[j + 1] = word_sp[j + 1].rsplit('จ.', 1)[0].rsplit('ต.', 1)[0].rsplit('แขวง', 1)[0].rsplit('ข.', 1)[0].rsplit('อ.', 1)[0]
                    word_sp[j] = word_sp[j] + word_sp[j + 1]
                    print("------->{}".format(word_sp[j]))
                json_data[i]["Soi"] =  word_sp[j]

            if "ถ." in word_sp[j] or "ถนน" in word_sp[j]:
                if j + 1 < len(word_sp):
                    word_sp[j + 1] = word_sp[j + 1].rsplit('จ.', 1)[0].rsplit('ต.', 1)[0].rsplit('แขวง', 1)[0].rsplit('ซ.', 1)[0].rsplit('อ.', 1)[0]
                    word_sp[j] = word_sp[j] + word_sp[j + 1].lstrip('ถ.')
                    #print("------->{}".format(word_sp[j]))
                json_data[i]["Road"] =  word_sp[j]

            if (not "กท" in word_sp[j] and "ม." in word_sp[j]) or ("หมู่" in word_sp[j] and len(word_sp[j])<= 6):
                if  j+1 < len(word_sp) and  (word_sp[j+1].isnumeric() ):
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))
                json_data[i]["Mu"] =  word_sp[j]

    for a in json_data:
        print(json_data[a])

    print(set(Postcode_list))

sql_command = """select * FROM location_thai"""
param_select = []
read_database(sql_command, param_select)

#print(set(PostCode_db))