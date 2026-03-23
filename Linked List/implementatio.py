class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

singlyLink=Node(3)
a=Node(6)
b=Node(9)
c=Node(12)

singlyLink.next=a
a.next=b
b.next=c

print(singlyLink.data)

def display(singlyLink):
    current=singlyLink
    elments=[]
    while current:
        elments.append(str(current.data))
        current=current.next
    print('-> '.join(elments))

display(singlyLink)


class DoublyLink:
    def __init__(self,data,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous

doublyLink=DoublyLink(10)
A1=DoublyLink(20)
B1=DoublyLink(30)
C1=DoublyLink(40)

doublyLink.next=A1
A1.next=B1
A1.previous=doublyLink
B1.next=C1
B1.previous=A1

def displayDoubly(doublyLink):
    current=doublyLink
    elements=[]
    while current:
        elements.append(str(current.data))
        current=current.next
    print(' <--> '.join(elements))

displayDoubly(doublyLink)

circularLink=Node(2)
a2=Node(4)
b2=Node(6)
c2=Node(8)

circularLink.next=a2
a2.next=b2
b2.next=c2
c2.next=circularLink

print(c2.next.data)

def displayCircular(circularLink):
    current=circularLink
    elments=[]
    while current:
        elments.append(str(current.data))
        current=current.next
        if current == circularLink:
            elments.append(str(current.data))
            break
    print(' --> '.join(elments))

displayCircular(circularLink)



