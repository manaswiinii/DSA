print("manaswini-cse25102")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
class BinaryTree:
    def __init__(self):
        self.root = None
 
    def insert(self, value):
        new_node = Node(value)
 
        if self.root is None:
            self.root = new_node
            return
 
        queue = [self.root]
 
        while queue:
            current = queue.pop(0)
 
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
 
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)
 
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
 
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
 
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
 
 
bt = BinaryTree()
 
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)
 
print("Inorder:")
bt.inorder(bt.root)
 
print("\nPreorder:")
bt.preorder(bt.root)
 
print("\nPostorder:")
bt.postorder(bt.root)
