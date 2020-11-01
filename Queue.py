import array

class Queue():
    
    arr = array.array('i',[])
    
    def __init__(self):
        return None
    
    def Enqueue(self,Element):
        arr = self.arr.append(Element)
        return self.arr
    
    def Dequeue(self):
        deq = self.arr[0]
        arr = self.arr.remove(deq)
        return '{} is removed from {}'.format(deq,self.arr)
    
    def Delete(self):
        self.arr = array.array('i',[])
        return -1
    
    def Size(self):
        sz = len(self.arr)
        if sz == 0:
            return -1
        else:
            return sz
        
    def RemoveElement(self,Element):
        for ele in self.arr:
            if Element == ele:
                self.arr.remove(ele)
                return self.arr
            
    def DisplayQueue(self):
        dis = []
        for i in range(1,len(self.arr)+1):
            dis.append(self.arr[0-i])
        return dis
            
            

Queue = Queue()
print("Enter the text for performing Queue.")
print('''      1.Insert        -  'Queue.Enqueue(\'Element\')'.
      2.Remove        -  'Queue.Dequeue()'.
      3.Delete        -  'Queue.Delete()'.
      4.Size          -  'Queue.Size()'.
      5.RemoveElement -  'Queue.RemoveElement(\'Element\')'.
      6.DisplayQueue  -  'Queue.DisplayQueue().''')
print("Element should be integer.")

  
        













