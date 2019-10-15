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


# Example 4
#
print("-------------------")
# Assume that we have a few friends over, and that we have 
# decided to play several games of Scrabble. 
# Being Python programmers, we have stored our scores 
# in a dictionary:

scores={'Reuven':[300, 250, 350, 400], 
'Atara':[200, 300, 450, 150], 
'Shikma':[250, 380, 420, 120],
'Amotz':[100, 120, 150, 180] }

def average(scores):  
    return sum(scores) / len(scores)

print({ name : average(score)
    for name, score in scores.items() })
# {'Amotz': 137, 'Atara': 275, 'Reuven': 325, 'Shikma': 292}
print(average([ one_score  
              for one_player_scores in scores.values()  
              for one_score in one_player_scores ]))
# 257

print([ one_score      
      for one_player_scores in scores.values()     
      for one_score in one_player_scores
      if one_score > 200])
# [300, 250, 350, 400, 300, 450, 250, 380, 420]

#If I want to put these above-200 scores into a CSV file 
# of some sort
print(','.join([ str(one_score)  
               for one_player_scores in scores.values() 
               for one_score in one_player_scores  
               if one_score > 200]))
# '300,250,350,400,300,450,250,380,420'


# Example 5
#
print("-------------------")
rooms = [[{'age': 14, 'hobby': 'horses', 'name': 'Andi'},  
          {'age': 12, 'hobby': 'piano', 'name': 'Bobby'},  
          {'age': 9, 'hobby': 'chess', 'name': 'Chintia'}],  
         [{'age': 15, 'hobby': 'programming', 'name': 'Dara'}, 
          {'age': 17, 'hobby': 'driving', 'name': 'Endang'}],  
         [{'age': 45, 'hobby': 'writing', 'name': 'Faris'},  
          {'age': 43, 'hobby': 'chess', 'name': 'Gea'}]]

print([ person['name']      
       for room in rooms
       for person in room ])
# ['Andi','Bobby','Chintia','Dara','Endang','Faris','Gea']

print([ person['name']  
      for room in rooms  
      for person in room  
      if person['hobby'] == 'chess' ])
# ['Chintia', 'Gea']