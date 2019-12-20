import os.path

with open("Text/RawAddressData.txt", mode="r",encoding="utf-16") as rf:
    addr_data = rf.read().splitlines()
    json_data = {}
    for i in range(len(addr_data)):
        word_sp = addr_data[i].split(" ")
        word_sp = list(filter(None, word_sp))
        json_data[i] = {}
        for j in range(len(word_sp)):
            json_data[i]["No"] =  word_sp[0]

            if word_sp[-1].isnumeric():
                json_data[i]["Postcode"] =  word_sp[-1]

    for a in json_data:
        print(json_data[a])

