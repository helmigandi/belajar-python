# Python Docstring is the documentation string which is string 
# literal, and it occurs in the class, module, function or 
# method definition, and it is written as a first statement. 

# One-line DocString
def square(a):
    '''Returns argument a is squared.'''
    return a**a

print (square.__doc__)


help(square)

# Multi-line Docstrings

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)

# Example 1
def string_reverse(str1):
    """ Returns the reversed String.

    Parameters:
        str1 (str):The string which is to be reversed.

    Returns:
        reverse(str1):The string which gets reversed.   

    """
    reverse_str1 = ''
    i = len(str1)
    while i > 0:
        reverse_str1 += str1[ i - 1 ]
        i = i- 1
    return reverse_str1
print(string_reverse('projkal998580'))

# Example 2

class Vehicles(object):
    '''
    The Vehicle object contains a lot of vehicles

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    '''
    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance,destination):
        '''We can't travel distance in vehicles without fuels, so here is the fuels

        Args:
            distance (int): The amount of distance traveled
            destination (bool): Should the fuels refilled to cover the distance?

        Raises:
            RuntimeError: Out of fuel

        Returns:
            cars: A car mileage
        '''
        pass
