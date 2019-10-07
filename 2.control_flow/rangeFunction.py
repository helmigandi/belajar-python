# If you do need to iterate over a sequence of numbers, 
# the built-in function range() comes in handy. 

for i in range(5):
    print(i)
print()
# 0
# ..
# 5

# It is possible to let the range start at another number, 
# or to specify a different increment (even negative; 
# sometimes this is called the ‘step’):
# range(5, 10)
#    5, 6, 7, 8, 9

# range(0, 10, 3)
#    0, 3, 6, 9

# range(-10, -100, -30)
#   -10, -40, -70

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 0 Mary
# 1 had
# ...

# In most such cases, however, it is convenient to use
# the enumerate() function.