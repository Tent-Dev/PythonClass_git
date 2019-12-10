height = {165,150,165,110,198}

weight = set()

weight.add(100) #เพิ่มค่าเดียว
weight.update({60,50,40}) #เพิ่มหลายค่า

print(height)
print(weight)
print(len(weight))
print(weight[0])

weight.remove(100) # ถ้าไม่มีจะเออเร่อ

weight.discard(5) #ถ้าไม่มี ก็ไม่เออเร่อ


