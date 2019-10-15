# Nested List Comprehensions are nothing but a 
# list comprehension within another list comprehension 
# which is quite similar to nested for loops.

# Example 1
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


# Example 2
#
print("-------------------")

# 2-D List 
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
  
# Nested List Comprehension to flatten a given 2-D matrix 
flatten_matrix = [val for sublist in matrix for val in sublist] 
  
print(flatten_matrix) 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Example 3
#
print("-------------------")

# 2-D List of planets 
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
flatten_planets = [] 
  
for sublist in planets: 
    for planet in sublist: 
          
        if len(planet) < 6: 
            flatten_planets.append(planet) 
          
print(flatten_planets) 

# 2-D List of planets 
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
# Nested List comprehension with an if condition 
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6] 
          
print(flatten_planets) 
