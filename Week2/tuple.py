#tuple

mytuple1 = ("Adisak", 40, "TNI")
mytuple2 = 150.5, 15, 60 ,"Test"
mytuple3 = mytuple1+mytuple2 # เอามาต่อกัน
mytuple4 = (1,2,8,5,6,2,3) #เก็บตัวเลขอย่างเดียว
print(mytuple1)
print(mytuple2)

print("\nBy Position : {}".format(mytuple1[0]))

print("Lenght : {}\n".format(len(mytuple1)))

print("--------------ทำกับตัว Index--------------")
for x in range(len(mytuple1)):
    print (mytuple1[x])

print("------------ทำกับตัวข้อมูลทีละตำแหน่ง----------------")

for x in mytuple1:
    print(x)
print("----------------------------")


for i,j in enumerate(mytuple1): # ดึงค่าในแต่ละ loop i = ตำแหน่ง j = ค่าในตำแหน่งนั้นๆ
    print("{} - {}".format(i,j))

print("----------------------------")
print("{}".format(mytuple3))
print("----------------------------")

print(sorted(mytuple4)) # เรียงลำดับ *ต้อง data type เดียวกัน -> ออกมาเป็น List [..,..,..]
