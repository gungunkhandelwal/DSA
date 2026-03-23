class Node:
    def __init__(self,value,left = None ,right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return
        
        stack = [self.root]

        while stack:
            current = stack.pop()
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    stack.append(current.left)
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    stack.append(current.right)
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value , end =" ")
            self.inorder(node.right)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print("    " * level + str(node.value))
            self.print_tree(node.left, level + 1)


Tree = BinarySearchTree()
Tree.insert(50)
Tree.insert(60)
Tree.insert(40)
Tree.insert(30)
Tree.insert(10)
Tree.insert(90)
Tree.insert(80)
Tree.insert(5)
Tree.inorder(Tree.root)
Tree.print_tree(Tree.root)

