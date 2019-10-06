# The continue statement, also borrowed from C, 
# continues with the next iteration of the loop:

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
# Found an even number 2
# Found a number 3
# Found an even number 4
# Found a number 5
# Found an even number 6
# Found a number 7
# Found an even number 8
# Found a number 9

print("=================================")

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
# Who are you?
# andi
# Who are you?
# Joe
# Hello, Joe. What is the password? (It is a fish.)
# fish
# Who are you?
# Joe
# Hello, Joe. What is the password? (It is a fish.)
# swordfish
# Access granted.