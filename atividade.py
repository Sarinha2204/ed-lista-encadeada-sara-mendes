class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None
        

class LinkList:
    def __init__ (self):
        self.head = None
        self._size = 0
        
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        
    def insert_end(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
            
        self._size += 1
    
    def remove(self, value):
        pointer = self.head
        previous = None
        
        while pointer:
            if pointer.data == value:
                
                if previous is None: 
                    self.head = pointer.next
                else:
                    previous.next = pointer.next
                    
                self._size -= 1
                return True
            
            previous = pointer 
            pointer = pointer.next
            
        return False
    
    def search(self, value):
        pointer = self.head
        
        while pointer:
            if pointer.data == value:
                return True
            pointer = pointer.next
            
        return False
    
    def print_list(self):
        pointer = self.head
        
        while pointer:
            print(pointer.data, end=" - ")
            pointer = pointer.next
            
        print("None")
        

lista = LinkList()

lista.insert_beginning(5)
lista.insert_end(7)
lista.insert_end(9)

lista.print_list()

print("List size:", lista.size())
print("Is it empty?", lista.is_empty())

print("Look for 7:", lista.search(7))

lista.remove(7)
lista.print_list()

print("Size after removal: ", lista.size())