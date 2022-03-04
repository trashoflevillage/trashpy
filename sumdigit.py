import math

input = 652
o = 0
i = 0

while input > 0:
    n = input%10
    input = math.floor(input/10)
    o += n
    i += 1
print(o)