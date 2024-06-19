class Stack:
	def __init__(self):
		self._items = []


	def __str__(self):
		s ='('
		for el in self._items:
			s+=str(el)+','
		if s.endswith(','): 
			s=s[:-1]
		s+=')'
		return s
	def push(self,e):
		self._items.append(e)
		
	def pop(self):
		self._items.pop()
		
		
	def top(self):
		return self._items[-1]
	
	def size(self):
		return len(self._items)
		
	def isEmpty(self):
		v = False
		if self.size()==0: # or use if len(self._items)==0
			v = True
		return v
		
	def clear(self):
		self._items = []

