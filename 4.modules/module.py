# Such a file is called a module; definitions from a module 
# can be imported into other modules or into the main module.

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# For call this module with Python interpreter or script:
# >>>   import module1

# >>>   fibo.fib(1000)
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

# >>>   fibo.fib2(100)
#       [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# >>>   fib = fibo.fib
# >>>   fib(500)
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# >>>   from fibo import fib, fib2
# >>>   fib(500)
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# >>>   from fibo import *
# >>>   fib(500)
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# Note that in general the practice of importing * from a 
# module or package is frowned upon, since it often causes 
# poorly readable code. 

# >>>   import fibo as fib
# >>>   fib.fib(500)
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# >>>   from fibo import fib as fibonacci
# >>>   fibonacci(500)
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# Executing modules as scripts

# adding this code at the end of your module:
# if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))

# $ python fibo.py 50
#   0 1 1 2 3 5 8 13 21 34
