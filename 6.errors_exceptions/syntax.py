
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax

""" Syntax Errors

The parser repeats the offending line and displays a little 
‘arrow’ pointing at the earliest point in the line where the 
error was detected.

he error is caused by (or at least detected at) the token 
preceding the arrow: in the example, the error is detected at 
the function print(), since a colon (':') is missing before it.

File name and line number are printed so you know where to 
look in case the input came from a script.


"""