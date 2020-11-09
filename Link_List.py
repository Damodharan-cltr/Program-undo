class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class List:
    def __init__(self):
        self.head = None

if __name__ == "__main__":

     List = List()
     List.head = Node(1)
     second = Node(2)
     third = Node(3)
     List.head.next =second
     second.next = third
     while List.head != None:
         print(List.head.item,end=' ')
         List.head = List.head.next
