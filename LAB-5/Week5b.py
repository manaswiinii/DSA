class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Link to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create_list(self):
        n = int(input("Enter number of nodes: "))
        self.head = None
        for _ in range(n):
            data = int(input("Enter data: "))
            self.insert_at_end_internal(data)
        print("Linked List created successfully")

    # Internal helper to handle backward/forward links during creation
    def insert_at_end_internal(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # 2. Insert at Beginning
    def insert_at_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 3. Insert at End
    def insert_at_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # 4. Insert at Index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        if index < 0:
            print("Invalid index!")
            return
        if index == 0:
            new_node = Node(data)
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        curr = 0
        while temp and curr < index - 1:
            temp = temp.next
            curr += 1
        if not temp:
            print("Index out of bounds!")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            if temp.next:  # If inserting before an existing node
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    # 5. Delete from Beginning
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty!")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # 6. Delete from End
    def delete_from_end(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    # 7. Delete from Index
    def delete_from_index(self):
        index = int(input("Enter index: "))
        if not self.head:
            print("List is empty!")
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        curr = 0
        while temp and curr < index:
            temp = temp.next
            curr += 1
        if not temp:
            print("Index out of bounds!")
        else:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev

    # 8. Count Number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(f"Number of nodes: {count}")

    # 9. Display
    def display(self):
        if not self.head:
            print("None")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def main():
    llist = DoublyLinkedList()
    
    while True:
        print("\n----- DOUBLY LINKED LIST -----")
        print("1. Create Linked List")
        print("2. Insert at Beginning")
        print("3. Insert at End")
        print("4. Insert at Index")
        print("5. Delete from Beginning")
        print("6. Delete from End")
        print("7. Delete from Index")
        print("8. Count Number of nodes")
        print("9. Display")
        print("10. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 1:
            llist.create_list()
        elif choice == 2:
            llist.insert_at_beginning()
        elif choice == 3:
            llist.insert_at_end()
        elif choice == 4:
            llist.insert_at_index()
        elif choice == 5:
            llist.delete_from_beginning()
        elif choice == 6:
            llist.delete_from_end()
        elif choice == 7:
            llist.delete_from_index()
        elif choice == 8:
            llist.count_nodes()
        elif choice == 9:
            llist.display()
        elif choice == 10:
            break
        else:
            print("Invalid choice! Select numbers between 1 and 10.")

if __name__ == "__main__":
    main()
