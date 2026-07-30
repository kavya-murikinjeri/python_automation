# Zip(arg1,arg2) returns an iterator tuple, takes lists, tuples, sets as arguments

l1 = [1,2,3]
l2=["ind", "Aus","pak"]

op=zip(l1,l2)
print(op)
print(list(op))

tot_price = (40, 50, 60)
Discount = (30,19,20)
zi=zip(tot_price,Discount)

for x,y in zi:
    print(x-y)