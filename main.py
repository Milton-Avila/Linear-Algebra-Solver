import numpy as np

class Transformacao:
    def __init__(self, vector):
        # Representa toda a Equação coletada no Input ( 'Dominio + Contra-Domínio' )
        self.vector = vector
        # Variável que vai conter apenas o Domínio da Equação
        self.dom = ''
        # Variável que vai conter apenas o Contra-Domínio da Equação
        self.cDom = ''
        # Variável que contém a dimensão do contra-domínio
        self.dim = [0]*2
        self.dicIndex = {'x': 0,
                         'y': 1,
                         'z': 2}



        self.separar_vetor()
        self.montar_matriz_trans()
        if(self.matTrans != None):
            self.monta_matriz()
            self.dimensao_imagem()
            self.dimensao_kernel()
            self.bijetora()
            self.operador()
            if(self.operador): self.acha_autovalores()
       
            
        

    # É informado a dimensão do *Domínio* e *Contra Domínio*
    def descobre_dimensao(self, vec: list):
        dim = 1

        for i in vec:
            if i == ',':
                dim += 1
        
        return dim

    # Função responsável por separar o vetor 
    def separar_vetor(self):
        vector = self.vector.replace(' ', '')

        # O vetor é dividido entre dom e cdom
        self.dom = vector.split('=')[0]
        self.cDom = vector.split('=')[1]

        # O número de linhas é definido pela dimensão do contra domínio
        self.dim[0] = self.descobre_dimensao(self.cDom)

        # O número de colunas é definido pela dimensão do domínio
        self.dim[1] = self.descobre_dimensao(self.dom)

    # Função responsável por criar a matriz de transformação Linear
    def montar_matriz_trans(self):
        # Separar em sistemas individuais
        systems = (self.cDom.split(","))
        matTrans = [0]* np.prod(self.dim)
        count, count2 = 0, False
        value, string = 1, '0'

        try:    
            for vec in systems:
                if(count2):
                    raise Exception
                for coor in vec:
                    if coor == '*':
                        raise Exception
                    elif coor not in 'xyz+-':
                        string += coor
                        count2 = True
                    elif coor not in '+-':
                        count2 = False
                        if string == '0':
                            string += '1'
                        value *= int(string)
                        matTrans[self.dicIndex.get(coor)+count] = int(value)
                        value = 1
                        string = '0'
                    elif coor not in '+':
                        if(count2):
                            raise Exception
                        value = -1
                    else:
                        if(count2):
                            raise Exception
                
                count += self.dim[1]

            self.matTrans = matTrans

        except:
            self.matTrans = None

    # Função responsável por montar a matriz
    def monta_matriz(self):
        matriz = np.array(self.matTrans)
        matriz.shape = (self.dim)
        self.matriz = matriz

    # Função responsável por encontrar a dimensão da imagem
    def dimensao_imagem(self):
        dimImg = np.linalg.matrix_rank(self.matriz)       
        self.dimImg = dimImg

    # Função responsável por encontrar a dimensão do Kernel/núcleo
    def dimensao_kernel(self):
        # Dimensão do kernel (espaço nulo)
        dimKernel = self.matriz.shape[1] - self.dimImg
        self.dimKernel = dimKernel

    # Função que determina se a matriz da transformação Linear é bijetora
    def bijetora(self):
        # Verifica se é bijetora
        bijetora = self.dimImg == self.matriz.shape[0] and self.dimKernel == 0
        self.bijetora = bijetora

    # Função que determina se a matriz da transformação Linear é operadora
    def operador(self):
        operador = self.dim[0] == self.dim[1]
        self.operador = operador

    # Função que encontra os autovalores
    def acha_autovalores(self):
        autovalores = np.linalg.eigvals(self.matriz)
        self.autovalores = autovalores

    # Função teste que mostra os dados 
    def mostra_dados(self):
        print(" MATRIZ RELACIONADA: ")
        print(self.matriz)
        print(" DIMENSÃO DA IMAGEM: ", self.dimImg)
        print(" DIMENSÃO DO KERNEL: ", self.dimKernel)
        if(self.bijetora): print(" É BIJETORA ")
        else: print(" NÃO É BIJETORA ")

        if(self.operador): 
            print(" É OPERADOR: ")
            print(" AUTOVALORES: ")
            print(self.autovalores)
        else:
            print(" NÃO É OPERADOR ")
    
    # Função que pega os dados
    def get_dados(self):
        if(self.matTrans != None):
            lista_dados = [self.matriz, self.dimImg, 
                        self.dimKernel, self.bijetora, 
                        self.operador]
            if(self.operador):
                lista_dados.append(self.autovalores)
            else:
                lista_dados.append(False)
        else:
            lista_dados = None
        return lista_dados



# Exemplo de Entrada:
'''
x, y, z = 5x + 4y + z, 2x + 6y + z, - 2x + 2y + 2z
'''

# Exemplo de string output
'''
[x,y,z, x,y,z, x,y,z]
[2,0,0, 0,2,0, 0,0,5]
'''