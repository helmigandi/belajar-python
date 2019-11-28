""" Quick overview of inheritance
So what is class inheritance? Similarly to genetics, a child 
class can 'inherit' attributes and methods from a parent. 
Let's jump right into some code for an example. In the below 
code block we'll demonstrate inheritance with a Child class 
inheriting from a Parent class.

"""
class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = 'I am a child'

# Create instance of child
child = Child()

# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()

# Output
# I am a child
# I am a parent
# Back in my day...

"""
We see that the Child class 'inherited' attributes and methods 
from the Parent class. Without any work on our part, the 
Parent.parent_method is a part of the Child class. To get 
the benefits of the Parent.__init__() method we needed to 
explicitly call the method and pass self. This is because 
when we added an __init__ method to Child, we overwrote the 
inherited __init__.

"""

""" Intro to super

In the simplest case, the super function can be used to replace 
the explicit call to Parent.__init__(self). Our intro example 
from the first section can be rewritten with super as seen below. 
Note, that the below code block is written in Python 3, earlier 
versions use a slightly different syntax. Additionally, the output 
has been omitted since it's identical to the first code block.

"""

class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = 'I am a parent'


# Create instance of child
child = Child()

# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()

"""
To be honest, super in this case gives us little, if any, 
advantage. Depending on the name of our parent class we 
might save some keystrokes, and we don't have to pass self 
to the call to __init__. Below are some pros and cons of 
the use of super in single inheritance cases.

"""



""" Multiple inheritance, super, and the diamond problem

This is actually an example of the 'diamond problem' of multiple 
inheritance. Its name is of course based on the shape of its 
design, and the fact that it's a fairly confusing problem.

"""

class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)

# Output

# Start init TextDescriber.__init__()
# Start WordCounter.__init__()
# Start init Vocabulary.__init__()
# Start Tokenizer.__init__()
# End Tokenizer.__init__()
# End init Vocabulary.__init__()
# End WordCounter.__init__()
# End init TextDescriber.__init__()
# --------
# ['row', 'row', 'row', 'your', 'boat']
# {'boat', 'your', 'row'}
# 5

"""
First off, we see the TextDescriber class has inherited all the 
attributes of the class family tree. Thanks to multiple 
inheritance we can 'combine' the functionality of more than 
one class.

https://www.datacamp.com/community/tutorials/super-multiple-inheritance-diamond-problem

"""