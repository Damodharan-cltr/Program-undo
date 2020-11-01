import array

class List():
    
    arr = array.array('i',[])
    
    def __init__(self):
        return None
    
    def Insert(self,Element):
        arr = self.arr.append(Element)
        return self.arr
    
    def Remove(self,Element):
        fun = False
        for ele in self.arr:
            if ele == Element:
                arr = self.arr.remove(Element)
                fun = True
                break
        if fun == True:
            return self.arr
        else:
            return "Element not found."
        
    def Index(self,Element):
        ind = 0
        bol = False
        for i in range(len(self.arr)):
            if self.arr[i] == Element:
                bol = True
                break
            else:
                ind += 1
        if bol == True:
            return ind
        else:
            return -1
                
    def Delete(self):
        self.arr = array.array('i',[])
        return -1
    
    def Size(self):
        sz = len(self.arr)
        if sz == 0:
            return -1
        else:
            return sz
    def DisplayList(self):
        lis = []
        for ele in self.arr:
            lis.append(ele)
        return lis

List = List()
print("Enter the text for performing List.")
print('''      1.Insert      -  'List.Insert(\'Element\')'.
      2.Remove      -  'List.Remove(\'Element\')'.
      3.Index       -  'List.Index(\'Element\')'.
      4.Delete      -  'List.Delete()'.
      5.Size        -  'List.Size()'.
      6.DisplayList -  'List.DisplayList().''')
print("Element should be number.")


