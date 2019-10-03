x = int(input("Please enter an integer: "))
# Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Exception Handle
# import sys
# try:
#     x = int(input("Enter a number between 1 - 10 "))
# except ValueError:
#     print("Err.. numbers only")
#     sys.exit()

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")