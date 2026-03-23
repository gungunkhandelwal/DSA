class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next= next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if prev is not None:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_start(5)
ll.insert_at_end(30)

ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

ll.delete_node(20)
ll.display()  # Output: 5 -> 10 -> 30 -> None
