import csv

def workingscvfile(data):
    with open("Export/Name.csv","a") as f:
        fw = csv.writer(f)
        fw.writerows(data)

def create(name):
    insertCol = []
    insertRow = []
    email_create = name.split(" ")
    email_create = "{}.{}_st@tni.ac.th".format(email_create[1][0:2], email_create[0])
    print("Your Thai-Nichi student E-mail is \"{}\"".format(email_create.lower()))

    insertCol.append(name.title()) # .title() -> Set first character upper
    insertCol.append(email_create.lower())
    insertRow.append(insertCol)
    workingscvfile(insertRow)

name = input("Please Enter your full name : ")
create(name)




