# Single line function - called anonymous functions as they dont have
# names. They are expressions not statements.
# This function returns the sum of its two arguments: lambda a, b: a+b.

g = lambda z, y: z * y
print(g(7, 8))
# 14

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
# 6
print(high_ord_func(2, lambda x: x + 3))
# 7

print("-" * 50)

# Using sorted function with lambda
# sorted(iterable, key)
# key is optional

my_list = ['one', 'two', 'three', 'four', 'five']
print(sorted(my_list))
print(sorted(my_list, key=lambda x: x[-1])) # return last value of x

another_list = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(sorted(another_list)) # sorted based on these first numerical
print(sorted(another_list, key=lambda x: x[1])) # sorted the second value in the argument

print("-" * 50)

# regular function
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
 
 
# lambda function
even = lambda x: x % 2 == 0# results
print('is_even(4): {}'.format(is_even(4)))
print('is_even(3): {}'.format(is_even(3)))
print('even(4): {}'.format(even(4)))
print('even(3): {}'.format(even(3)))

# >>> is_even(4): True
# >>> is_even(3): False
# >>> even(4): True
# >>> even(3): False