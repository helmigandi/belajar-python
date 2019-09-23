print(2 + 2)
# 4
print(50 - 5*6)
# 20
print((50 - 5*6) / 4)
# 5.0
print(8 / 5)  # division always returns a floating point number
#1.6

print("===================")

print(17 / 3)  # classic division returns a float
#5.666666666666667
print(17 // 3)  # floor division discards the fractional part
# 5
print(17 % 3)  # the % operator returns the remainder of the division
# 2
print(5 * 3 + 2)  # result * divisor + remainder
# 17

print("===================")

print(5 ** 2)  # 5 squared
# 25
print(2 ** 7)  # 2 to the power of 7
# 128

print("===================")

# The equal sign (=) is used to assign a value to a variable.
width = 20
height = 5 * 9
print(width * height)
# 900

print("===================")

# There is full support for floating point; operators with 
# mixed type operands convert the integer operand to floating point:
print(4 * 3.75 - 1)
# 14.0

print("===================")

# In interactive mode, the last printed expression 
# is assigned to the variable _. Because of we are not using interactive
# mode, we changes with total and totalTax
tax = 12.5 / 100
price = 100.50
totalTax = price * tax
print(totalTax) # >>> price + _
# 12.5625
total = price + totalTax
print(total)
# 113.0625
print(round(total, 2)) # >>> round(_, 2)
# 113.06
