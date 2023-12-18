j = {a, a, b, b, b, c, c, c, c, a, a, a, a, a}
d = 1
e = 1
f = 1
g = 1
string = {}
while j == a:
    d = d + 1
d = d * a
string.append(d)

while j == b:
    e = e + 1
e = e * b
string.append(e)

while j == c:
    f = f + 1
f = f * c
string.append(f)

while j == a:
    e = e + 1
e = e - 2
g = g * a
string.append(g)

print(string)

2a 3b 4c 5a