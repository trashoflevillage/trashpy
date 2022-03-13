$ -> Pushes the stack length to the top of the stack.
+ -> Pops the top two values and outputs their sum.
- -> Pops the top two values and outputs their difference.
* -> Pops the top two values and outputs their product.
/ -> Pops the top two values and outputs their quotient.
% -> Pops the top two values and outputs their modulo.
\ -> Swaps the top two values of the stack.
> -> Pushes the bottom value to the top of the stack.
< -> Pushes the top value to the bottom of the stack.
_ -> Pops the top value of the stack.
. -> Pushes number input to top of the stack.
: -> Pops and outputs the top value of the stack.
, -> Pushes the ascii value of the input to the top of the stack.
; -> Pops and outputs the ascii value for the top of the stack.
" -> Duplicates the top value of the stack to the top of the stack.
' -> Duplicates the second top value of the stack to the top of the stack.
! -> Pops the top number of the stack. If it was 0, push 1. Otherwise, push 0.
( -> Jumps to matching ) if top number is 0.
[ -> Jumps to matching ] if top number is 0.
] -> Jumps to the matching [ if the top number is not 0.

    Everything in the stack is an integer.
    Getting input does nothing if input is empty.

Subroutines:

    Subroutines are defined with {name|code}.
    Subroutines are called with {name}, however the curly brackets aren't required if the name is one character long.
    Calling an undefined subroutine will not do anything.
    Calling a defined subroutine will run the code that was supplied for the subroutine.
    You can redefine subroutines.

    Example:

    {0|$"-}${0}

    {0|$"-} specifies that when the subroutine "0" is called, the code "$"-" will run. {0} calls the subroutine called "0", which triggers "$$-".