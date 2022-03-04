p = 0 # Pointer position
a = [] # Array contents

i = 0

while i < 30000: # Fills the array with 30k cells
    i += 1
    a.append(0)
    print("\033[95mInitializing array: \033[0m" + str(i) + "/30000")

print("> = Increment the data pointer (to point to the next cell to the right).\n< = Decrement the data pointer (to point to the next cell to the left).\n+ = Increment (increase by one) the byte at the data pointer.\n- = Decrement (decrease by one) the byte at the data pointer.\n. = Output the byte at the data pointer.\n, = Accept one byte of input, storing its value in the byte at the data pointer.\n[ = If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.\n] = If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.\nAll other characters will be ignored.")

input = input("\033[32mBrainfuck: \033[0m")

for i in input:
    
    print(i)

    if i == ">":
        if p < 30000:
            p += 1
            
    if i == "<":
        if p > 0:
            p -= 1

    if i == "+":
        c = a[p] + 1
        a[p] = c

    if i == "-":
        c = a[p] - 1
        a[p] = c
    
    
print(a)