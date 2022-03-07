import os

userinput:list[str] = []
stack = []

class StackOutOfBounds(Exception):
    pass
 
def peek(index: int =-1):
    if len(stack) < abs(index):
        raise StackOutOfBounds
    else:
        return stack[index]

def pop():
    if len(stack) == 0:
        raise StackOutOfBounds
    else:
        return stack.pop()

def runCode(code: str):

    try:
        location = 0
        while location < len(code):
            location += 1
            char = stack[location]
            depth = 0
            if char == "(":
                depth += 1
                    while depth > 0:
                        location += 1 # TODO UNFINISHED TODO UNFINISHED TODO

            if char == "$":
                stack.append(len(stack))
                continue
            
            if char == "+":
                a = pop()
                b = pop()
                stack.append(b+a)
                continue
            
            if char == "-":
                a = pop()
                b = pop()
                stack.append(b-a)
                continue
            
            if char == "*":
                a = pop()
                b = pop()
                stack.append(b*a)
                continue
            
            if char == "/":
                a = pop()
                b = pop()
                stack.append(int(b/a))
                continue
            
            if char == "%":
                a = pop()
                b = pop()
                stack.append(b%a)
                continue

            if char == "\\":
                a = pop()
                b = pop()
                stack.append(a)
                stack.append(b)
                continue

            if char == "_":
                pop()
                continue

            if char == "\"":
                stack.append(peek())
                continue

            if char == "'":
                stack.append(peek(-2))
                continue

            if char == "!":
                stack.append(1 if pop() == 0 else 0)

            if char == ":":
                print(pop(), end="")
            
            if char == ";":
                print(chr(pop()), end="")

            if char == ".": 
                output = ""
                while len(userinput) > 0 and userinput[-1].isnumeric(): # The - sign signifies relative to the top of the list. -1 Gets from the top, -2 gets from second top, etc.
                    output = output + userinput.pop()
                
                if output != "":
                    stack.append(int(output))
                
            if char == ",":
                stack.append(ord(userinput.pop()))

            if char == ">":
                if len(stack) > 0:
                    stack.append(stack.pop(0))
                else:
                    raise StackOutOfBounds

            if char == "<":
                stack.insert(0, pop())


    except StackOutOfBounds:
        pass

filename = input("\033[32mFile Directory (.lengthy): \033[0m")

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, filename), "r") as file: # Make this automatically append .lengthy if it's not specified
    filecontents = file.read()
    if "." in filecontents or ":" in filecontents:
        userinput = list(input("\033[32mUser Input: \033[0m")) # vartype(value) converts the value to the specified variable type. This includes lists, strings, etc.
        userinput.reverse()
    runCode(filecontents)