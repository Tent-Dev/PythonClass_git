import os.path

getfile_comment = open("MyFile/practice-comment.txt","r")
getfile_rude = open("MyFile/rude_word.txt","r")

openfile_can = "MyFile/canshow.txt"
openfile_cant = "MyFile/cannottshow.txt"

Exist_can = os.path.exists(openfile_can)
Exist_cant = os.path.exists(openfile_cant)

data_comment = getfile_comment.read().splitlines()
data_rude = getfile_rude.read().splitlines()

rude_low = []
com_low = []

get_not = 0
text = ""
text_ok = ""

for i,j in enumerate(data_rude):
    rude_low.append(j.lower())

for i,j in enumerate(data_comment):
    com_low.append(j.lower())

rude_low = set(rude_low)
com_low = set(com_low)

for k,l in enumerate(com_low):
    check = l.split(" ")
    check = set(check)
    if(check & rude_low):
        get_not+= 1
        text += "{}\n".format(l)
        print(text)
        break
    else:
        text_ok += "{}\n".format(l)

if Exist_can:
        fp = open(openfile_can, "a", encoding="utf-8")

else:
    fp = open(openfile_can, "x")

if Exist_cant:
        fp = open(openfile_cant, "a", encoding="utf-8")

else:
    fp = open(openfile_cant, "x")

fp.write(text)
fp.write(text_ok)

print(check & rude_low)

print("Word rude have :{}".format(get_not))
print("Total have :{}".format(len(com_low)))

print("Bad feedback :{:.2f} %".format(get_not/len(com_low)))
