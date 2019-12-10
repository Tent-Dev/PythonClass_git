#How to find item in list ignoring case

flowers = ["Sun flower","Ivy","Jusmine","Lily"]
search = input("Enter flower that you want to search : ")

convertCha = [item.lower() for item in flowers]
check = search.lower() in convertCha
print(check)
