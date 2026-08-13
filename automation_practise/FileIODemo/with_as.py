# without with keyword we need to closse the file after each operation, using with we can avoid this
# f=open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "r")
# print(f.read())


# f=open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "r+")
# f.write("This is readwrite text")

with open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "w") as fw:
    fw.write("This is the line using with keyword")

with open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "r") as fw:
    print(fw.read())

    