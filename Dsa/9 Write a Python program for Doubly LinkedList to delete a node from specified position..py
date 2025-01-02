class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_at_position(self, position):
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        if position == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(position):
            current = current.next
            print(current.data)
            if not current:
                print("Position out of bounds.")
                return

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Original List:")
dll.display()

dll.delete_at_position(2)
print("After Deleting Node at Position 2:")
dll.display()
