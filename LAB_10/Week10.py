print("Manaswini-CSE25102")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root is None:
        return 0
    return root.height


def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def right_rotate(y):
    x = y.left
    t = x.right

    x.right = y
    y.left = t

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    t = y.left

    y.left = x
    x.right = t

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    # LL case
    if b > 1 and data < root.left.data:
        return right_rotate(root)

    # RR case
    if b < -1 and data > root.right.data:
        return left_rotate(root)

    # LR case
    if b > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL case
    if b < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


root = None

while True:
    print("\n\n1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        root = insert(root, x)
    elif ch == 2:
        inorder(root)
    elif ch == 3:
        preorder(root)
    elif ch == 4:
        break
    else:
        print("Invalid choice")

