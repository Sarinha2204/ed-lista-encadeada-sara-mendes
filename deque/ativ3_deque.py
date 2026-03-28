
""" Atividade 3 — Identificação do erro lógico
Analise a implementação abaixo.

def remove_end(self):
    if self._size == 0:
        raise IndexError("The queue is empty")    

    elem = self.tail.data
    pointer = self.head
    prev = None

    while pointer:
        prev = pointer
        pointer = pointer.next

    prev.next = None
    self.tail = prev
    self._size = self._size - 1

    return elem
Responda:

Qual é o erro lógico principal dessa implementação?
Após o laço, prev referencia qual nó?
Por que a instrução prev.next = None não remove corretamente o último elemento nesse caso?
O que deveria ser encontrado antes de atualizar self.tail? """