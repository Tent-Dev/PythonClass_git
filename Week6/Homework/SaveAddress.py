import os.path
import sqlite3
PostCode_db = [] # จาก database thai_location
db_main = {}
db_zone = {}
db_country = {}

db_sub = {}
def read_database(sql_command, param_select):
    myDatabase = "Database/Thai.db"

    with (sqlite3.connect(myDatabase)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(sql_command, param_select)
        j = 0
        for i in cursor:
            db_main[j] = {}
            db_zone[j] = {}
            db_country[j] = {}

            db_sub[j] = {}
            db_sub[j]['District'] = i['District']
            db_sub[j]['Zone'] = i["Zone"]
            db_sub[j]['Country'] = i["Province"]
            db_sub[j]['PostalCode'] = str(i['PostalCode'])

            db_main[j][str(i['PostalCode'])] = db_sub[j]
            db_zone[j][str(i['Zone'])] = db_sub[j]
            db_country[j][str(i['Province'])] = db_sub[j]

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
            check_zone = True
            for j in range(len(word_sp)):

                if word_sp[j].isnumeric() and len(word_sp[j]) == 5:
                    json_data[i]["Postcode"] =  word_sp[j]
                    Postcode_list.append(word_sp[j])
                    #print("------->{}".format(word_sp[j]))

                if ("/" in word_sp[j] or "-" in word_sp[j] or (word_sp[j].isnumeric() and word_sp[j] not in Postcode_list)) and check_no:
                    json_data[i]["No"] =  word_sp[j].replace('เลขที่ห้อง','').rsplit('ม.',1)[0]
                    check_no = False
                    #print("------->{}".format(word_sp[j]))

                if ("ต." in word_sp[j] or "แขวง" in word_sp[j] or "ตำบล" in word_sp[j]):
                    if j + 1 < len(word_sp) and word_sp[j+1]:
                        word_sp[j] = word_sp[j].rsplit('อ.',1)[0]+word_sp[j+1].rsplit('อ.',1)[0].rsplit('อ .',1)[0].rsplit('ซ.',1)[0].rsplit('จ.',1)[0].rsplit('เขต',1)[0].rsplit('เขต.',1)[0].rsplit('อำเภอ',1)[0].rsplit('จังหวัด',1)[0]
                        #print("------->{}".format(word_sp[j]))

                    json_data[i]["District"] =  word_sp[j].replace('ต.','').replace('ตำบล','').replace('แขวง','')

                if ("อ." in word_sp[j] or "เขต" in word_sp[j] or "อำเภอ" in word_sp[j]) and check_zone:
                    if j + 1 < len(word_sp) and word_sp[j+1]:
                        word_sp[j] = word_sp[j]+word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                        #print("------->{}".format(word_sp[j]))

                    json_data[i]["Zone"] =  word_sp[j].replace('อ.','').replace('เขต','').replace('อำเภอ','').replace('กทม','').replace('.','').replace('กรุงเทพมหานคร','')
                    check_zone = False

                if "จ." in word_sp[j]:
                    if j + 1 < len(word_sp) and (not word_sp[j+1].isnumeric()):
                        word_sp[j] = word_sp[j]+word_sp[j+1].rsplit('อ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                        #print("------->{}".format(word_sp[j]))
                    json_data[i]["Country"] =  word_sp[j].replace('จ.','').replace('จังหวัด','')

                if "ซ." in word_sp[j]:
                    if j + 1 < len(word_sp):
                        word_sp[j] = word_sp[j] + word_sp[j + 1].rsplit('จ.', 1)[0].rsplit('ต.', 1)[0].rsplit('แขวง', 1)[0].rsplit('ข.', 1)[0].rsplit('อ.', 1)[0]
                        #print("------->{}".format(word_sp[j]))
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
        no_country_count = 0
        json_data_no_posecode = {}
        json_data_no_country = {}
        for a in json_data:
            json_data_no_posecode[no_postcode_count] = {}
            json_data_no_country[no_country_count] = {}

            for i in db_main: # Replace data from DB_Thai to db if missing
                if 'Zone' in json_data[a].keys() and json_data[a]['Zone'] in db_zone[i].keys():
                    json_data[a].update(Country=db_zone[i][json_data[a]['Zone']]['Country'],
                                        Postcode=db_zone[i][json_data[a]['Zone']]['PostalCode'])

                if 'Postcode' in json_data[a].keys() and json_data[a]['Postcode'] in db_main[i].keys() and 'Country' not in json_data[a].keys():
                    json_data[a].update(Country=db_main[i][json_data[a]['Postcode']]['Country'])

                if 'Country' in json_data[a].keys() and json_data[a]['Country'] in db_country[i].keys() and 'Postcode' not in json_data[a].keys():
                    json_data[a].update(Postcode=db_country[i][json_data[a]['Country']]['PostalCode'])

            if 'Postcode' not in json_data[a].keys():
                json_data_no_posecode[no_postcode_count] = json_data[a]
                no_postcode_count+=1

            if 'Country' not in json_data[a].keys():
                json_data_no_country[no_country_count] = json_data[a]
                no_country_count+=1

        for k in json_data:
            print(json_data[k])
        print("-"*80)
        print("No 'Postcode' in Data : {} item(s)".format(no_postcode_count))
        print("No 'Country' in Data : {} item(s)".format(no_country_count))

        choice = input("See Data it don't have 'Postcode' [Y/N] : ").lower()

        if choice == 'y':
            for a in json_data_no_posecode:
                print(json_data_no_posecode[a])

        elif choice == 'n':
            choice2 = input("See Data it don't have 'Country' [Y/N] : ").lower()

            if choice2 == 'y':
                for a in json_data_no_country:
                    print(json_data_no_country[a])


        #print(set(Postcode_list))

if __name__ == '__main__':

    sql_command = """select * FROM location_thai"""
    param_select = []
    read_database(sql_command, param_select)

    classify_data()

    # print('-' * 30)
    # for i in db_main:
    #     if 'บางพลี' in db_zone[i]:
    #         print(db_zone[i])
    #         print(db_zone[i]['บางพลี']['PostalCode'])


