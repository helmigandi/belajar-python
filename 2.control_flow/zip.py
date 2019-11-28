""" Zip()

Returns an iterator of tuples.
From a data scientists perspective, it enables you to iterate 
over two or more lists at the same time. This can come in handy 
when working with dates and times.

For the example, I’ve decided to compare a week of sales date 
from some fictional company and fictional regions:

ou can apply the same logic for iterating over 3 arrays at the 
same time, you would only need to add ‘s3’ and some other list 
name into brackets.

"""

sales_north = [350, 287, 550, 891, 241, 653, 882]
sales_south = [551, 254, 901, 776, 105, 502, 976]
for s1, s2 in zip(sales_north, sales_south):
    print(s1 — s2)

# >>> -201
#     33
#     -351
#     115
#     136
#     151
#     -94

""" Using zip() in Python

Python’s zip() function is defined as zip(*iterables). The 
function takes in iterables as arguments and returns an iterator. 
This iterator generates a series of tuples containing elements 
from each iterable. zip() can accept any type of iterable, such 
as files, lists, tuples, dictionaries, sets, and so on.

"""

""" Passing n Arguments

Here, you use zip(numbers, letters) to create an iterator that 
produces tuples of the form (x, y). In this case, the x values 
are taken from numbers and the y values are taken from letters. 
Notice how the Python zip() function returns an iterator. To 
retrieve the final list object, you need to use list() to consume 
the iterator.

"""

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zipped  # Holds an iterator object
# <zip object at 0x7fa4831153c8>
type(zipped)
# <class 'zip'>
list(zipped)
# [(1, 'a'), (2, 'b'), (3, 'c')]

"""
If you’re working with sequences like lists, tuples, or strings, 
then your iterables are guaranteed to be evaluated from left to 
right. This means that the resulting list of tuples will take the 
form [(numbers[0], letters[0]), (numbers[1], letters[1]),..., 
(numbers[n], letters[n])]. However, for other types of iterables 
(like sets), you might see some weird results:


This means that the tuples returned by zip() will have elements 
that are paired up randomly. If you’re going to use the Python 
zip() function with unordered iterables like sets, then this is 
something to keep in mind.

"""
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
list(zip(s1, s2))
# [(1, 'a'), (2, 'c'), (3, 'b')]

# Passing No Arguments
zipped = zip()
zipped
# <zip object at 0x7f196294a488>
list(zipped)
# []

# Passing One Argument
a = [1, 2, 3]
zipped = zip(a)
list(zipped)
# [(1,), (2,), (3,)]

# three iterables:
integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
list(zipped)
# [(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]

# Calculating in Pairs
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')
# Total profit: 5200.0
# Total profit: 5100.0
# Total profit: 4800.0

"""

https://realpython.com/python-zip-function/
https://towardsdatascience.com/3-essential-python-skills-for-data-scientists-b642a1397ae3

"""