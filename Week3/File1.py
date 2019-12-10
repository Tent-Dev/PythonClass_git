import os.path

openfile = "TextFile/text.txt" #ต้องสร้างDirectory ก่อน ถ้าจะทำ path
Exist = os.path.exists(openfile) #เช็คว่ามีไฟล์นี้แล้วหรือยัง return boolean

if Exist :
    fp = open(openfile,"a",encoding="utf-8")

else:
    fp = open(openfile,"x")


# Mode 'x' = สร้างและเขียนไฟล์ ต้องไม่มีไฟล์นี้อยู่ก่อน
# Mode 'w' = เขียนทับ (Overwrite)
# Mode 'a' = เปิดไฟล์เพื่อเขียนต่อ
# Mode 'r' = Read
# Mode 'r+' = Read and Write

fp.write("สวัสดี\n")
fp.close()


