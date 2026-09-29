class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None  # Points to the top node of the stack

    # 1. Push Operation
    def push(self):
        data = int(input("Enter data to push: "))
        new_node = Node(data)
        
        # New node points to the current top, then becomes the new top
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed onto the stack.")

    # 2. Pop Operation
    def pop(self):
        if not self.top:
            print("Stack Underflow! Stack is empty.")
            return
        
        popped_node = self.top
        self.top = self.top.next  # Move top pointer to the next node
        print(f"Popped element: {popped_node.data}")

    # 3. Peek Operation
    def peek(self):
        if not self.top:
            print("Stack is empty!")
            return
        
        print(f"Top element is: {self.top.data}")

    # 4. Display Operation
    def display(self):
        if not self.top:
            print("Stack is empty!")
            return
        
        print("Stack elements (Top to Bottom):")
        temp = self.top
        while temp:
            print(f"| {temp.data} |")
            temp = temp.next
        print("-----")


def main():
    stack_obj = StackLinkedList()
    
    while True:
        print("\n----- STACK OPERATIONS (LINKED LIST) -----")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 1:
            stack_obj.push()
        elif choice == 2:
            stack_obj.pop()
        elif choice == 3:
            stack_obj.peek()
        elif choice == 4:
            stack_obj.display()
        elif choice == 5:
            print("Exiting stack program.")
            break
        else:
            print("Invalid choice! Select numbers between 1 and 5.")

if __name__ == "__main__":
    main()
