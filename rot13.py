input = "Hello World"
input = input.upper()
o = ""

for i in input:
    if i != " ":
        a = ord(i) - 13
        if a < 65:
            a = ord(i) + 13
        i = chr(a)
    o = o + i

print(o)