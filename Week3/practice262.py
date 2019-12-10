import os.path

ok_list = []
bad_list = []

with open("MyFile/rude_word.txt", mode="r") as rf:
    r_word = rf.read().lower().splitlines()

with open("MyFile/practice-comment.txt", mode="r") as f:
    c_word = f.read().lower().splitlines()
    for i in range(len(c_word)):
        check_bad = False
        c_word_sp = c_word[i].split(" ")

        for j in c_word_sp:
            if j in r_word:
                check_bad = True

        if check_bad:
            bad_list.append(c_word[i])
        else:
            ok_list.append(c_word[i])
print(ok_list)

open_File_can = "MyFile/canshow.txt"
exist_can = os.path.exists(open_File_can)

with open("MyFile/canshow.txt", mode="a") as wc:
    for i in ok_list:
        if exist_can:
            wc.write("{}\n".format(i))
        else:
            wc.write("{}\n".format(i))

    for a in bad_list:
        if exist_can:
            wc.write("{}\n".format(a))
        else:
            wc.write("{}\n".format(a))

print("Bad Feedback = {:.2f} %".format((len(bad_list) / (len(ok_list) + len(bad_list))) * 100))
