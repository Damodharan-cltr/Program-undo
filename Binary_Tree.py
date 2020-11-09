class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def TraversePreOrder(self):
        print(self.val, end = " ")
        if self.left:
            self.left.TraversePreOrder()
        if self.right:
            self.right.TraversePreOrder()

    def TraverseInOrder(self):
        if self.left:
            self.left.TraverseInOrder()
        print(self.val, end=" ")
        if self.right:
            self.right.TraverseInOrder()

    def TraversePostOrder(self):
        if self.left:
            self.left.TraversePostOrder()
        if self.right:
            self.right.TraversePostOrder()
        print(self.val, end=' ')

root= Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("PreOrder")
root.TraversePreOrder()
print("\nPostOrder")
root.TraversePostOrder()
print("\nInorder")
root.TraverseInOrder()
