# Circular Queue implementation using Array

MAX_SIZE = 5
queue = [None] * MAX_SIZE

front = -1
rear = -1


def enqueue():
    global front, rear

    # Check if queue is full
    if (rear + 1) % MAX_SIZE == front:
        print("Queue Overflow! Queue is full.")
        return

    item = input("Enter the element to enqueue: ")

    # First element
    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % MAX_SIZE

    queue[rear] = item
    print(item, "inserted into the queue.")


def dequeue():
    global front, rear

    # Check if queue is empty
    if front == -1:
        print("Queue Underflow! Queue is empty.")
        return

    item = queue[front]
    queue[front] = None

    # If only one element was present
    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % MAX_SIZE

    print(item, "deleted from the queue.")


def peek():
    if front == -1:
        print("Queue is empty.")
    else:
        print("Front element:", queue[front])


def display():
    if front == -1:
        print("Queue is empty.")
        return

    print("Queue elements:", end=" ")

    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % MAX_SIZE

    print()


# Menu-driven program
while True:
    print("\n--- CIRCULAR QUEUE USING ARRAY ---")
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
