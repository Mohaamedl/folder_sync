class Queue:
    def __init__(self,maxSize=1000):
        self._items = []
        self._maxSize = maxSize
    
    
    
    def __str__(self):
        s ='('
        for el in self._items:
            s+=str(el)+','
            if s.endswith(','):
                s=s[:-1]
        s+=')'
        return s
    
    
    def add(self,e):
        try: 
            if self.size() >= self._maxSize:
                raise Exception('Full')
            self._items.insert(0,e)
        except Exception as e:
            print(e)
            
            
    def size(self):
        return len(self._items)
    
    
    def first(self):
        return self._items[-1]
    
    def remove(self):
        try:
            if self.isEmpty():
                raise Exception('Empty Queue')
            self._items.pop()
        except Exception as e:
            print(e)
    def isEmpty(self):
        v = False
        if self.size() == 0:
            v = True
        return v
    def clear(self):
        self._items =[]
