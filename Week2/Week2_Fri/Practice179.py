def check(applicant,num):
    wantedskill = {"C#" , "Python" , "Java" ,"PHP" , "SQL" , "Go"}
    check = len(applicant & wantedskill)

    check = (check/ len(wantedskill))*100

    print("Applicant {} skil match : {:.2f} %".format(num,check))

# Find % Skill match from Applicant

applicant1skill = {"VB","C","Ruby","Java","HTML"}
applicant2skill = {"C#","HTML","R","PHP","SQL","Swift","PHP"}
applicant3skill = {"Java","C++","Ruby","JavaScript","Objective-C","Go"}
applicant4skill = {"Java","Python","Go","SQL","Swift"}
applicant5skill = {"C++","C","C#","Objective-C","JavaScript","SQL"}
applicant = [applicant1skill,applicant2skill,applicant3skill,applicant4skill,applicant5skill]
check(applicant1skill,1)
check(applicant2skill,2)
check(applicant3skill,3)
check(applicant4skill,4)
check(applicant5skill,5)

