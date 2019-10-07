# The break statement, like in C, breaks out of 
# the innermost enclosing for or while loop.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
print("=================================")
# If the execution reaches a break statement, it immediately
# exits the while loop’s clause.

while True:
    print('Please type your name:')
    name = input()
    if name == 'helmi':
        break
print('Thank you!')
# Please type your name.
# adam
# Please type your name.
# helmi
# Thank you!