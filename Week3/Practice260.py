def reader():
    with open("TextFile/ilovesea.txt",mode="r",encoding="utf-8") as f:
        data = f.readlines()
        for i,j in enumerate(data):
            print(f"{i+1} - {data[i]}",end="")
reader()

