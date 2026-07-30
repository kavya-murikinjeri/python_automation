# tuples are immutable, ordered, indexed, allow duplicates
t1=(1,2,"kavya","surya",True, False, True, False)
t2=(5,6,7,8)

print(t1)
print(t1[6])
print(t1[0:5:1])
print(t1[-1])
print(len(t1))
print(type(t1))
t3= t1 + t2
print(t3)
print(type(t3))
# t1.append("true")
print(t1.index("surya"))