# Features of a Python Dictionary
# 1. The key of a Python dictionary cannot be changed.
# 2. The value of a key can be changed.
# 3. The ordering is not significant. The order in which you have 
#    entered the items in the dictionary, may not be the same 
#    order in which the items are returned.


# Creating Dictionaries
my_dict = {}
my_other_dict = dict()
my_other_other_dict = {1: 'one', 2: 'two', 3: 'three'}


# Example 1
print("--------------------")
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])
# 4098
del tel['sape']
tel['irv'] = 4127
print(tel)
# {'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))
# ['jack', 'guido', 'irv']
print(sorted(tel))
# ['guido', 'irv', 'jack']
print('guido' in tel)
# True
print('jack' not in tel)
# False


print("--------------------")
# The dict() constructor builds dictionaries 
# directly from sequences of key-value pairs:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# In addition, dict comprehensions can be used to create 
# dictionaries from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier 
# to specify pairs using keyword arguments:
print(dict(sape=4139, guido=4127, jack=4098))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}


print("--------------------")
MLB_team = {
        'Colorado' : 'Rockies',
        'Boston'   : 'Red Sox',
        'Minnesota': 'Twins',
        'Milwaukee': 'Brewers',
        'Seattle'  : 'Mariners'
    }
# Accessing Dictionary Values
MLB_team['Minnesota']   # 'Twins'
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
# 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 
# 'Seattle': 'Mariners', 'Kansas City': 'Royals'}

MLB_team['Seattle'] = 'Seahawks'    # update
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
# 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 
# 'Seattle': 'Seahawks', 'Kansas City': 'Royals'}

del MLB_team['Seattle'] # delete entry
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
# 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 
# 'Kansas City': 'Royals'}


print("--------------------")
# Building a Dictionary Incrementally
# as shown above, is fine if you know all the keys and values 
# in advance. But what if you want to build a dictionary on 
# the fly?

person = {}
type(person)
# <class 'dict'>

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)

print(person['children'])
# ['Ralph', 'Betty', 'Joey']
print(person['children'][-1])
# 'Joey'
print(person['pets']['cat'])
# 'Sox'


print("--------------------")
d = {'a': 10, 'b': 20, 'c': 30}
# Built-in Dictionary Methods

# .clear()
d.clear()
print(d) # {}

# .get(<key>[, <default>])
print(d.get('b'))
# 20
print(d.get('z'))
# None
# If <key> is not found and the optional <default> 
# argument is specified, that value is returned 
# instead of None:
print(d.get('z', -1))
# -1
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
# 'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# 'I am bringing 0 eggs.'


# .items()
# Returns a list of key-value pairs in a dictionary.
d = {'a': 10, 'b': 20, 'c': 30}
list(d.items())
# [('a', 10), ('b', 20), ('c', 30)]
list(d.items())[1][0]
# 'b'
list(d.items())[1][1]
# 20

# .keys()
# Returns a list of keys in a dictionary.
list(d.keys())
# ['a', 'b', 'c']
for k, v in d.items():
        print('Key: ' + k + ' Value: ' + str(v))

# .values()
# Returns a list of values in a dictionary.
list(d.values())
# [10, 20, 30]

# .pop(<key>[, <default>])
# Removes a key from a dictionary, if it is present, 
# and returns its value.
d.pop('b')
# 20
d.pop('z', -1)
# -1

# .popitem()
# d.popitem() removes a random
d.popitem()
# ('c', 30)
d
# {'a': 10, 'b': 20}

# .update(<obj>)
# Merges a dictionary with another dictionary or with an iterable 
# of key-value pairs.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
d1
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}
d1.update([('b', 200), ('d', 400)]) # or d1.update(b=200, d=400)
d1
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}

# setdefault()
# You’ll often have to set a value in a dictionary for a certain 
# key only if that key does not already have a value. 
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# 'black'
spam
# {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')
# 'black'



print("--------------------")
# Operators and Built-in Functions
MLB_team = {
     'Colorado' : 'Rockies',
     'Boston'   : 'Red Sox',
     'Minnesota': 'Twins',
     'Milwaukee': 'Brewers',
     'Seattle'  : 'Mariners'
}
'Milwaukee' in MLB_team
# True
'Toronto' in MLB_team
# False
'Toronto' not in MLB_team
# True



# Dictionary Comprehension
# dict_variable = {key:value for (key,value) in dictonary.items()}

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)