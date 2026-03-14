class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:                   # Tem pelo menos um elemento?
            pointer = self.head         
            while(pointer.next):        # Percorrer a lista até next.None
                pointer = pointer.next
            pointer.next = Node(elem)   # Adiciona um novo elemento
        else:
            self.head = Node(elem)      # Adiciona o primeiro elemento
        self._size = self._size + 1

    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range") 
        
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range") 
    
lista = LinkList()
lista.append(5)
lista.append(7)
lista.append(9)
print(lista[1])
lista[1] = 20
print(lista[1])