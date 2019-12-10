def reader():
    with open("TextFile/province.txt",mode="r",encoding="utf-8") as f:
        data = f.read()
        print(data)

def reader_2():
    with open("TextFile/ilovesea.txt",mode="r",encoding="utf-8") as f:
        data = f.readlines()
        for i,j in enumerate(data):
            print(f"{i+1} - {data[i]}")

reader()
reader_2()
