# Queue with circular queue
class QueueArray:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        self.capacity=capacity
        self.front=0
        self.rear=-1
        self.size=0
    
    def enqueue(self,item):
        if self.size == self.capacity:
            return "Queue is full"
        self.rear=(self.rear+1)% self.capacity
        self.queue[self.rear]=item
        self.size +=1
    
    def deque(self):
        if self.size ==0:
            return "Queue is empty"
        removed=self.queue[self.front]
        self.front=(self.front+1)% self.capacity
        self.size -=1
        return removed
    
    def display(self):
        print("Queue",end=' ')
        for i in range(self.size):
            index=(self.front+i)% self.capacity
            print(self.queue[index],end=" ")
        print()

queue=QueueArray(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.deque()
queue.deque()
queue.enqueue(60)
queue.enqueue(70)
queue.display()

# Queue withour curcular import
class QueueArrays:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.rear == self.capacity - 1:
            return "Queue is full"
        self.rear += 1
        self.queue[self.rear] = item
        self.size += 1

    def deque(self):
        if self.front > self.rear:
            return "Queue is empty"
        removed = self.queue[self.front]
        self.front += 1
        self.size -= 1
        return removed

    def display(self):
        if self.front > self.rear:
            print("Queue is empty")
            return
        print("Queue:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

Q=QueueArrays(5)
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
print(Q.deque())
print(Q.deque())
print(Q.enqueue(60))
Q.enqueue(70)
Q.display()