#Find the comment have rude word

rude_word = ["damn","hell","ass","piss","silly","idiotic"]

comment_input = input("Please comment our service : ")

comment = comment_input.lower().split(" ")
check = 0


for i,word in enumerate(comment):

    for j in rude_word:
        if word == j:
            print("Cannot show [{}]".format(comment_input))
            check+=1
            break

if check == 0:
    print("Can show [{}]".format(comment_input))


