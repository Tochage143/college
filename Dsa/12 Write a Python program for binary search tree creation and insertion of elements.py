class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, current, traversal):
        if current is not None:
            self._inorder_traversal(current.left, traversal)
            traversal.append(current.key)
            self._inorder_traversal(current.right, traversal)
        return traversal

# Example usage
bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]
for element in elements:
    bst.insert(element)

print("Inorder Traversal of the BST:", bst.inorder_traversal())
