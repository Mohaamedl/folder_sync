from LinkedList import LinkedList
class Queue:
    def __init__(self,maxSize=1000):
        self._items = LinkedList()
        self._maxSize = maxSize
    
    
    
    def __str__(self):
        return self._items.__str__()
    
    
    def add(self,e):
        try: 
            if self.size() >= self._maxSize:
                raise Exception('Full')
            self._items.addFirst(e)
        except Exception as e:
            print(e)
            
            
    def size(self):
        return self._items.size()
    
    
    def first(self):
        return self._items.first()
    
    def remove(self):
        try:
            if self.isEmpty():
                raise Exception('Empty Queue')
            self._items.removeFirst()
        except Exception as e:
            print(e)
    def isEmpty(self):
        return self._items.isEmpty()
    
    
    def clear(self):
        self._items.reset()
        
