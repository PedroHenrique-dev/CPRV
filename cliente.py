class Cliente:
    def __init__(self, nome, coordenadaX, coordenadaY, demanda, statusAtividade):
        self.nome = nome
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.demanda = demanda
        self.statusAtividade = statusAtividade
    
    def status(self):
        print('     * Status do Cliente')
        print(f'Nome: {self.nome}')
        print(f'Demanda: {self.demanda}')
        print(f'Local(coordenadas): ({self.coordenadaX},{self.coordenadaY})')
        print(f'Status da atividade: {self.statusAtividade}')

    def getNome(self): return self.nome
    
    def getCoordenadaX(self): return self.coordenadaX
    def getCoordenadaY(self): return self.coordenadaY

    def getDemanda(self): return self.demanda
    def setDemanda(self, valor): self.demanda = valor

    def getStatusAtividade(self): return self.statusAtividade
    def setStatusAtividade(self, status): self.statusAtividade = status