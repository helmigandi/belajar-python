
#f-String
# To use formatted string literals, begin a string with f or F 
# before the opening quotation mark or triple quotation mark. 
# Inside this string, you can write a Python expression between 
# { and } characters that can refer to variables or literal values.
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
# 'Results of the 2016 Referendum'

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

# Passing an integer after the ':' will cause that field to be a 
# minimum number of characters wide. This is useful for making 
# columns line up.
table = {'Bambang': 4127123, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
















# str.format()
# The str.format() method of strings requires more manual effort. 
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
#'42572654 YES votes  49.67%'

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam

print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
# The story of Bill, Manfred, and Georg.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678


# Old string formatting
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.



# str.format() and Old string formatting Isn’t Great
# https://realpython.com/python-f-strings/
