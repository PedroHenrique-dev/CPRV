class Deposito:
    def __init__(self, nome, coordenadaX, coordenadaY, quantidadeProdutos):
        self.nome = nome
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.quantidadeProdutos = quantidadeProdutos
        self.statusAtividade = True

    def status(self):
        print('     * Status do Depósito')
        print(f'Nome: {self.nome}')
        print(f'Capacidade: {self.quantidadeProdutos}')
        print(f'Local(coordenadas): ({self.coordenadaX},{self.coordenadaY})')
        print(f'Status da atividade: {self.statusAtividade}')

    def getNome(self): return self.nome
    
    def getCoordenadaX(self): return self.coordenadaX
    def getCoordenadaY(self): return self.coordenadaY

    def getQuantidadeProdutos(self): return self.quantidadeProdutos
    def setQuantidadeProdutos(self, valor): self.quantidadeProdutos = valor

    def getStatusAtividade(self): return self.statusAtividade
    def setStatusAtividade(self, status): self.statusAtividade = status
