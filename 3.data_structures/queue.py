# The first element added is the first element retrieved 
# (“first-in, first-out”)

# To implement a queue, use collections.deque which was 
# designed to have fast appends and pops from both ends.

from collections import deque
queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
#'Eric'
queue.popleft()                 # The second to arrive now leaves
#'John'
print(queue)                           # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])