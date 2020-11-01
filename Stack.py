
import array

class Stack():
    
    """"Creating a class "Stack" in order to perform
    stack data structure using array."""
    
    arr = array.array('i',[])
    
    def __init__(self):
        return None
    
    def Push(self,Element):
        arr=self.arr.append(Element)
        return self.arr
    
    def Pop(self):
        rmv = self.arr[-1]
        arr = self.arr.remove(rmv)
        return "{0} is removed from {1}".format(rmv,self.arr)
    
    def Delete(self):
        self.arr = array.array('i',[])
        return -1
    
    def Size(self):
        sz = len(self.arr)
        if sz == 0:
            return -1
        else:
            return sz
        
    def PopElement(self,Element):
        for ele in self.arr:
            if Element == ele:
                self.arr.remove(ele)
                return self.arr
            
    def DisplayStack(self):
        for i in range(1,len(self.arr)+1):
            dis = self.arr[0-i]
            print(dis)
        
        
Stack = Stack()
print("Enter the text for performing Stack.")
print('''      1.Insert        -  'Stack.Push(\'Element\')'.
      2.Remove        -  'Stack.Pop()'.
      3.Delete        -  'Stack.Delete()'.
      4.Size          -  'Stack.Size()'.
      5.PopElement    -  'Stack.PopElement(\'Element\')'.
      6.DisplayStack  -  'Stack.DisplayStack().''')
print("Element should be number.")

