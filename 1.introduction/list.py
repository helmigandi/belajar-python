# LIST
# Python knows a number of compound data types, 
# used to group together other values. The most 
# versatile is the list, which can be written 
# as a list of comma-separated values (items) 
# between square brackets. Lists might contain 
# items of different types, but usually the items 
# all have the same type.

squares = [1, 4, 9, 16, 25]
print(squares)
# [1, 4, 9, 16, 25]
print(squares[0])  # indexing returns the item
# 1
print(squares[-1])
# 25
print( squares[-3:])  # slicing returns a new list
# [9, 16, 25]
print( squares[:]) # The following slice returns a new (shallow) copy of the list:
# [1, 4, 9, 16, 25]
print( squares + [36, 49, 64, 81, 100])
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("================================")

# Unlike strings, which are immutable, lists are a mutable type, 
# i.e. it is possible to change their content:

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
# 64
cubes[3] = 64  # replace the wrong value
print(cubes)
# [1, 8, 27, 64, 125]

# You can also add new items at the end of the list, by using 
# the append() method (we will see more about methods later):

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
# [1, 8, 27, 64, 125, 216, 343]

print("================================")

# Assignment to slices is also possible, and this can even 
# change the size of the list or clear it entirely:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
print(letters)
# ['a', 'b', 'f', 'g']

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
# []

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters))
# 4

print("================================")

# It is possible to nest lists (create lists containing 
# other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
# ['a', 'b', 'c']
print(x[0][1])
# 'b'
