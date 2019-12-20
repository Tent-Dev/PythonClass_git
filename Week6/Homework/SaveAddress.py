import os.path

with open("Text/RawAddressData.txt", mode="r",encoding="utf-16") as rf:
    addr_data = rf.read().splitlines()
    json_data = {}
    for i in range(len(addr_data)):
        word_sp = addr_data[i].split(" ")
        word_sp = list(filter(None, word_sp))
        json_data[i] = {}
        for j in range(len(word_sp)):
            if "/" in word_sp[0] or "-" in word_sp[0]:
                json_data[i]["No"] =  word_sp[0]

            if word_sp[-1].isnumeric():
                json_data[i]["Postcode"] =  word_sp[-1]

            if "ต." in word_sp[j]:
                json_data[i]["Tumbon"] =  word_sp[j]

            if "อ." in word_sp[j]:
                json_data[i]["Aumpoar"] =  word_sp[j]

            if "จ." in word_sp[j]:
                json_data[i]["Country"] =  word_sp[j]

            if "ซ." in word_sp[j]:
                json_data[i]["Soi"] =  word_sp[j]

            if "ถ." in word_sp[j]:
                json_data[i]["Road"] =  word_sp[j]

            if "ม." in word_sp[j] or ("หมู่" in word_sp[j] and len(word_sp[j])<= 6):
                json_data[i]["Mu"] =  word_sp[j]

            #print("---->{}".format(word_sp[j]))

    for a in json_data:
        print(json_data[a])

