class Leitor:
    def __init__(self, caminho, arquivo):
        #Pegar o caminho do arquivo que contém a matriz
        self.arquivo = caminho + '\\' + arquivo
    
    def lerArquivo(self):
        #Ler o arquivo com a matriz e retornar a matriz
        matriz = []
        arquivo = open(self.arquivo,'r')
        print(self.arquivo)
        linha = arquivo.readline()
        linhas = 0
        colunas = 0
        while linha != '':
            elementos = linha.split()
            for i in range(len(elementos)):
                elementos[i] = float(elementos[i])
                colunas += 1
            matriz.append(elementos)
            linhas += 1
            linha = arquivo.readline()
        colunas = int(colunas/linhas)
        arquivo.close()
        return matriz, linhas, colunas