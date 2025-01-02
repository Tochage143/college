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

    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted = False
        while not sorted:
            sorted = True
            current = self.head

            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    sorted = False
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_end(50)
dll.insert_at_end(20)
dll.insert_at_end(40)
dll.insert_at_end(10)
dll.insert_at_end(30)

print("Original List:")
dll.display()

dll.sort()
print("Sorted List in Ascending Order:")
dll.display()
