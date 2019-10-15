# The list methods make it very easy to use a list as a stack, 
# where the last element added is the first element retrieved 
# (“last-in, first-out”). 
stack = [3, 4, 5]

stack.append(6)
stack.append(7)
print(stack)# [3, 4, 5, 6, 7]

stack.pop()# 7
print(stack)# [3, 4, 5, 6]

stack.pop()# 6
stack.pop()# 5
print(stack)# [3, 4]