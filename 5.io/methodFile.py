# To read a file’s contents, call f.read()
# f.readline() reads a single line from the file
# 

f = open('workfile.txt', 'r+')
# print(f.read())
# print(f.readline())
for line in f:
    print(line, end='')
# This is the first line of the file.
# Second line of the file

# f.write(string) writes the contents of string to the file
f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)

print(f.read(3))