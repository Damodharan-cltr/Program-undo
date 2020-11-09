

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    def Push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            
    def Pop(self):
        if self.isempty():
            return None
        else:
            poppednode  = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    
    def Peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
        
    def Display(self):
        internode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(internode != None):
                print(internode.data, "->", end = " ")
                internode = internode.next
            return
        


Stack = Stack()
print("Enter Stack.Push('Elememt') to add")
print("Enter Stack.Pop() to remove top most element")
print("Enter Display() to view stack") 
