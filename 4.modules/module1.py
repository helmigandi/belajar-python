""" Modules

Modules in Python are separate code groupings which packages 
program code and data for reuse.
Some of the advantages of using modules in your Python code are:
- they enable you to organize your code into smaller pieces that are easier to manage.
- the code in the modules can be reloaded and rerun as many times as needed, which enables code reuse.
- modules are self-contained – you can never see a name in another file, 
  unless you explicitly import it. This helps you to avoid name clashes across your programs.

The collection of classes, functions, and variables inside
a module is known as attributes. These attributes can 
be accessed using their names.

"""

import simple_module1
simple_module1.Welcome("Bob")

""" Import modules


There are two ways to import a module:

- using the import statement – imports the entire module.
- using the from…import statement – imports only individual module attributes.

Here is how we can import a module using the import statement:

"""

# We can also use the from…import statement to import only the attribute we need.

from simple_module1 import Bye
Bye("John")

import sys
for p in sys.path:
    print(p)

""" Find files on disk

Python looks for files using path information from three sources:
- environment variables – environment variables (such as PYTHONPATH) that containt a list of directories to search for files.
- current directory – Python can access files in contained in the current directory.
- default directories – Python can find files conteined in the set of default directories included in the path information.

To add a path to the sys.path attribute, use the following code:
import sys
sys.path.append("E:\\backup")

To change the current Python directory, the following code can be used:
import os
os.chdir("C:\Python34\Scripts")

"""

dir(simple_module1)
print(dir(simple_module1))
# ['Bye', 'Welcome', '__builtins__', '__cached__', '__doc__', 
# '__file__', '__loader__', '__name__', '__package__', '__spec__']

""" Display module content

    Bye, Welcome – the functions provided by the module
    __builtins__ – a listing of all the built-in attributes that are accessible from the module.
    __cached__ – the name and location of the cached file associated with the module.
    __doc__ – help information for the module.
    __file__ – the name and location of the module, relative to the current Python directory.
    __loader__ – the loader information for this module.
    __name__ – the name of the module.
    __package__ – used internally by the import system.
    __spec__ – set to the module spec that was used when importing the module.

https://geek-university.com/python/display-module-content/
"""