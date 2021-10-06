a = "1"
b = "2"

c = a + b
print(c)  # 12

d = "ABCDEFG"
first_three = d[0:3]
print(first_three)

e = 'clocrkr1e1c1t'
every_two = e[::2]
print(every_two)

f = "uppercase"
print(f.upper())

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(g.find("snow"))  # 95

bob = g.replace("Mary", "Bob")
print(bob)
