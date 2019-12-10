def star():
    print("*" * 55)

def line():
    print("-" * 55)

def calGrade(total):
    if total >= 97:
        grade = "A+"
    elif total >= 93:
        grade = "A"
    elif total >= 90:
        grade = "A-"
    elif total >= 87:
        grade = "B+"
    elif total >= 83:
        grade = "B"
    elif total >= 80:
        grade = "B-"
    elif total >= 77:
        grade = "C+"
    elif total >= 73:
        grade = "C"
    elif total >= 70:
        grade = "C-"
    elif total >= 67:
        grade = "D+"
    elif total >= 63:
        grade = "D"
    elif total >= 60:
        grade = "D-"
    else:
        grade = "F"

    return grade

def checkWord(word):
    i = 0
    wordA = 0
    check = ["A","E","I","O","U"]
    for value in word:
        value.upper()
        if value == check[i]:
            wordA+=1
            i+=1

    if wordA > 0:
        print("Have vowels")
    else:
        print("Without vowels")

    print("word : {}".format(wordA))

def checkPrice(price,deprecate,year):
    import math
    price_in_loop = price
    for numofyear in range(1,year+1,1):
        deprecate_in_loop = (price_in_loop*deprecate)/100
        pricesum = price_in_loop - deprecate_in_loop

        math.ceil(pricesum)
        print("After {} year : Reduce = {:,.2f} BATH Price = {:,.2f} BATH".format(numofyear,deprecate_in_loop,pricesum))
        price_in_loop = pricesum

