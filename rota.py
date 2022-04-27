class Rota:
    def __init__(self, veiculo, rota, custo):
        self.veiculo = veiculo
        self.rota = rota
        self.custo = custo

    def exibirRota(self):
        print('     * Rotas')
        print(f'Veiculo: {self.veiculo}')
        print(f'Rota: {self.rota}')
        print(f'Custo: {self.custo}')