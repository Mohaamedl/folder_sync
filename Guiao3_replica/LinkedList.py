
class Node:
    def __init__(self, infoval=None):
        self.info = infoval
        self.link = None


class LinkedList:
    def __init__(self):
        '''Creation of the linked list'''
        self.head = None
        self.tail  = None
        self.nitems = 0

    def addFirst(self,element):
        '''Add at the beginning'''

        # create new node
        new_node = Node(element)

        # connect new node to current first node
        new_node.link = self.head

        # update first (to the address of new node)   
        self.head = new_node

        # if empty update last (with new node address)
        if self.tail is None:
            self.tail = new_node

        # increase number of items
        self.nitems += 1

    def addLast(self, element):
        '''Add element at the end'''
        
        # create new node
        new_node = Node(element)

        # update first if empty
        if self.head is None:
            self.head = new_node
        else:  # connect new node at end
            self.tail.link = new_node

        # update last (to the address of new node)     
        self.tail = new_node
        
        # increase number of items
        self.nitems += 1


    def first(self):
        '''Return first element'''
        assert not self.isEmpty(), "ERROR! Empty list" 

        first_node = self.head   # node at beginning

        return first_node.info
         
    def removeFirst(self):
        '''Delete first element'''
        assert not self.isEmpty(), "ERROR! Empty list"  

        # change head to the second node in list
        self.head = self.head.link 
        self.nitems -= 1
         
             

    def __len__(self):
        '''Return number of elements in the linked list'''
        return self.nitems

    def size(self):
        '''Return number of elements in the linked list'''
        return self.__len__()


    def reset(self):
        '''Reset the linked list'''
        self.__init__()

    def isEmpty(self):
        '''Return True if linked list is empty'''
        return self.nitems == 0

    def __str__(self):
        '''Return a string with linked list friendly representation'''
        printval = self.head
        str1 = ""
        while printval is not None:
            str1 = str1 + f"{repr(printval.info)} -> "
            printval = printval.link
        str1 = str1 + f"{printval}"
        return str1
## test
def test():
    linkedlist1 = LinkedList()
    
    print(linkedlist1, "; len:", len(linkedlist1)) # invokes __len__()

    #linkedlist1.first()

    linkedlist1.addLast("Monday") 
    linkedlist1.addLast("Tuesday")
    linkedlist1.addLast("Wednesday")
    linkedlist1.addLast(['a','b','c'])
    linkedlist1.addFirst("Sunday")
    print(linkedlist1, "; len:", len(linkedlist1)) # invokes __len__()
    
    linkedlist1.removeFirst()
 
    print(linkedlist1, "; len:", len(linkedlist1)) # invokes __len__()

    linkedlist1.reset()
    print(linkedlist1, "; len:", len(linkedlist1)) # invokes __len__()

if __name__ == "__main__":
    test()
