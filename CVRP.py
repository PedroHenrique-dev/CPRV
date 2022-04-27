from veiculo import Veiculo
from deposito import Deposito
from cliente import Cliente
from rota import Rota
from math import pow, sqrt

class CVRP:
    def __init__(self, matriz, deposito, capacidadeVeiculo):
        self.deposito = Deposito(nome('d', deposito[0]), deposito[1], deposito[2], deposito[3])
        self.cliente = salvarClientes(matriz)
        self.rotas = []
        self.capacidadeVeiculo = capacidadeVeiculo
        self.veiculo = []

    def exibirVeiculos(self):
        for i in range(len(self.veiculo)):
            self.veiculo[i].status(self.capacidadeVeiculo)
            print('_'*50)

    def exibirRotas(self):
        for i in range(len(self.rotas)):
            self.rotas[i].exibirRota()
            print('_'*50)
    
    def statusDeposito(self): self.deposito.status()

    def statusCliente(self, posicao): self.cliente[posicao].status()
    
    def statusClientes(self):
        for i in range(len(self.cliente)):
            self.cliente[i].status()
            print('_'*50)

    def criarRotas(self):
        contadorVeiculos = 0
        teste = testeAtendimento(self.cliente)
        while self.deposito.getStatusAtividade() != False and teste != False:
            caminho = []
            self.veiculo.append(Veiculo(nome('v', contadorVeiculos+1), self.capacidadeVeiculo))
            atualizar = saidaDeposito(self.deposito, self.veiculo[contadorVeiculos], self.cliente)
            if atualizar != []:
                caminho.append(atualizar[0][0])
                self.deposito = atualizar[1]
                self.veiculo[contadorVeiculos].setCapacidade(atualizar[2])
                self.veiculo[contadorVeiculos].setStatusAtividade(atualizar[3])
                self.cliente[atualizar[6]].setDemanda(atualizar[4])
                self.cliente[atualizar[6]].setStatusAtividade(atualizar[5])
                teste = testeAtendimento(self.cliente)
                while self.veiculo[contadorVeiculos].getStatusAtividade() != False and teste != False:
                    atualizar = verticeVertice(caminho, self.veiculo[contadorVeiculos], self.cliente)
                    if atualizar == []: self.veiculo[contadorVeiculos].setStatusAtividade(False)
                    else:
                        self.veiculo[contadorVeiculos].setCapacidade(atualizar[1])
                        self.veiculo[contadorVeiculos].setStatusAtividade(atualizar[2])
                        self.cliente[atualizar[5]].setDemanda(atualizar[3])
                        self.cliente[atualizar[5]].setStatusAtividade(atualizar[4])
                        teste = testeAtendimento(self.cliente)
                caminho, self.deposito, self.veiculo[contadorVeiculos], self.cliente = voltarDeposito(caminho, self.deposito, self.veiculo[contadorVeiculos], self.cliente)
                dados = dadosRota(caminho)
                rota = Rota(self.veiculo[contadorVeiculos].getNome(), dados[0], dados[1])
                self.rotas.append(rota)
                contadorVeiculos += 1

# Vertice -> Vertice +++++++++++++++++++++++++++++++++++++++++++++++++++
def verticeVertice(caminho, veiculo, cliente):
    atual = posicao(caminho[len(caminho)-1][2], cliente)
    escolha = menorDistancia(cliente[atual], cliente, veiculo)
    if escolha == []: return []
    caminho.append(aresta(veiculo.getNome(), cliente[atual].getNome(), cliente[escolha[0]].getNome(), escolha[1]))
    veiculoClientes = atualizarDados(cliente[escolha[0]], veiculo)
    return caminho, veiculoClientes[0], veiculoClientes[1], veiculoClientes[2], veiculoClientes[3], escolha[0]

