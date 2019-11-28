# Bagian 1
""" Class Definition Syntax

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

A class is a user-defined blueprint or prototype from which 
objects are created. Classes provide a means of bundling data 
and functionality together. Creating a new class creates a new 
type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for 
maintaining its state. Class instances can also have methods 
(defined by its class) for modifying its state.

An object is created using the constructor of the class. 
This object will then be called the instance of the class. 
In Python we create instances in the following manner:

Instance = class(arguments)

"""

class Dog:

    def __init__(self):
        pass

""" How to create a class

To define a class in Python, you can use the class keyword, 
followed by the class name and a colon. Inside the class, 
an __init__ method has to be defined with def. This is the 
initializer that you can later use to instantiate objects. 
It's similar to a constructor in Java. __init__ must always 
be present! It takes one argument: self, which refers to 
the object itself. Inside the method, the pass keyword is 
used as of now, because Python expects you to type something 
there. Remember to use correct indentation!

Note: self in Python is equivalent to this in C++ or Java.

In this case, you have a (mostly empty) Dog class.
"""

ozzy = Dog()
print(ozzy)
# <__main__.Dog object at 0x111f47278>

""" Instantiating objects

To instantiate an object, type the class name, followed by 
two brackets. You can assign this to a variable to keep 
track of the object.

"""

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

""" Adding attributes to a class

After printing ozzy, it is clear that this object is a dog. 
But you haven't added any attributes yet. Let's give the Dog 
class a name and age.

You can see that the function now takes two arguments after self: 
name and age. These then get assigned to self.name and self.age 
respectively. You can now now create a new ozzy object, with a 
name and age.

ozzy = Dog("Ozzy", 2)

To access an object's attributes in Python, you can use the dot 
notation. This is done by typing the name of the object, followed 
by a dot and the attribute's name.

print(ozzy.name)
print(ozzy.age)
print(ozzy.name + " is " + str(ozzy.age) + " year(s) old.")

# Ozzy
# 2
# Ozzy is 2 year(s) old.

The str() function is used here to convert the age attribute, 
which is an integer, to a string, so you can use it in 
the print() function. 

"""

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

""" Define methods in a class

This is where instance methods come in. You can rewrite the class 
to now include a bark() method.

The bark method can now be called using the dot notation, 
after instantiating a new ozzy object. The method should 
print "bark bark!" to the screen. Notice the parentheses 
(curly brackets) in .bark(). These are always used when 
calling a method. They're empty in this case, since the 
bark() method does not take any arguments.

ozzy = Dog("Ozzy", 2)
ozzy.bark()

# bark bark!

Recall how you printed ozzy earlier? The code below now 
implements this functionality in the Dog class, with the 
doginfo() method. You then instantiate some objects with 
different properties, and call the method on them.

"""

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

ozzy.doginfo()
skippy.doginfo()
filou.doginfo()

# Ozzy is 2 year(s) old.
# Skippy is 12 year(s) old.
# Filou is 8 year(s) old.

"""
As you can see, you can call the doginfo() method on objects 
with the dot notation. The response now depends on which Dog 
object you are calling the method on.

Since dogs get older, it would be nice if you could adjust 
their age accordingly. Ozzy just turned 3, so let's change 
his age.

"""

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

ozzy = Dog("Ozzy", 2)
print(ozzy.age)
# 2

ozzy.birthday()
print(ozzy.age)
# 3

"""
Now, you don't need to manually change the dog's age. whenever 
it is its birthday, you can just call the birthday() method.

"""

class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

""" Passing arguments to methods

 Take a look at the setBuddy() method below. It takes self, 
 as per usual, and buddy as arguments. In this case, buddy 
 will be another Dog object. Set the self.buddy attribute 
 to buddy, and the buddy.buddy attribute to self. This means 
 that the relationship is reciprocal; you are your buddy's 
 buddy. In this case, Filou will be Ozzy's buddy, which 
 means that Ozzy automatically becomes Filou's buddy. 

You can now call the method with the dot notation, and 
pass it another Dog object. In this case, Ozzy's buddy 
will be Filou:

ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)

If you now want to get some information about Ozzy's buddy, 
you can use the dot notation twice:. First, to refer to 
Ozzy's buddy, and a second time to refer to its attribute.

print(ozzy.buddy.name)
print(ozzy.buddy.age)
# Filou
# 8

Notice how this can also be done for Filou.

print(filou.buddy.name)
print(filou.buddy.age)
# Ozzy
# 2

The buddy's methods can also be called. The self argument that 
gets passed to doginfo() is now ozzy.buddy, which is filou.

ozzy.buddy.doginfo()
# Filou is 8 year(s) old.


"""