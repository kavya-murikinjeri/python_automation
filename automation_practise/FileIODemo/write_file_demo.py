'''
Manual steps to write a file
open notepad and create a file
write in file
close file

modes
read mode - r
write mode - w
append mode - a
readwrite mode - r+
'''
# f=open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "w")
# f.write("This is first line")
# f.close

f=open("C:\\Users\\suri1\\Downloads\\writedemo.txt", "a")
l = [1,2,3,4,5]
for i in l:
    f.write(str(i)+"\n")
    f.close()