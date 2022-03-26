import os

userinput:list[str] = []
stack = []
subroutines = {}

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
        location:int = 0

        while location < len(code):
            char = code[location]
            
            if char == "(":
                if peek() == 0:
                    depth:int = 1
                    while depth > 0:
                        location += 1
                        if code[location] == "(":
                            depth += 1

                        elif code[location] == ")":
                            depth -= 1

            if char == "{":
                depth:int = 1
                subroutine:str = ""
                localloc = 0
                key = ""
                value = ""
                memory = ""
                reading = 1
                while depth > 0:
                    localloc += 1
                    location += 1
                    if code[location] == "{":
                        depth += 1
                    elif code[location] == "}":
                        depth -= 1
                    elif code[location] == "|" and depth == 1:
                        key = memory
                        memory = ""
                        reading += 1
                    memory = memory + code[location]
                if reading == 2:
                    value = memory[1:len(memory)-1]
                if reading == 1:
                    runCode(subroutines[memory[:-1]])
                    
                subroutine = subroutine + code[location]
                if key in subroutines:
                    subroutines.pop(key)
                subroutines[key] = value

            elif char == "[":
                if peek() == 0:
                    depth:int = 1
                    while depth > 0:
                        location += 1
                        if code[location] == "[":
                            depth += 1

                        elif code[location] == "]":
                            depth -= 1

            elif char == "]":
                if peek() != 0:
                    depth:int = 1
                    while depth > 0:
                        location -= 1
                        if code[location] == "[":
                            depth -= 1

                        elif code[location] == "]":
                            depth += 1

            elif char == "$": stack.append(len(stack))
            elif char == "+": a = pop(); b = pop(); stack.append(b+a)
            elif char == "-": a = pop(); b = pop(); stack.append(b-a)
            elif char == "*": a = pop(); b = pop(); stack.append(b*a)
            elif char == "/": a = pop(); b = pop(); stack.append(int(b/a))
            elif char == "%": a = pop(); b = pop(); stack.append(b%a)
            elif char == "\\": a = pop(); b = pop(); stack.append(a); stack.append(b)
            elif char == "_": pop()
            elif char == "\"": stack.append(peek())
            elif char == "'": stack.append(peek(-2))
            elif char == "!": stack.append(1 if pop() == 0 else 0)
            elif char == ":": print(pop(), end="")
            elif char == ";": print(chr(pop()), end="")
            elif char == ".": 
                output = ""
                while len(userinput) > 0 and userinput[-1].isnumeric(): # The - sign signifies relative to the top of the list. -1 Gets from the top, -2 gets from second top, etc.
                    output = output + userinput.pop()
                if output != "":
                    stack.append(int(output))
            elif char == ",": 
                if len(stack) > 0:
                    stack.append(ord(userinput.pop()))
            elif char == ">":
                if len(stack) > 0:
                    stack.append(stack.pop(0))
                else:
                    raise StackOutOfBounds
            elif char == "<": stack.insert(0, pop())
            elif char in subroutines:
                runCode(subroutines[char])

            location += 1


    except Exception:
        pass

filename = input("\033[32mFile Directory (.lengthy): \033[0m")

dirname = os.path.dirname(__file__)

if ".lengthy" not in filename:
    filename = filename + ".lengthy"

with open(os.path.join(dirname, filename), "r") as file: # Make this automatically append .lengthy if it's not specified
    filecontents = file.read()
    if "." in filecontents or "," in filecontents:
        userinput = list(input("\033[32mUser Input: \033[0m")) # vartype(value) converts the value to the specified variable type. This includes lists, strings, etc.
        userinput.reverse()
    runCode(filecontents)