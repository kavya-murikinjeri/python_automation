# Dictionaries collection of key value pairs, ordered, duplicate keys are not allowed but duplicate values are allowed
# heterogeneous and mutable

dict1={1:"kavya",2:"surya",3:"Hello"}
print(dict1)
dict1[5]="product"
print(dict1)
print(dict[5])
dict1.pop(5)
print(dict1.keys())
print(dict1.values())
dict1.update({5:"product"})
print(dict1)
print(dict1.items())
dict2 = dict1.copy()
print(dict2)
print(dict1.get(2))