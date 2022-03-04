p = 0 # Pointer position
a = [] # Array contents

i = 0

while i < 30000: # Fills the array with 30k cells
    i += 1
    a.append(0)

print("> = Increment the data pointer (to point to the next cell to the right).\n< = Decrement the data pointer (to point to the next cell to the left).\n+ = Increment (increase by one) the byte at the data pointer.\n- = Decrement (decrease by one) the byte at the data pointer.\n. = Output the byte at the data pointer.\n, = Accept one byte of input, storing its value in the byte at the data pointer.\n[ = If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.\n] = If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.\nAll other characters will be ignored.")

ud = input("\033[32mBrainfuck: \033[0m")
ui = input("\033[32mInput: \033[0m")

loc = 0

while loc < len(ud):

    i = ud[loc]

    if i == "[":
        if a[p] == 0:
            obrac = 1
            while obrac > 0:
                loc += 1
                if ud[loc] == "[":
                    obrac += 1
                if ud[loc] == "]":
                    obrac -= 1     

    if i == "]":
        if a[p] != 0:
            obrac = 1
            while obrac > 0:
                loc -= 1
                if ud[loc] == "]":
                    obrac += 1
                if ud[loc] == "[":
                    obrac -= 1    

    if i == ">":
        p += 1
        if p > 30000:
            print("\nOut of bounds exception")
            break

            
    if i == "<":
        p -= 1
        if p < 0:
            print("\nOut of bounds exception")
            break

    if i == "+":
        a[p] = (a[p] + 1)%256

    if i == "-":
        a[p] = (a[p] - 1)%256

    if i == ".":
        print(chr(a[p]), end="")

    if i == ",":
        if len(ui) > 0:
            a[p] = ord(ui[0])
            ui = ui[1:] # num: gets all the num above it
        else:
            a[p] = 0
        
    loc += 1


print("\nStopped Execution")