# = is assignment, == is equals to

i = 0 # Iterations for the while loop.

# Mult of 3 is Fizz, mult of 5 is Buzz, mult of both is FizzBuzz

while i < 200:

    i += 1
    
    if i%3 == 0 and i%5 == 0:
        print("\033[32mFizzBuzz\033[0m")
    elif i%3 == 0:
        print("\033[96mFizz\033[0m")
    elif i%5 == 0:
        print("\033[95mBuzz\033[0m")
    else:
        print(i)
    