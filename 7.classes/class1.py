""" Python Classes and Objects

A class is a user-defined blueprint or prototype from which 
objects are created. Classes provide a means of bundling data 
and functionality together.

Some points on Python class:

    1. Classes are created by keyword class.
    2. Attributes are the variables that belong to class.
    3. Attributes are always public and can be accessed 
       using dot (.) operator. Eg.: Myclass.Myattribute

"""


""" Class Objects

An Object is an instance of a Class. A class is like a blueprint 
while an instance is a copy of the class with actual values. 
It’s not an idea anymore, it’s an actual dog, like a dog of 
breed pug who’s seven years old. 

An object consists of :

    State : It is represented by attributes of an object. 
    It also reflects the properties of an object.
    Example -> Breed, Age, Color

    Behavior : It is represented by methods of an object. 
    It also reflects the response of an object with other objects.
    Example -> Bark, Sleep, eat

    Identity : It gives a unique name to an object and enables 
    one object to interact with other objects.
    Example -> Name of dog

"""


""" Declaring Objects (Also called instantiating a class)

When an object of a class is created, the class is said to be 
instantiated. All the instances share the attributes and the 
behavior of the class. But the values of those attributes, i.e. 
the state are unique for each object. A single class may have 
any number of instances.

"""
# Python program to 
# demonstrate instantiating 
# a class   
class Dog:  
      
    # A simple class 
    # attribute 
    attr1 = "mamal"
    attr2 = "dog"
  
    # A sample method   
    def fun(self):  
        print("I'm a", self.attr1) 
        print("I'm a", self.attr2) 
  
# Driver code 
# Object instantiation 
Rodger = Dog() 
  
# Accessing class attributes 
# and method through objects 
print(Rodger.attr1) 
Rodger.fun() 

# Output:
# mamal
# I'm a mamal
# I'm a dog

""" The self

1. Class methods must have an extra first parameter in method 
definition. We do not give a value for this parameter when we 
call the method, Python provides it.
2. If we have a method which takes no arguments, then we still 
have to have one argument.
3. This is similar to this pointer in C++ and this reference in Java.

When we call a method of this object as myobject.method(arg1, arg2), 
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2)
– this is all the special self is about.

"""

""" __init__ method

The __init__ method is similar to constructors in C++ and Java. 
Constructors are used to initialize the object’s state. Like 
methods, a constructor also contains collection of statements
(i.e. instructions) that are executed at time of Object creation. 
It is run as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do 
with your object.

"""

# A Sample class with init method  
class Person:  
    
    # init method or constructor   
    def __init__(self, name):  
        self.name = name  
    
    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  
    
p = Person('Nikhil')  
p.say_hi()  

# Output:
# Hello, my name is Nikhil

""" Class and Instance Variables

Instance variables are for data unique to each instance and class 
variables are for attributes and methods shared by all instances 
of the class. Instance variables are variables whose value is 
assigned inside a constructor or method with self whereas class 
variables are variables whose value is assigned in the class.

"""
# Defining instance varibale using constructor.

# Python program to show that the variables with a value   
# assigned in class declaration, are class variables and  
# variables inside methods and constructors are instance  
# variables.  
     
# Class for Computer Science Student  
class Dog:  
    
    # Class Variable  
    animal = 'dog'             
    
    # The init method or constructor  
    def __init__(self, breed, color):  
      
        # Instance Variable      
        self.breed = breed 
        self.color = color         
     
# Objects of CSStudent class  
Rodger = Dog("Pug", "brown")  
Buzo = Dog("Bulldog", "black")  
  
print('Rodger details:')    
print('Rodger is a', Rodger.animal)  
print('Breed: ', Rodger.breed) 
print('Color: ', Rodger.color) 
  
print('\nBuzo details:')    
print('Buzo is a', Rodger.animal)  
print('Breed: ', Buzo.breed) 
print('Color: ', Buzo.color) 
  
# Class variables can be accessed using class  
# name also  
print("\nAccessing class variable using class name") 
print(Dog.animal)         

# Output:

# Rodger details:
# Rodger is a dog
# Breed:  Pug
# Color:  brown

# Buzo details:
# Buzo is a dog
# Breed:  Bulldog
# Color:  black

# Accessing class variable using class name
# dog

# Defining instance variable using normal method.

# Python program to show that we can create   
# instance variables inside methods  
     
# Class for Computer Science Student  
class Dog:  
        
    # Class Variable  
    animal = 'dog'      
        
    # The init method or constructor  
    def __init__(self, breed):  
            
        # Instance Variable  
        self.breed = breed              
    
    # Adds an instance variable   
    def setColor(self, color):  
        self.color = color  
        
    # Retrieves instance variable      
    def getColor(self):      
        return self.color     
    
# Driver Code  
Rodger = Dog("pug")  
Rodger.setColor("brown")  
print(Rodger.getColor())   

# Output:

# brown

# https://www.geeksforgeeks.org/python-classes-and-objects/