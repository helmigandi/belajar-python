# Tuples
# Tuples are defined by enclosing the elements in parentheses (())
# Tuples are immutable.

# Tuples are immutable, and usually contain a heterogeneous 
# sequence of elements that are accessed via unpacking 
# or indexing (or even by attribute in the case of namedtuples). 

# Lists are mutable, and their elements are usually homogeneous 
# and are accessed by iterating over the list.

t = 12345, 54321, 'hello!'
print(t[0])
# 12345
print(t)
# (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
([1, 2, 3], [3, 2, 1])


# A special problem is the construction of tuples 
# containing 0 or 1 items:
# Empty tuples are constructed by an empty pair of parentheses; 
# a tuple with one item is constructed by following a value with 
# a comma.
print("-------------------")
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))# 0
print(len(singleton))# 1
print(singleton)
# ('hello',)

# Tuple Packing and Unpacking
print("-------------------")
b = ("Bob", 19, "CS")       # tuple packing
(name, age, studies) = b    # tuple unpacking
print(name) # 'Bob'
print(age) # 19
print(studies) # 'CS'

awesomeTuple = ('paladin', 'rogue', 'priest', 'warrior', 'druid')
belkas, gorkin, landril, maxilum, ferral = awesomeTuple
print(belkas) # 'paladin'
print(maxilum) # 'warrior'

# We can create lists of tuples. This is great for 
# working with stuff like log files.
print("-------------------")
logs = [
    ('HTTP_OK', 'GET /index.html'),
    ('HTTP_NOT_FOUND', 'GET /index.htmll')
    ]
errorCount = 0
for log in logs:
    status, message = log
    if status is not 'HTTP_OK':
        errorCount += 1
print(errorCount)
# errorCount
# 1