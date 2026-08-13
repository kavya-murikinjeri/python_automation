f=open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "r")
print(f.read())
f.close()

f=open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "r+")
f.write("This is readwrite text")
f.close()