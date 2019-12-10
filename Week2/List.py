#list
Name = ["Adisak","Salinla","Pasakorn","Suwat","Surachai"]

print(Name)
print(Name[0])
print(len(Name))

Name[0] = "Chutipas" # Can Edit

print(Name[0])

print(sorted(Name))
print(Name[1:4:2]) # ดึงข้อมูล index ที่1 - 4 โดยเพิ่มขึ้นที่ละ2

Name.append("Added") #เพิ่มข้อมูลต่อท้าย

print(Name)

del Name[0] # ลบข้อมูล

Name.remove("Added") #ลบข้อมูล

print(Name)

print("--------------------------------")

mylist = []

for x in range(10):
    mylist.append(x)

print(mylist)

print("------------Convert--------------------")
a = (1,2,3,4)

b = list(a)

print(b)

print("------------Create--------------------")

dollar = [(x*30.18) for x in range(100,1001)]

print(dollar)
