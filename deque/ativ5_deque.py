""" Atividade 5 — Análise de complexidade
Responda às perguntas abaixo.

Qual é a complexidade da operação add_start()?
Qual é a complexidade da operação add_end()?
Qual é a complexidade da operação remove_start()?
Qual é a complexidade da operação remove_end() nessa implementação?
Por que remove_end() não é O(1) em uma lista simplesmente encadeada? """


# Respostas:

# 1. A complexidade do add_start() é O(1) porque a operação envolve apenas a criação de um novo nó e a atualização dos ponteiros head e tail, independentemente do tamanho da lista.
# 2. A complexidade de add_end() é O(1) porque a operação envolve apenas a criação de um novo nó e a atualização dos ponteiros tail, independentemente do tamanho da lista.
# 3. A complexidade de remove_start() é O(1) porque a operação envolve apenas a atualização do ponteiro head para o próximo nó, independentemente do tamanho da lista.
# 4. A complexidade de remove_end() nessa implementação é O(n) porque é necessário percorrer toda a lista para encontrar o penúltimo nó, o que leva tempo proporcional ao número de elementos na lista.
# 5. remove_end() não é O(1) em uma lista simplesmente encadeada porque, para remover o último elemento, é necessário percorrer a lista desde o início até o penúltimo nó para atualizar o ponteiro tail, o que resulta em uma complexidade linear O(n).