class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        # Initialize the array with None and track the top index
        self.stack = [None] * capacity
        self.top = -1

    # 1. Push Operation
    def push(self):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        
        data = int(input("Enter data to push: "))
        self.top += 1
        self.stack[self.top] = data
        print(f"{data} pushed onto the stack.")

    # 2. Pop Operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow! Stack is empty.")
            return
        
        popped_element = self.stack[self.top]
        self.stack[self.top] = None  # Clear the slot
        self.top -= 1
        print(f"Popped element: {popped_element}")

    # 3. Peek Operation
    def peek(self):
        if self.top == -1:
            print("Stack is empty!")
            return
        
        print(f"Top element is: {self.stack[self.top]}")

    # 4. Display Operation
    def display(self):
        if self.top == -1:
            print("Stack is empty!")
            return
        
        print("Stack elements (Top to Bottom):")
        # Loop backwards from top down to 0
        for i in range(self.top, -1, -1):
            print(f"| {self.stack[i]} |")
        print("-----")


def main():
    try:
        size = int(input("Enter the size of the stack: "))
    except ValueError:
        print("Please enter a valid size integer. Defaulting size to 5.")
        size = 5

    stack_obj = Stack(size)
    
    while True:
        print("\n----- STACK OPERATIONS -----")
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
