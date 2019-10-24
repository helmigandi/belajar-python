# open() returns a file object, and is most commonly used 
# with two arguments: open(filename, mode).

# mode can be 'r' when the file will only be read
# 'w' for only writing (an existing file with the same name will 
# be erased)
# 'a' opens the file for appending; any data written to the file 
# is automatically added to the end. 
# 'r+' opens the file for both reading and writing. 
# 'b' appended to the mode opens the file in binary mode: 
# now the data is read and written in the form of bytes objects. 
# This mode should be used for all files that don’t contain text.


f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()
# We can check that the file has been automatically closed.
f.closed
# True

# If you’re not using the with keyword, then you should call 
# f.close() to close the file and immediately free up any 
# system resources used by it.
