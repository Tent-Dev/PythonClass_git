print("Senior : 65 up \nAdult  : 18-64 \nJunior : 4-17 \nChild  : 0-3")

age_Senior, age_adult, age_Junior, age_Child = input("Enter number of Senior, Adult, Junior, Child : ").split(",")

sum = (int(age_Senior)*19.95)+(int(age_adult)*22.95)+(int(age_Junior)*14.95)+(int(age_Child)*0)

print("Total of Ticket = ${:,.2f}".format(sum))