# Deposito +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def saidaDeposito(deposito, veiculo, cliente):
    caminho = []
    if veiculo.getCapacidade() > deposito.getQuantidadeProdutos():
        veiculo.setCapacidade(deposito.getQuantidadeProdutos())
    deposito.setQuantidadeProdutos(deposito.getQuantidadeProdutos()-veiculo.getCapacidade())
    if deposito.getQuantidadeProdutos() == 0:
        deposito.setStatusAtividade(False)
    escolha = menorDistancia(deposito, cliente, veiculo)
    if escolha == []: return []
    caminho.append(aresta(veiculo.getNome(), deposito.getNome(), cliente[escolha[0]].getNome(), escolha[1]))
    veiculoClientes = atualizarDados(cliente[escolha[0]], veiculo)
    return caminho, deposito, veiculoClientes[0], veiculoClientes[1], veiculoClientes[2], veiculoClientes[3], escolha[0]
    
def distanciaVoltar(atual, deposito):
    distancia = 0
    x = coordenada(atual)
    y = coordenada(deposito)
    distancia = euclidiana(x, y)
    return distancia

def voltarDeposito(caminho, deposito, veiculo, cliente):
    atual = posicao(caminho[len(caminho)-1][2], cliente)
    distancia = distanciaVoltar(cliente[atual], deposito)
    caminho.append(aresta(veiculo.getNome(), cliente[atual].getNome(), deposito.getNome(), distancia))
    if veiculo.getCapacidade() > 0 :
        deposito.setQuantidadeProdutos(deposito.getQuantidadeProdutos()+veiculo.getCapacidade())
        veiculo.setCapacidade(0)
        veiculo.setStatusAtividade(False)
    return caminho, deposito, veiculo, cliente

# Clientes +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def salvarClientes(matriz):
    cliente = []
    for i in range(len(matriz)): cliente.append(Cliente(nome('c', matriz[i][0]), matriz[i][1], matriz[i][2], matriz[i][3], True))
    return cliente

def testeAtendimento(clientes):
    for i in range(len(clientes)):
        if clientes[i].getStatusAtividade() == True: return True
    return False

# Funções ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def atualizarDados(cliente, veiculo):
    if cliente.getDemanda() < veiculo.getCapacidade():
        veiculo.setCapacidade(veiculo.getCapacidade() - cliente.getDemanda())
        cliente.setDemanda(0)
        cliente.setStatusAtividade(False)
        if veiculo.getCapacidade() == 0: veiculo.setStatusAtividade(False)
    else:
        cliente.setDemanda(cliente.getDemanda() - veiculo.getCapacidade())
        veiculo.setCapacidade(0)
        veiculo.setStatusAtividade(False)
        if cliente.getDemanda() == 0: cliente.setStatusAtividade(False)
    return veiculo.getCapacidade(), veiculo.getStatusAtividade(), cliente.getDemanda(), cliente.getStatusAtividade()

def menorDistancia(atual, cliente, veiculo):
    distancias,ligações = [],[]
    x = coordenada(atual)
    for i in range(len(cliente)):
        if cliente[i].getStatusAtividade() == True and cliente[i].getDemanda() < veiculo.getCapacidade():
            ligações.append(i)
            y = coordenada(cliente[i])
            distancias.append(euclidiana(x, y))
    if ligações == []: return []
    menor = 40000
    for i in range(len(distancias)):
        if menor > distancias[i]:
            menor = distancias[i]
            posicao = i
    return ligações[posicao], menor

def dadosRota(caminho):
    custo = 0
    vertices = []
    for i in range(len(caminho)): 
        vertices.append(caminho[i][1])
        custo += caminho[i][3]
    vertices.append(caminho[0][1])
    return vertices, custo

def posicao(valor, cliente):
    for i in range(len(cliente)):
        if valor == cliente[i].getNome(): return i

def coordenada(local): return local.getCoordenadaX(), local.getCoordenadaY()

def euclidiana(x, y): return sqrt(pow(x[0]-y[0],2)+pow(x[1]-y[1],2))

def aresta(veiculo, vertice1, vertice2, custo): return veiculo, vertice1, vertice2, custo

def nome(cigla, i): return cigla+str(i)