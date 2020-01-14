db.Products.find({});

db.Products.find({'pname':'U11 Eyes'}) //เอา pname = 'U11 Eyes'

db.Products.find({'pname':{'$regex':'a'}) //เอาข้อมูลpnameที่มีตัวอักษร a อยู่

db.Products.find({'pname':{'$regex':'A', '$options':'i'}}) //เอาข้อมูลpnameที่มีตัวอักษร aทั้งพิมพ์เล็ก-ใหญ่ อยู่ 

db.Products.find({'pname':{'$regex':'^S', '$options':'i'}}) //เอาข้อมูลpnameที่มีตัวอักษรขึ้นต้นด้วย S ทั้งพิมพ์เล็ก-ใหญ่

db.Products.find({'pname':{'$regex':'s$', '$options':'i'}}) //เอาข้อมูลpnameที่มีตัวอักษรลงท้ายด้วย S ทั้งพิมพ์เล็ก-ใหญ่


db.Products.update({'pbrand':'Acer'},{'$set':{'pprice':10000}}) //อัปเดทค่า pprice ที่เป็นขอ Acer ที่เจอค่าแรก
//db.Products.update({เงื่อนไข},{set:})

db.Products.update({'pbrand':'Acer'},{'$set':{'pprice':10000}},{'multi':true}) //อัปเดทค่า pprice ที่เป็นขอ Acer ทั้งหมด


db.Products.remove({'pbrand':'Acer'})

db.Products.remove({'$and':[{'psize':{'$lt':5}},{'pprice':{'$lt':5000}}]})