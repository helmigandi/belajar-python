# Python can be enclosed in single quotes ('...') or double quotes 
# ("...") with the same result

print( 'spam eggs')  # single quotes
# 'spam eggs'
print( 'doesn\'t')  # use \' to escape the single quote...
# "doesn't"
print( "doesn't")  # ...or use double quotes instead
# "doesn't"
print( '"Yes," they said.')
# '"Yes," they said.'
print( "\"Yes,\" they said.")
# '"Yes," they said.'
print( '"Isn\'t," they said.')
# '"Isn\'t," they said.'

print()

print( '"Isn\'t," they said.')
# '"Isn\'t," they said.'
print('"Isn\'t," they said.')
# "Isn't," they said.
s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), \n produces a new line
# First line.
# Second line.

print("===============================")

# If you don’t want characters prefaced by \ to be interpreted
# as special characters, you can use raw strings by adding an r 
# before the first quote:

print('C:\some\name')  # here \n means newline!
# C:\some
# ame
print(r'C:\some\name')  # note the r before the quote
# C:\some\name

print()

# String literals can span multiple lines. One way is 
# using triple-quotes: """...""" or '''...'''.

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print("===============================")

# Strings can be concatenated (glued together) with the + operator, 
# and repeated with *:
print(3 * 'un' + 'ium')
# 'unununium'

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
# 'Put several strings within parentheses to have them joined together.'

# If you want to concatenate variables or a variable and a literal, use +:
prefix = 'Py'
print(prefix + 'thon')
#'Python'

print("===============================")

# Strings can be indexed (subscripted), with 
# the first character having index 0.

word = 'Python'
print(word[0])  # character in position 0
# 'P'
print(word[5])  # character in position 5
# 'n'
print(word[-1]) # last character
# 'n'
print(word[-2]) # second-last character
# 'o'
print(word[-6])
# 'P'

print("===============================")

# In addition to indexing, slicing is also supported.
print( word[0:2])  # characters from position 0 (included) to 2 (excluded)
# 'Py'
print( word[2:5])  # characters from position 2 (included) to 5 (excluded)
# 'tho'

print( word[:2] + word[2:])
# 'Python'
print( word[:4] + word[4:])
# 'Python'

print( word[:2])   # character from the beginning to position 2 (excluded)
# 'Py'
print( word[4:])   # characters from position 4 (included) to the end
# 'on'
print( word[-2:])  # characters from the second-last (included) to the end
# 'on'
print()

# If you need a different string, you should create a new one:
print('J' + word[1:])
# 'Jython'
print(word[:2] + 'py')
# 'Pypy'

# The built-in function len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
print(len(s))
# 34

print('%(language)s has %(number)03d quote types.' %
       {'language': "Python", "number": 2})
# Python has 002 quote types.


# You can see others format string at 
# https://docs.python.org/3/tutorial/introduction.html#strings