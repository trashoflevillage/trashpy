
i = 0
nums = [0,1]
print(0)
print(1)

while i < 200:

    output = (nums[-1]) + (nums[-2]) # listname[-1] gets the last index, listname[-2] gets the second to last index.
    nums.append(output)
    print(output)
    i += 1
    
