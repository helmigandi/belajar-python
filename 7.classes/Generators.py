""" Understanding Generators

Generator functions look and act just like regular functions, 
but with one defining characteristic. Generator functions use 
the Python yield keyword instead of return.

"""
def infinite_sequence():
    num = 0
    while num <= 100:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")
gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))

"""
yield indicates where a value is sent back to the caller, but 
unlike return, you don’t exit the function afterward.

"""

""" Building Generators With Generator Expressions

Like list comprehensions, generator expressions allow you to 
quickly create a generator object in just a few lines of code. 
They’re also useful in the same cases where list comprehensions 
are used, with an added benefit: you can create them without 
building and holding the entire object in memory before iteration. 
In other words, you’ll have no memory penalty when you use 
generator expressions.

"""
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

print(nums_squared_lc)
# [0, 1, 4, 9, 16]
print(nums_squared_gc)
# <generator object <genexpr> at 0x107fbbc78>

"""

The first object used brackets to build a list, while the second 
created a generator expression by using parentheses. The output 
confirms that you’ve created a generator object and that it is 
distinct from a list.

"""

""" Profiling Generator Performance

In this case, the list you get from the list comprehension 
is 87,624 bytes, while the generator object is only 120. 
This means that the list is over 700 times larger than the 
generator object!

"""

import sys
nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))
# 87624
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
# 88

"""

Remember, list comprehensions return full lists, while generator 
expressions return generators. Generators work the same whether 
they’re built from a function or an expression. Using an 
expression just allows you to define simple generators in a 
single line, with an assumed yield at the end of each inner 
iteration.

"""

""" Understanding the Python Yield Statement

When you call a generator function or use a generator 
expression, you return a special iterator called a generator. 
You can assign this generator to a variable in order to use it. 
When you call special methods on the generator, such as next(), 
the code within the function is executed up to yield.

When the Python yield statement is hit, the program suspends 
function execution and returns the yielded value to the caller. 
(In contrast, return stops function execution completely.) 
When a function is suspended, the state of that function is saved. 
This includes any variable bindings local to the generator, the 
instruction pointer, the internal stack, and any exception handling.

"""
def multi_yield():
yield_str = "This will print the first string"
yield yield_str
yield_str = "This will print the second string"
yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))
# This will print the first string
print(next(multi_obj))
# This will print the second string

# print(next(multi_obj))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

"""

Take a closer look at that last calls to next(). You can see 
that execution has blown up with a traceback. This is because 
generators, like all iterators, can be exhausted. Unless your 
generator is infinite, you can iterate through it one time only. 
Once all values have been evaluated, iteration will stop and 
the for loop will exit. If you used next(), then instead you’ll 
get an explicit StopIteration exception.

https://realpython.com/introduction-to-python-generators/
"""



def get_odd_numbers(i):
    return range(1, i, 2)
def yield_odd_numbers(i):
    for x in range(1, i, 2):
       yield x
foo = get_odd_numbers(10)
bar = yield_odd_numbers(10)
print(foo)
# [1, 3, 5, 7, 9]
print(bar)
# <generator object yield_odd_numbers at 0x1029c6f50>
print(bar.next())
# 1
print(bar.next())
# 3

"""
As you can see, in the first case foo holds the entire list in 
memory at once. It's not a big deal for a list with 5 elements, 
but what if you want a list of 5 million? Not only is this a huge 
memory eater, it also costs a lot of time to build at the time that 
the function is called.

In the second case, bar just gives you a generator. A generator is 
an iterable--which means you can use it in a for loop, etc, but 
each value can only be accessed once. All the values are also not 
stored in memory at the same time; the generator object "remembers" 
where it was in the looping the last time you called it--this way, 
if you're using an iterable to (say) count to 50 billion, you don't 
have to count to 50 billion all at once and store the 50 billion numbers 
to count through.


"""