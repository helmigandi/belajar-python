# In program.py

import hr

salary_employee = hr.SalaryEmployee(110, 'John Smith', 1500)
hourly_employee = hr.HourlyEmployee(111, 'Jane Doe', 40, 15)
commission_employee = hr.CommissionEmployee(112, 'Kevin Bacon', 1000, 250)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
