# The del statement

# There is a way to remove an item from a list given its index 
# instead of its value.
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# [1, 66.25, 333, 333, 1234.5]

del a[2:4]
print(a)
# [1, 66.25, 1234.5]

del a[:]
print(a)
# []

# del can also be used to delete entire variables:
del a
# Untuk menghapus variabel a
