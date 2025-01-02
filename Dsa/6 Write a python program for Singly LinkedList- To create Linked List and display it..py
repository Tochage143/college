
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedlist:
    def __init__(self):
        self.head = None

    def insert_node(self,data):
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
        else :
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head == None:
            print('list is empyt ')
        else :
            current = self.head
            while current:
                print(current.data,end="-> ")
                current = current.next
            print('None')


linkedlist = SinglyLinkedlist()
linkedlist.insert_node(1)
linkedlist.insert_node(2)
linkedlist.insert_node(3)
linkedlist.display()
