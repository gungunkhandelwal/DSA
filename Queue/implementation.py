from collections import deque

queue=deque()
queue.append(1)
queue.appendleft(2)
queue.append(3)
queue.append(10)
queue.appendleft(34)
print(queue.pop())
print(queue.popleft())
print(queue)