# The pass statement does nothing. It can be used 
# when a statement is required syntactically but 
# the program requires no action. For example:

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# This is commonly used for creating minimal classes:
class MyEmptyClass:
    pass