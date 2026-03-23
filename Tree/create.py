class Tree:
    def __init__(self,val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"Tree({self.val})"

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.right = Tree(10)

A = Tree(1)
B = Tree(2)
C= Tree(3)
D = Tree(4)
E = Tree(5)
F = Tree(10)

A.left = B
B.left = D
B.right = E
A.right = C
C.left = F


print(root.val)

def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(root)

print()
print('############################')
print()

def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(root)

print()
print('############################')
print()

def post_order(node):
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(root)

# Iterative method


print()
print('############################')
print()

def pre_order_dfs(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right : stack.append(node.right)
        if node.left : stack.append(node.left)

pre_order_dfs(root)


print()
print('############################')
print()

# Level order
from collections import deque

def level_order_traversal(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order_traversal(root)

print()
print('############################')
print()

def search_dfs(node,target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return search_dfs(node.left,target) or search_dfs(node.right , target)

print(search_dfs(root , 0))


print()
print('############################')
print()


def search_bst(node , target):
    if not node:
        return False
    
    if node.val == target:
        return True
    if target < node.val:
        return search_bst(node.left , target)
    else:
        return search_bst(node.right , target)

print(search_bst(root , 10))

print()
print('############################')
print()

def inorder_travs(node):
    stack = []
    curr = node
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr  = stack.pop()
        print(curr.val,end=' ')
        curr = curr.right

inorder_travs(root)

print()
print('############################')
print()

def postorder(node):
    if not node:
        return
    s1,s2=[node] , []

    while s1:
        curr = s1.pop()
        s2.append(curr)
        if curr.left: s1.append(curr.left)
        if curr.right: s1.append(curr.right)
    
    while s2:
        print(s2.pop().val,end=' ')

postorder(root)
