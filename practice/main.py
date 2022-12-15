a = 2
b = "ahoj"
c = "RRRRRR" + 'bbbbbb'

d,e,f = 5, "LLLL", 444
g = 000

print(d, g)
print(e, f)

print('aaaaaa', a, b, c)

del  a
#print(a)

print(b[2:3], g)

pole = ["abcdef", "ERTZ"]
print(pole[1:2])

print(type(b), type(g), str(g), type(g))
newG = str(g)
g = str(g)
print(newG, type(newG), type(g), g)