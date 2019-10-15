fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# list.count(x)
# Return the number of times x appears in the list.
print("-"*5+"Count"+"-"*5)
print(fruits.count('apple'))
# 2
print(fruits.count('tangerine'))
# 0


# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item 
# whose value is equal to x.
print("-"*5+"Index"+"-"*5)
print(fruits.index('banana'))
# 3
print(fruits.index('banana', 4))  # Find next banana starting a position 4
# 6


# list.reverse()
# Reverse the elements of the list in place.
print("-"*5+"Reverse"+"-"*5)
fruits.reverse()
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']


# list.append(x)
# Add an item to the end of the list.
print("-"*5+"Append"+"-"*5)
fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']


# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used 
# for sort customization, see sorted() for their explanation).
print("-"*5+"Sort"+"-"*5)
fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']


# list.pop([i])
# Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list.
print("-"*5+"Pop"+"-"*5)
print(fruits.pop())
print(fruits)
# 'pear'

# list.extend(iterable)
# Extend the list by appending all the items from the iterable.
print("-"*5+"Extend, Append & Insert"+"-"*5)
x = [1, 2, 3]
x.extend([4, 5])
print (x) # gives you: [1, 2, 3, 4, 5]
# append: Appends object at the end.
x = [1, 2, 3]
x.append([4, 5])
print (x) # gives you: [1, 2, 3, [4, 5]]
# Insert an item at a given position.
x = [1, 2, 3]
x.insert(1, [4, 5])
print (x) # gives you: [1, 2, 3, [4, 5]]


# list.remove(x)
# Remove the first item from the list whose value is equal to x.
print("-"*5+"Remove"+"-"*5)
fruits.remove('kiwi')
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'orange']
# Remove the same fruits
for x in range(fruits.count("banana")):
    fruits.remove("banana")
print(fruits)

