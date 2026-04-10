class Processo:
    def __init__(self, pid, tempo_execucao):
        self.pid = pid
        self.tempo_restante = tempo_execucao
        self.proximo = None
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, processo):
        if self.fim is None:
            self.inicio = self.fim = processo
        else:
            self.fim.proximo = processo
            self.fim = processo

    def dequeue(self):
        if self.esta_vazia():
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        removido.proximo = None
        return removido
    def round_robin(self, quantum):
        tempo_total = 0

        print("Início da simulação:\n")

        while not self.esta_vazia():
            processo = self.dequeue()

            print(f"Processo {processo.pid} executando...")

            if processo.tempo_restante > quantum:
                tempo_total += quantum
                processo.tempo_restante -= quantum

                print(f" -> Executou {quantum}, resta {processo.tempo_restante}")

                self.enqueue(processo)
            else:
                tempo_total += processo.tempo_restante

                print(f" -> Finalizado (usou {processo.tempo_restante})")
                processo.tempo_restante = 0

            print(f"Tempo total: {tempo_total}\n")

        print("Todos os processos finalizaram.")

fila = Fila()

fila.enqueue(Processo("P1", 10))
fila.enqueue(Processo("P2", 4))
fila.enqueue(Processo("P3", 6))

quantum = 3

fila.round_robin(quantum)
