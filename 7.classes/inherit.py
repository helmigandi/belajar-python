""" Inheritance

Inheritance models what is called an is a relationship. 
This means that when you have a Derived class that inherits 
from a Base class, you created a relationship where Derived 
is a specialized version of Base.



Note: In an inheritance relationship:

1. Classes that inherit from another are called derived classes, 
subclasses, or subtypes.
2. Classes from which other classes are derived are called base 
classes or super classes.
3. A derived class is said to derive, inherit, or extend a base 
class.

Let’s say you have a base class Animal and you derive from it to 
create a Horse class. The inheritance relationship states that a 
Horse is an Animal. This means that Horse inherits the interface 
and implementation of Animal, and Horse objects can be used to 
replace Animal objects in the application.

This is known as the Liskov substitution principle. The principle 
states that “in a computer program, if S is a subtype of T, then 
objects of type T may be replaced with objects of type S without 
altering any of the desired properties of the program”.

Everything in Python is an object. Modules are objects, 
class definitions and functions are objects, and of course, 
objects created from classes are objects too.

"""

""" Creating Class Hierarchies

In this section, you’ll start modeling an HR system. The example 
will demonstrate the use of inheritance and how derived classes 
can provide a concrete implementation of the base class interface.

The HR system needs to process payroll for the company’s employees,
but there are different types of employees depending on how their 
payroll is calculated.

You start by implementing a PayrollSystem class that processes 
payroll:

-----------------------------------------------------------------
# In hr.py

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')
-----------------------------------------------------------------

The PayrollSystem implements a .calculate_payroll() method that 
takes a collection of employees and prints their id, name, and 
check amount using the .calculate_payroll() method exposed on 
each employee object.

Now, you implement a base class Employee that handles the 
common interface for every employee type:

-----------------------------------------------------------------
# In hr.py

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
-----------------------------------------------------------------

Employee is the base class for all employee types. 
It is constructed with an id and a name. 

The HR system requires that every Employee processed must 
provide a .calculate_payroll() interface that returns the 
weekly salary for the employee. The implementation of that 
interface differs depending on the type of Employee.

For example, administrative workers have a fixed salary, 
so every week they get paid the same amount:

-----------------------------------------------------------------
# In hr.py

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
-----------------------------------------------------------------

You create a derived class SalaryEmployee that inherits Employee. 
The class is initialized with the id and name required by the base 
class, and you use super() to initialize the members of the base 
class. 

SalaryEmployee also requires a weekly_salary initialization 
parameter that represents the amount the employee makes per week.

The class provides the required .calculate_payroll() method 
used by the HR system. The implementation just returns the 
amount stored in weekly_salary.

The company also employs manufacturing workers that are paid 
by the hour, so you add an HourlyEmployee to the HR system:

-----------------------------------------------------------------
# In hr.py

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
-----------------------------------------------------------------

The HourlyEmployee class is initialized with id and name, 
like the base class, plus the hours_worked and the hour_rate 
required to calculate the payroll. The .calculate_payroll() 
method is implemented by returning the hours worked times 
the hour rate.

Finally, the company employs sales associates that are paid 
through a fixed salary plus a commission based on their sales, 
so you create a CommissionEmployee class:

-----------------------------------------------------------------
# In hr.py

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
-----------------------------------------------------------------

The application creates its employees and passes them to 
the payroll system to process payroll:

-----------------------------------------------------------------
# In program.py

import hr

salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
-----------------------------------------------------------------
You can run the program in the command line and see the results:

-----------------------------------------------------------------
$ python program.py

Calculating Payroll
===================
Payroll for: 1 - John Smith
- Check amount: 1500

Payroll for: 2 - Jane Doe
- Check amount: 600

Payroll for: 3 - Kevin Bacon
- Check amount: 1250
-----------------------------------------------------------------

The program creates three employee objects, one for each of the 
derived classes. Then, it creates the payroll system and passes 
a list of the employees to its .calculate_payroll() method, which
calculates the payroll for each employee and prints the results.


https://realpython.com/inheritance-composition-python/
"""
