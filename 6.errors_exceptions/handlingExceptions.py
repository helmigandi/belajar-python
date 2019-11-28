while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")







""" Handling Exceptions

It is possible to write programs that handle selected exceptions, 
but allows the user to interrupt the program (using Control-C or 
whatever the operating system supports).

An except clause may name multiple exceptions as a parenthesized tuple, for example:
... except (RuntimeError, TypeError, NameError):
...     pass



https://docs.python.org/3/tutorial/errors.html#handling-exceptions
"""


try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

# Enter your age: 25
# Welcome, you are old enough.

""" try…except…else

 The statements inside the else block will be executed only 
 if the code inside the try block doesn’t generate an exception. 

try:
    statements # statements that can raise exceptions
except:
    statements # statements that will be executed to handle exceptions
else:
    statements # statements that will be executed if there is no exception
"""

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
finally:
    print ('There may or may not have been an exception.')

# Enter your age: 55
# There may or may not have been an exception.


""" try…except…finally

try:
    statements # statements that can raise exceptions
except:
    statements # statements that will be executed to handle exceptions
finally:
    statements # statements that will always be executed

The finally block will always be executed, regardless whether an 
exception occurrs in the try block. Finally clauses are also 
called clean-up or termination clauses, because they are usually 
used when your program crashes and you want to perform tasks such 
as closing the files or logging off the user.
"""


try:
    age=int(input('Enter your age: '))
except ValueError:
    print('Invalid value entered.')
except KeyboardInterrupt:
    print('You have interrupted the program.')    
else:
    if age >= 21:
        print('Welcome, you are old enough.')
    else:
        print('Go away, you are too young.')

# You can also handle multiple exceptions with a single except clause:
# try:
#     age=int(input('Enter your age: '))
# except (ValueError, KeyboardInterrupt):
#     print('There was an exception.')
# else:
#     if age >= 21:
#         print('Welcome, you are old enough.')
#     else:
#         print('Go away, you are too young.')



""" Catch specific exceptions

It is recommended to specify an exact exceptions that the except 
clause will catch. For example, to catch an exception that occurs 
when the user enters a non-numerical value instead of a number, 
we can catch only the built-in ValueError exception that will 
handle such event.

To see the full list of exceptions, go here:
https://docs.python.org/3.5/library/exceptions.html
"""


try:
    raise ValueError
except ValueError:
    print('There was an exception.')
# There was an exception.



""" Raise exception

You can manually throw (raise) an exception in Python with 
the keyword raise. This is usually done for the purpose of 
error-checking.

x = 5
if x < 10:
    raise ValueError('x should not be less than 10!')
"""


newChance = True

while newChance == True:
    try:
        age = int(input('Enter your age: '))
    except ValueError:
        print ('You have to enter a number!')
        try:
            startOver = int(input('To start over, enter 0. To exit, press any other key. '))
        except:
            print('OK, you do not want to start over, see you soon!')
            newChance = False
        else:
            if startOver == 0:
                newChance = True
            else:
                print('OK, you do not want to start over, see you soon!')
                newChance = False

# Enter your age: a
# You have to enter a number!
# o start over, enter 0. To exit, press any other key. 0
# Enter your age: 21


""" Nest exception handling statements

This process (called nesting) is often used in situations when 
you want to obtain the right type of user input. For example, 
if the user enters a non-numeric value instead of a number, 
you can give the user another chance to enter the right value type.

"""

try:
    print ('Press Return or Ctrl+C:')
    ignore = input()
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception')



""" Side effect of Exception Handling

Exception handling has a side effect too. Programs using 
try-except to handle exception will run slightly slower. 
Also the size of your code will also increase. 

https://www.datacamp.com/community/tutorials/exception-handling-python

"""