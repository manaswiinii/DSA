print("manaswini-cse25102")
class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size
 
    def insert(self, value, index=0):
        if index >= self.size:
            print("Tree is full")
            return
 
        if self.tree[index] is None:
            self.tree[index] = value
        elif value < self.tree[index]:
            self.insert(value, 2 * index + 1)
        else:
            self.insert(value, 2 * index + 2)
 
    def inorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
 
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)
 
    def preorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
 
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)
 
    def postorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
 
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")
 
 
bt = BinaryTree(10)
 
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)
 
print("Inorder:")
bt.inorder()
 
print("\nPreorder:")
bt.preorder()
 
print("\nPostorder:")
bt.postorder()