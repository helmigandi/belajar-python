def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    eggs = 0
    return eggs
spam()
""" Local Scopes Cannot Use Variables in Other Local Scopes

When bacon() returns, the local scope for that call is destroyed. 
The program execution continues in the spam() function to print 
the value of eggs ❸, and since the local scope for the call to 
spam() still exists here, the eggs variable is set to 99. This 
is what the program prints.

We use global keyword to read and write a global variable inside a function.
Use of global keyword outside a function has no effect
"""
print("--------------------------------------------")
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

""" The global Statement


The global keyword is used to create global variables from a 
no-global scope, e.g. inside a function.

"""
print("----------------------------------------")
def scope_test():
    def do_global():
        nonlocal spam
        spam = "non spam"
    
    spam = "test spam"
    do_global()
    print("After global assignment:", spam)

scope_test()
# print("In global scope:", spam)

print("----------------------------------------")
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()

""" The nonlocal Statement

The nonlocal keyword is used to work with variables inside 
nested functions, where the variable should not belong to 
the inner function.

Use the keyword nonlocal to declare that the variable is not local.

Nonlocal variable are used in nested function whose local 
scope is not defined. This means, the variable can be neither 
in the local nor the global scope.

"""