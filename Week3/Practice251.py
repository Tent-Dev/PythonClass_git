def read():
    f = open("TextFile/MarvelComics.txt","r")

    data = sorted(f.readlines(),reverse=True)

    for i,j in enumerate(data):
        print("{}.) {}".format(i+1,data[i].upper()),end="")

    f.close()

read()
