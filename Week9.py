
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def find_min(self, root):
        while root and root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


bst = BST()

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Delete")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        bst.root = bst.insert(bst.root, data)

    elif choice == 2:
        key = int(input("Enter value to search: "))
        if bst.search(bst.root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        bst.inorder(bst.root)
        print()

    elif choice == 4:
        bst.preorder(bst.root)
        print()

    elif choice == 5:
        bst.postorder(bst.root)
        print()

    elif choice == 6:
        key = int(input("Enter value to delete: "))
        bst.root = bst.delete(bst.root, key)
        print("Deletion completed")

    elif choice == 7:
        break

    else:
        print("Invalid choice")
