from math import pow, sqrt

def posicao(valor, clientes):
    for i in range(len(clientes)):
        if valor == clientes[i][0]: return i

def euclidiana(x, y): return sqrt(pow(x[0]-y[0],2)+pow(x[1]-y[1],2))
    
def coordenada(matriz): return matriz[1], matriz[2]

def distanciaVoltar(atual, deposito):
    distancia = 0
    x = coordenada(atual)
    y = coordenada(deposito)
    distancia = euclidiana(x, y)
    return distancia

def menorDistancia(atual, clientes, veiculo):
    distancias,ligações = [],[]
    x = coordenada(atual)
    for i in range(len(clientes)):
        if clientes[i][4] == True and clientes[i][3] < veiculo[1]:
            ligações.append(i)
            y = coordenada(clientes[i])
            distancias.append(euclidiana(x, y))
    if ligações == []: return []
    menor = 40000
    for i in range(len(distancias)):
        if menor > distancias[i]:
            menor = distancias[i]
            posicao = i
    return ligações[posicao], menor

def aresta(veiculo, vertice1, vertice2, custo): return veiculo, vertice1, vertice2, custo

def atualizarDados(escolha, veiculo, clientes):
    if clientes[escolha[0]][3] < veiculo[1]:
        veiculo[1] -= clientes[escolha[0]][3]
        clientes[escolha[0]][3] = 0
        clientes[escolha[0]][4] = False
        if veiculo[1] == 0: veiculo[2] = False
    else:
        clientes[escolha[0]][3] -= veiculo[1]
        veiculo[1] = 0
        veiculo[2] = False
        if clientes[escolha[0]][3] == 0: clientes[escolha[0]][4] = False
    return veiculo, clientes

def saidaDeposito(deposito, veiculo, clientes):
    caminho = []
    if capacidade <= deposito[3]: veiculo[1] = capacidade
    else: veiculo[1] = deposito[3]
    veiculo[2] = True
    deposito[3] -= veiculo[1]
    escolha = menorDistancia(deposito, clientes, veiculo)
    if escolha == []: return []
    caminho.append(aresta(veiculo[0], deposito[0], clientes[escolha[0]][0], escolha[1]))
    veiculoClientes = atualizarDados(escolha, veiculo, clientes)
    return caminho, deposito, veiculoClientes[0], veiculoClientes[1]

def verticeVertice(caminho, veiculo, clientes):
    atual = posicao(caminho[len(caminho)-1][2], clientes)
    escolha = menorDistancia(clientes[atual], clientes, veiculo)
    if escolha == []: return []
    caminho.append(aresta(veiculo[0], clientes[atual][0], clientes[escolha[0]][0], escolha[1]))
    veiculoClientes = atualizarDados(escolha, veiculo, clientes)
    return caminho, veiculoClientes[0], veiculoClientes[1]

def voltarDeposito(caminho, deposito, veiculo, clientes):
    atual = posicao(caminho[len(caminho)-1][2], clientes)
    escolha = distanciaVoltar(clientes[atual], deposito)
    caminho.append(aresta(veiculo[0], clientes[atual][0], deposito[0], escolha))
    if veiculo[1] > 0 :
        deposito[3] += veiculo[1]
        veiculo[1] = 0
        veiculo[2] = False
    return caminho, deposito, veiculo, clientes

def status(deposito, clientes, caminho):
    print(deposito)
    print(clientes)
    print(caminho)

def testeAtendimento(clientes):
    for i in range(len(clientes)):
        if clientes[i][4] == True: return True
    return False

def guardarCaminho(caminho):
    custo = 0
    vertices = []
    for i in range(len(caminho)):
        veiculo = caminho[0][0]
        vertices.append(caminho[i][1])
        custo += caminho[i][3]
    vertices.append(caminho[0][1])
    return veiculo, vertices, custo

def nomeVeiculo(cigla, i): return cigla+str(i)

#veiculo = [id, capacidade, atividade]
capacidade = 10
veiculo = ['', 0, True]
#clientes = [id, coordenada1, coordenada2, demanda, atividade]
clientes = [['c1', 3, 3, 10, True],
            ['c2', 1, 1, 1, True],
            ['c3', 6, 6, 4, True],
            ['c4', 9, 9, 1, True]]
#deposito = [id, coordenada1, coordenada2, quantidadeProdutos, atividade]
deposito = ['d1', 0, 0, 20, True] 
caminhos = []
contadorVeiculos = 1
dados = []
teste = testeAtendimento(clientes)
while deposito[3] > 0 and teste != False:
    veiculo[0] = nomeVeiculo('v', contadorVeiculos)
    atualizar = saidaDeposito(deposito, veiculo, clientes)
    if atualizar != []:
        caminho = atualizar[0]
        teste = testeAtendimento(clientes)
        while veiculo[2] != False and teste != False:
            atualizar = verticeVertice(caminho, veiculo, clientes)
            if atualizar == []: veiculo[2] = False
            else:
                caminho = atualizar[0]
                veiculo = atualizar[1]
                clientes = atualizar[2]
                teste = testeAtendimento(clientes)
        voltarDeposito(caminho, deposito, veiculo, clientes)
        dados.append(guardarCaminho(caminho))
        contadorVeiculos += 1
print(dados)
