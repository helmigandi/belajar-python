# List comprehensions provide us with a simple way to create a 
# list based on some iterable. An iterable is something you can 
# loop over.

# [<Output Expression> for <Item> in <Iterable> if <Condition>]

# List Comprehensions is used to create a new list from an 
# existing list

# Example 1
#
print("-------------------")
lst = ['Acer', 'Asus', 'Lenovo', 'HP']
# regular function
def starts_with_a(lst):
    valids = []
 
    for word in lst:
        if word[0].lower() == 'a':
            valids.append(word)
 
    return valids
 
# list comprehension
lst_comp = [word for word in lst if word[0].lower() == 'a']

print('starts_with_a: {}'.format(starts_with_a(lst)))
print('list_comprehension: {}'.format(lst_comp))

#starts_with_a: ['Acer', 'Asus']
# list_comprehension: ['Acer', 'Asus']

# Example 2
#
print("-------------------")
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])# [-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])# [0, 2, 4]
# apply a function to all the elements
print([abs(x) for x in vec])# [4, 2, 0, 2, 4]
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# List comprehensions can contain complex expressions and nested functions:
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# Example 3
#
print("-------------------")
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num) # Output: [2, 3, 4]

list_c = [1, 2, 3]
list_d = [2, 7]
different_num = [(c, d) for c in list_c for d in list_d if c != d]
print(different_num) # Output: [(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]

list_e = [1, 2, 3]
square_cube_list = [ [e**2, e**3] for e in list_e]
print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]

# Example 4
#
print("-------------------")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
# list comprehension
print([[row[i] for row in matrix] for i in range(4)])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# regular loop
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# In the real world, you should prefer built-in functions 
# to complex flow statements.
print(list(zip(*matrix)))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

