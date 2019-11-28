""" Functions in Python

You use functions in programming to bundle a set of instructions 
that you want to use repeatedly or that, because of their 
complexity, are better self-contained in a sub-program and 
called when needed. 

That means that a function is a piece of code 
written to carry out a specified task.
"""


class Door:
    def open(self):
        print("hello stranger")

def knock_door():
    a_door = Door()
    Door.open(a_door)

knock_door()

""" Functions vs Methods

The example given shows you a class called "Door" which has a 
method or action called "open", it is called a method because 
it was declared inside a class. There is another portion of code 
with "def" just below which defines a function, it is a function 
because it is not declared inside a class, this function calls 
the method we defined inside our class as you can see and finally 
the function is being called by itself.

As you can see you can call a function anywhere but if you want 
to call a method either you have to pass a new object of the same 
type as the class the method is declared (Class.method(object)) or 
you have to invoke the method inside the object (object.Method()), 
at least in python.

Simple way to remember:

    Function → Free (Free means not belong to an object or class)
    Method → Member (A member of an object or class)

https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function
"""

# Define a function `plus()`
def plus(a,b):
    return a + b
  
# Create a `Summation` class
class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        return self.contents 

# Instantiate `Summation` class to call `sum()`
sumInstance = Summation()
print(sumInstance.sum(1,2))

""" Parameters vs Arguments

Parameters are the names used when defining a function or a method, 
and into which arguments will be mapped.

Consider the following example and look back to the above, 
you pass two arguments to the sum() method of the Summation class, 
even though you previously defined three parameters, namely, self, 
a and b.

Instance = class(arguments)

An object is created using the constructor of the class. 
This object will then be called the instance of the class.

self represents the instance of the class. 
By using the “self” keyword we can access the attributes 
and methods of the class in python.
"""

lass car(): 
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 
          
# both objects have different self which  
# contain their attributes 
audi = car("audi a4", "blue") 
ferrari = car("ferrari 488", "green") 
  
audi.show()     # same output as car.show(audi) 
ferrari.show()  # same output as car.show(ferrari) 
  
# Behind the scene, in every instance method  
# call, python sends the instances also with 
# that method call like car.show(audi) 


""" How To Define A Function: User-Defined Functions (UDFs)

The four steps to defining a function in Python are the following:

    1. Use the keyword def to declare the function and follow this up with the function name.
    2. Add parameters to the function: they should be within the parentheses of the function. End your line with a colon.
    3. Add statements that the functions should execute.
    4. End your function with a return statement if the function should output something. Without the return statement, your function will return an object None.

"""

def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World") 
  return 
  
hello()


""" The return Statement

Note that as you’re printing something in your UDF hello(), 
you don’t really need to return it. 

""" 
def no_return(x,y):
    c = x + y

res = no_return(4,5)
print(res)
# none

def return_sum(x,y):
    c = x + y
    return c

res = return_sum(4,5)
print(res)
# 9

def hello():
  print("Hello World") 
  return("hello")

def hello_noreturn():
  print("Hello World")
  
# Multiply the output of `hello()` with 2 
hello() * 2

# (Try to) multiply the output of `hello_noreturn()` with 2 
# hello_noreturn() * 2
# TypeError

def plus(a,b):
  sum = a + b
  return (sum, a)

# Call `plus()` and unpack variables 
sum, a = plus(3,4)

# Print `sum()`
print(sum)
# 7


""" Using main() as a Function

When your script is run by passing it as a command to the Python 
interpreter,

    python myscript.py

all of the code that is at indentation level 0 gets executed.
Functions and classes that are defined are, well, defined, 
but none of their code gets run. Unlike other languages, 
there's no main() function that gets run automatically - 
the main() function is implicitly all the code at the top level.

In this case, the top-level code is an if block. __name__ is a 
built-in variable which evaluates to the name of the current 
module. However, if a module is being run directly (as in 
myscript.py above), then __name__ instead is set to the 
string "__main__". Thus, you can test whether your script is 
being run directly or being imported by something else by testing

    if __name__ == "__main__":
        ...

If your script is being imported into another module, 
its various function and class definitions will be imported 
and its top-level code will be executed, but the code in the 
then-body of the if clause above won't get run as the condition 
is not met. As a basic example, consider the following two scripts:

# file one.py
    def func():
        print("func() in one.py")

    print("top-level in one.py")

    if __name__ == "__main__":
        print("one.py is being run directly")
    else:
        print("one.py is being imported into another module")

# file two.py
    import one

    print("top-level in two.py")
    one.func()

    if __name__ == "__main__":
        print("two.py is being run directly")
    else:
        print("two.py is being imported into another module")

Now, if you invoke the interpreter as

    python one.py

The output will be

    top-level in one.py
    one.py is being run directly

If you run two.py instead:

    python two.py

You get:

    top-level in one.py
    one.py is being imported into another module
    top-level in two.py
    func() in one.py
    two.py is being run directly



including a main() function in your Python program can 
be handy to structure your code logically - all of the 
most important components are contained within this main() 
function.

# Define `main()` function
    def main():
        hello()
        print("This is a main function")

    main()

However, as it stands now, the code of your main() function 
will be called when you import it as a module. To make sure 
that this doesn’t happen, you call the main() function 
when __name__ == '__main__'.

# Define `main()` function
    def main():
        hello()
        print("This is a main function")
  
# Execute `main()` function 
    if __name__ == '__main__':
        main()

"""



"""  Constructors in Python (__init__)

Constructors are generally used for instantiating an object.
The task of constructors is to initialize(assign values) to 
the data members of the class when an object of class is created.
In Python the __init__() method is called the constructor and 
is always called when an object is created.

Syntax of constructor declaration :

def __init__(self):
    # body of the constructor

Types of constructors :

1. default constructor :
The default constructor is simple constructor which doesn’t 
accept any arguments.It’s definition has only one argument which 
is a reference to the instance being constructed.
    
2. parameterized constructor :
constructor with parameters is known as parameterized constructor.
The parameterized constructor take its first argument as a 
reference to the instance being constructed known as self and the rest 
of the arguments are provided by the programmer.

Example of default constructor :
class GeekforGeeks: 
	geek = "" 

	# default constructor 
	def __init__(self): 
		self.geek = "GeekforGeeks"

	# a method for printing data members 
	def print_Geek(self): 
		print(self.geek) 


# creating object of the class 
obj = GeekforGeeks() 

# calling the instance method using the object obj 
obj.print_Geek() 

Output: GeekforGeeks


Example of parameterized constructor :

class Addition: 
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor 
	def __init__(self, f, s): 
		self.first = f 
		self.second = s 
	
	def display(self): 
		print("First number = " + str(self.first)) 
		print("Second number = " + str(self.second)) 
		print("Addition of two numbers = " + str(self.answer)) 

	def calculate(self): 
		self.answer = self.first + self.second 

# creating object of the class 
# this will invoke parameterized constructor 
obj = Addition(1000, 2000) 

# perform Addition 
obj.calculate() 

# display result 
obj.display() 

Output :
First number = 1000
Second number = 2000
Addition of two numbers = 3000

"""