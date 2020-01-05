import os.path
import sqlite3
PostCode_db = [] # จาก database thai_location
db_main = {}
db_sub = {}
def read_database(sql_command, param_select):
    myDatabase = "Database/Thai.db"
    json_data = {}

    with (sqlite3.connect(myDatabase)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(sql_command, param_select)
        j = 0
        for i in cursor:
            db_main[j] = {}
            db_sub[j] = {}
            json_data[j] = {}

            db_sub[j]['District'] = i['District']
            db_sub[j]['Zone'] = i["Zone"]
            db_sub[j]['Country'] = i["Province"]
            db_sub[j]['PostalCode'] = i['PostalCode']

            db_main[j][str(i['PostalCode'])] = db_sub[j]
            PostCode_db.append(i["PostalCode"])
            j+=1


def classify_data():
    with open("Text/RawAddressData.txt", mode="r",encoding="utf-16") as rf:
        addr_data = rf.read().splitlines()
        json_data = {}
        Postcode_list = []
        for i in range(len(addr_data)):
            word_sp = addr_data[i].split(" ")
            word_sp = list(filter(None, word_sp))
            json_data[i] = {}
            check_no = True
            for j in range(len(word_sp)):

                if word_sp[j].isnumeric() and len(word_sp[j]) == 5:
                    json_data[i]["Postcode"] =  word_sp[j]
                    Postcode_list.append(word_sp[j])
                    #print("------->{}".format(word_sp[j]))

                if ("/" in word_sp[j] or "-" in word_sp[j] or (word_sp[j].isnumeric() and word_sp[j] not in Postcode_list)) and check_no:
                    json_data[i]["No"] =  word_sp[j].replace('เลขที่ห้อง','')
                    check_no = False
                    #print("------->{}".format(word_sp[j]))

                if ("ต." in word_sp[j] or "แขวง" in word_sp[j] or "ตำบล" in word_sp[j]) and check_no:
                    if j + 1 < len(word_sp) and word_sp[j+1]:
                        word_sp[j+1] = word_sp[j+1].rsplit('อ.',1)[0].rsplit('อ .',1)[0].rsplit('ซ.',1)[0].rsplit('จ.',1)[0].rsplit('เขต',1)[0].rsplit('เขต.',1)[0].rsplit('อำเภอ',1)[0].rsplit('จังหวัด',1)[0]
                        word_sp[j] = word_sp[j].rsplit('อ.',1)[0]+word_sp[j+1]
                        #print("------->{}".format(word_sp[j]))

                    json_data[i]["District"] =  word_sp[j].replace('ต.','').replace('ตำบล','').replace('แขวง','')

                if "อ." in word_sp[j] or "เขต" in word_sp[j] or "อำเภอ" in word_sp[j]:
                    if j + 1 < len(word_sp) and word_sp[j+1]:
                        word_sp[j+1] = word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                        word_sp[j] = word_sp[j]+word_sp[j+1]
                        #print("------->{}".format(word_sp[j]))

                    json_data[i]["Zone"] =  word_sp[j].replace('อ.','').replace('เขต','').replace('อำเภอ','')

                if "จ." in word_sp[j]:
                    if j + 1 < len(word_sp) and (not word_sp[j+1].isnumeric()):
                        word_sp[j+1] = word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                        word_sp[j] = word_sp[j]+word_sp[j+1]
                        #print("------->{}".format(word_sp[j]))
                    json_data[i]["Country"] =  word_sp[j].replace('จ.','').replace('จังหวัด','')

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
                    json_data[i]["Mu"] =  word_sp[j].replace('หมู่','ม.')

        no_postcode_count = 0
        json_data_no_posecode = {}
        for a in json_data:
            json_data_no_posecode[no_postcode_count] = {}
            print(json_data[a])
            if 'Postcode' not in json_data[a].keys():
                json_data_no_posecode[no_postcode_count] = json_data[a]
                no_postcode_count+=1


        print("-"*80)
        print("No 'Postcode' in Data : {} item(s)".format(no_postcode_count))

        choice = input("See Data it don't have 'Postcode' [Y/N] : ").lower()

        if choice == 'y':
            for a in json_data_no_posecode:
                print(json_data_no_posecode[a])


        #print(set(Postcode_list))

if __name__ == '__main__':

    classify_data()

    sql_command = """select * FROM location_thai"""
    param_select = []
    read_database(sql_command, param_select)

    #print(set(PostCode_db))

    # print('-' * 30)
    # for i in db_main:
    #     if '10200' in db_main[i]:
    #         print(db_main[i])
    #         print(db_main[i]['10200']['District'])


