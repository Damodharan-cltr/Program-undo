


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front =self.rear = None
    
    def isempty(self):
        return self.front == None
    def Enqueue(self,item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear =temp
            return
        self.rear.next = temp
        self.rear = temp
    def Dequeue(self):
        if self.isempty():
            return
        temp = self.front
        self.front = temp.next
        
        if(self.front==None):
            self.rear = None
if __name__ == '__main__':
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Dequeue()
    q.Dequeue()
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(50)
    q.Dequeue()
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
