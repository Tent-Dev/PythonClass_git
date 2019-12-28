import os.path

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

            if "ต." in word_sp[j]:
                if j + 1 < len(word_sp) and word_sp[j+1]:
                    word_sp[j+1] = word_sp[j+1].rsplit('อ.',1)[0].rsplit('อ .',1)[0].rsplit('ซ.',1)[0].rsplit('จ.',1)[0]
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))

                json_data[i]["Tumbon"] =  word_sp[j]

            if "อ." in word_sp[j]:
                if j + 1 < len(word_sp) and word_sp[j+1]:
                    word_sp[j+1] = word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))

                json_data[i]["Aumpoar"] =  word_sp[j]

            if "จ." in word_sp[j]:
                if j + 1 < len(word_sp) and (not word_sp[j+1].isnumeric()):
                    word_sp[j+1] = word_sp[j+1].rsplit('จ.',1)[0].rsplit('ซ.',1)[0].rsplit('ต.',1)[0]
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))
                json_data[i]["Country"] =  word_sp[j]

            if "ซ." in word_sp[j]:
                json_data[i]["Soi"] =  word_sp[j]

            if "ถ." in word_sp[j]:
                json_data[i]["Road"] =  word_sp[j]

            if (not "กท" in word_sp[j] and "ม." in word_sp[j]) or ("หมู่" in word_sp[j] and len(word_sp[j])<= 6):
                if  j+1 < len(word_sp) and  (word_sp[j+1].isnumeric() ):
                    word_sp[j] = word_sp[j]+word_sp[j+1]
                    #print("------->{}".format(word_sp[j]))
                json_data[i]["Mu"] =  word_sp[j]

            #print("---->{}".format(word_sp[j]))

    for a in json_data:
        print(json_data[a])

    print(set(Postcode_list))
