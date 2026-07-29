li = ["AP","Delhi","Banglore","Karnataka","Kerala","Ooty"]
# lists are ordered, mutable, allow duplicates and enclose within [], accessible via indexing

print(li[3])
print(li[0:4:2])

# List methods
li.append("Chennai")
print(li)
print(li.sort)
print(li.index("Karnataka"))
print(li.count("Kerala"))
print(li)
li.insert(0,"Coorg")
print(li)
li.pop()
print(li)
li.remove("Karnataka")
print(li)
li.reverse()
print(li)
