from CVRP import CVRP
from leitor import Leitor

def construirMatrizNula(linhas, colunas):
    matriz = []
    for i in range(linhas):
        list.append(matriz, [0]*colunas)
    return matriz


arquivo = "NODE_COORD_SECTION.txt"
caminho = "\\Arquivos"
ler = Leitor(caminho, arquivo)
coordenadas, linhas, colunas = ler.lerArquivo()

arquivo = "DEMAND_SECTION.txt"
caminho = "\\Arquivos"
ler = Leitor(caminho, arquivo)
matrizArquivo = ler.lerArquivo()
colunas +=  matrizArquivo[2] - 1
demandas = matrizArquivo[0]

arquivo = "capacidadeVeiculo.txt"
caminho = "\\Arquivos"
ler = Leitor(caminho, arquivo)
matrizArquivo = ler.lerArquivo()
aux1 = matrizArquivo[0]
capacidadeVeiculo = int(aux1[0][0])

arquivo = "DEPOT_SECTION.txt"
caminho = "\\Arquivos"
ler = Leitor(caminho, arquivo)
matrizArquivo = ler.lerArquivo()
aux2 = matrizArquivo[0]
localDeposito = int(aux2[0][0]) - 1
capacidadeDeposito = int(aux2[0][1])

# matriz[cliente][coordenada1][coordenada2][demanda]
matriz = construirMatrizNula(linhas, colunas)
for i in range(linhas):
    for j in range(colunas):
        if j < colunas-1: matriz[i][j] = int(coordenadas[i][j])
        else: matriz[i][j] = int(demandas[i][1])
deposito = matriz[localDeposito]
deposito[3] = capacidadeDeposito
matriz.pop(localDeposito)

viagem = CVRP(matriz, deposito, capacidadeVeiculo)
viagem.criarRotas()
viagem.exibirRotas()
print('_'*50)