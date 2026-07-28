# String functions
name ="kavya"
print(len(name))

x = 20
print(type(x))
y = str(x)
print(type(y))

print(name.find("vy"))
print(name.capitalize())
print(name.upper())
print(name.lower())

z= "This is kavya, and i am doing fine"
print(name.count("a"))

print(name.isupper())
print(name.islower())

print(z.split(" "))

m= "    : ;''This is kavya, and i am doing fine   "
print(m.strip())
print(m.lstrip(" :; \''"))
print(z.replace("kavya","surya"))
print(z.index("kavya"))