# Sets
# Sets are unordered
# Set elements are unique. Duplicate elements are not allowed.
# A set itself may be modified, but the elements contained in 
# the set must be of an immutable type.


print("--------------------")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)                # fast membership testing
# True
print('crabgrass' in basket)
False


print("--------------------")
# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
print(a - b)                              # letters in a but not in b / Difference
# {'r', 'd', 'b'}
print(a | b)                              # letters in a or b or both / Union
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # letters in both a and b / Intersection  
# {'a', 'c'}
print(a ^ b)                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}

# Set comprehensions
z = {x for x in 'abracadabra' if x not in 'abc'}
print(z) # {'r', 'd'}


print("--------------------")
# You can initialize an empty set by using set()
emptySet = set()
# To intialize a set with values, you can pass in a list to set()
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
# Sets containing values can also be initialized by using curly braces.
dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
print(emptySet)
print(dataScientist)
print(dataEngineer)


print("--------------------")
# Add and Remove Values from Sets

# Initialize set with values
graphicDesigner = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere', 'Bridge'}
graphicDesigner.add('Illustrator')      # method add to add a value to a set
# graphicDesigner.add(['Powerpoint', 'Blender'])    # TypeError
print(graphicDesigner) 

# Remove Values from a Set
graphicDesigner.remove('Illustrator')   # the remove method to remove a value from a set.
graphicDesigner.discard('Premiere')     # the discard method to remove a value from a set.
print(graphicDesigner.pop())            # the pop method to remove and return an arbitrary value from a set.
print(graphicDesigner) 
# The benefit of this approach over the remove method 
# is if you try to remove a value that is not part of the set, 
# you will not get a KeyError. 

# Remove All Values from a Set
graphicDesigner.clear()

# Iterate through a Set
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}

for skill in dataScientist:
    print(skill)

# Transform Set into Ordered Values
# the sorted function which outputs a list that is ordered.
print(sorted(dataScientist, reverse = True))
print(dataScientist)

# Remove Duplicates from a List
print(list(set([1, 2, 3, 1, 7])))


print("--------------------")
# Set Operation Methods

dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

# union
print(dataScientist.union(dataEngineer))# dataScientist | dataEngineer
# {'Git', 'SQL', 'R', 'SAS', 'Hadoop', 'Scala', 'Tableau', 'Java', 'Python'}

# intersection
print(dataScientist.intersection(dataEngineer))# dataScientist & dataEngineer
# {'Git', 'Python', 'SQL'}

# difference
print(dataScientist.difference(dataEngineer))# dataScientist - dataEngineer
# {'SAS', 'Tableau', 'R'}

# symmetric_difference
print(dataScientist.symmetric_difference(dataEngineer))# dataScientist ^ dataEngineer
# {'SAS', 'Tableau', 'Java', 'R', 'Hadoop', 'Scala'}

print("--------------------")
# Set Comprehension
print({skill for skill in ['GIT', 'PYTHON', 'SQL'] if skill not in {'GIT', 'PYTHON', 'JAVA'}})

print("--------------------")       
# Membership Tests
# One of the main advantages of using sets in Python is that they are highly optimized for membership tests.

# Initialize a set
possibleSet = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS', 'Java', 'Spark', 'Scala'}

# Membership test
print('Python' in possibleSet)
# Since possibleSet is a set and the value 'Python' is a value 
# of possibleSet, this can be denoted as 'Python' ∈ possibleSet.

# If you had a value that wasn't part of the set, like 
# 'Fortran', it would be denoted as 'Fortran' ∉ possibleSet.

print("--------------------")       
# Subset
possibleSkills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}
print(mySkills.issubset(possibleSkills))
# If every value of the set mySkills is also a value of the 
# set possibleSkills, then mySkills is said to be a subset of 
# possibleSkills, mathematically written mySkills ⊆ possibleSkills.

print("--------------------")       
# Frozensets
# You have have encountered nested lists and tuples.
# Nested Lists and Tuples
nestedLists = [['the', 12], ['to', 11], ['of', 9], ['and', 7], ['that', 6]]
nestedTuples = (('the', 12), ('to', 11), ('of', 9), ('and', 7), ('that', 6))
# nestedSets = set([set()]) -> Error

# This is one situation where you may wish to use a frozenset. 
# A frozenset is very similar to a set except that a frozenset 
# is immutable.
# Initialize a frozenset
immutableSet = frozenset()
nestedSets = set([frozenset()])
print(nestedSets)
# It is important to keep in mind that a major disadvantage 
# of a frozenset is that since they are immutable, it means 
# that you cannot add or remove values.
