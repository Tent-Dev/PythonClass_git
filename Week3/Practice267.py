dic = {}
with open("Configuration/appConfig.ini", mode="r") as config:
    get_config = config.read().splitlines()

    for i, j in enumerate(get_config):
        key_value = j.split("=")
        dic[key_value[0]] = key_value[1]

with open("Data/products.csv", mode="r") as get_data:
    data = get_data.read().splitlines()

total = 0
for i, j in enumerate(data):
    list_data = j.split(",")
    total += (float(list_data[1]) * float(list_data[2]))
    print("{:10}{:10,.{}f}".format(list_data[0], float(list_data[1]) * float(list_data[2]), dic["decimal_places"]))

print("{}".format(dic["line"]) * 30)
print("Total Value {:10,.{}f} {}".format(total, dic["decimal_places"], dic["currency_unit"]))

# เนื่องจากช่วยคิดกับเพื่อน โค้ดอาจจะคล้ายกับอีกคนนะครับ
