import LinkedList
class Stack:
	def __init__(self):
		self._items = LinkedList()
		

	def __str__(self):
		return self._items.__str__()
	def push(self,e):
		self._items.addLast(e)
		
	def pop(self):
		self._items.removeFirst()
		
		
	def top(self):
		return self._items.first()
	
 
 
	def size(self):
		return self._items.size()

		
	def isEmpty(self):
		self._items.isEmpty()
  
		
	def clear(self):
		self._items.reset()

