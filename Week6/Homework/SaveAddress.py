import os.path

with open("Text/RawAddressData.txt", mode="r",encoding="utf-16") as rf:
    addr_data = rf.read().splitlines()
    for i in range(len(addr_data)):
        word_sp = addr_data[i].replace(" ม."," หมู่ ").split(" ")



        print(word_sp)
        # for j in word_sp:
        #     if j == "ม." or j == "หมู่":
        #         print(word_sp[0])


