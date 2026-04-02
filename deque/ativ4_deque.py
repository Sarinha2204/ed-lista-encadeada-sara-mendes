""" Atividade 4 — Casos de borda
Explique o que deveria acontecer em cada uma das situações abaixo ao executar remove_end():

O deque está vazio.
O deque possui apenas um elemento.
O deque possui dois elementos.
O deque possui vários elementos.
Para cada caso, descreva:

o valor retornado;
o novo valor de head;
o novo valor de tail;
o novo valor de _size. """

# Respostas:

# 1. IndexError("The queue is empty") 
# 2. O valor do único elemento é retornado, head e tail passam a ser None, e _size é atualizado para 0.
# 3. O valor do último elemento é retornado, head permanece o mesmo, tail passa a apontar para o primeiro elemento, e _size é atualizado para 1.
# 4. O valor do último elemento é retornado, head permanece o mesmo, tail passa a apontar para o penúltimo elemento, e _size é atualizado para o valor anterior menos um.
