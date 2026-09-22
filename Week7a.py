# Queue implementation using Array

queue = []
MAX_SIZE = 5

def enqueue():
    if len(queue) == MAX_SIZE:
        print("Queue Overflow! Queue is full.")
    else:
        item = input("Enter the element to enqueue: ")
        queue.append(item)
        print(item, "inserted into the queue.")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow! Queue is empty.")
    else:
        item = queue.pop(0)
        print(item, "deleted from the queue.")

def peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements:", end=" ")
        for item in queue:
            print(item, end=" ")
        print()


# Menu-driven program
while True:
    print("\n--- QUEUE USING ARRAY ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
