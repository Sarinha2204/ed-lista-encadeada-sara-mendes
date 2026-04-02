
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


# Respostas:

# O erro principal é que o laço while percorre toda a lista, fazendo com que prev aponte para o último nó em vez do penúltimo.
# Após o laço, prev referencia o último nó (tail).  
# A instrução prev.next = None não remove corretamente o último elemento porque prev está apontando para o último nó, e não para o penúltimo. Assim, ao definir prev.next como None, na verdade estamos tentando acessar um atributo de um nó que já é o último, o que não tem efeito sobre a estrutura da lista.