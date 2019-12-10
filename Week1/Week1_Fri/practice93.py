#import myLibrary # เรียกใช้ฟังก์ชั่นจากไฟล์อื่น
import csv
from chutipas.myLibrary import star , line, calGrade

#เขียน function ในการเก็บข้อมูล csv (ไฟล์ text)
def workingscvfile(data):
    with open("Export/score.csv","a") as f:
        fw = csv.writer(f)
        fw.writerows(data)

#list (next week)
insertCol = []
insertRow = []

#myLibrary.star() # Ex เรียกใช้ฟังก์ชั่นจากไฟล์อื่น
star() # import แบบ from
print("\t\t\t\t\tScore Calculate")
hwScore = float(input("Please enter Homework Score(Max is 100 points)\t: "))
midScore = float(input("Please enter Midterm Score(Max is 100 points)\t: "))
finalScore = float(input("Please enter Final Score(Max is 100 points)\t\t: "))

#myLibrary.star()
star()
hw = (hwScore * 20) / 100
mid = (midScore * 30) / 100
final = (finalScore * 50) / 100
total = hw + mid + final
print("Your Total Score is {:.2f}".format(total))
star()
print("Your grade is {}".format(calGrade(total)))
#myLibrary.line()
line()

#append list
insertCol.append(hwScore) # นำข้อมูลมาต่อกัน ใน list
insertCol.append(midScore)
insertCol.append(finalScore)
insertCol.append(calGrade(total))

insertRow.append(insertCol)
workingscvfile(insertRow)
