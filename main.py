import numpy as np

class MatrizTrans:
    def __init__(self, vector: str):
        self.vector = vector
        self.dom = ''
        self.cDom = ''
        self.dim = [0]*2
        self.dicIndex = {'x': 0,
                         'y': 1,
                         'z': 2}

        self.separar_vetor()
        self.montar_matriz_trans()

    # É informado a dimensão do *Domínio* e *Contra Domínio*
    def descobre_dimensao(self, vec):
        dim = 1

        for i in vec:
            if i == ',':
                dim += 1
        
        return dim

    def separar_vetor(self):
        vector = self.vector.replace(' ', '')

        # O vetor é dividido entre dom e cdom
        self.dom = vector.split('=')[0]
        self.cDom = vector.split('=')[1]

        # O número de linhas é definido pela dimensão do contra domínio
        self.dim[0] = self.descobre_dimensao(self.cDom)

        # O número de colunas é definido pela dimensão do domínio
        self.dim[1] = self.descobre_dimensao(self.dom)

    def montar_matriz_trans(self):
        # Separar em sistemas individuais
        systems = (self.cDom.split(","))
        matTrans = [0]* np.prod(self.dim)
        count = 0
        value, string = 1, '0'

        try:    
            for vec in systems:
                for coor in vec:
                    if coor == '*':
                        raise Exception
                    elif coor not in 'xyz+-':
                        string += coor
                    elif coor not in '+-':
                        if string == '0':
                            string += '1'
                        value *= int(string)
                        matTrans[self.dicIndex.get(coor)+count] = int(value)
                        value = 1
                        string = '0'
                    elif coor not in '+':
                        value = -1
                
                count += self.dim[1]

            self.matTrans = matTrans

        except:
            self.matTrans = None

            
        print(self.matTrans)

    def monta_matriz(self):
        matriz = np.array(self.matTrans)
        matriz.shape = (self.dim)
        self.matriz = matriz

    def dimensao_imagem(self):
        dimImg = np.linalg.matrix_rank(self.matriz)       
        self.dimImg = dimImg

    def dimensao_kernel(self):
        # Dimensão do kernel (espaço nulo)
        dimKernel = self.matriz.shape[1] - self.dimImg
        self.dimKernel = dimKernel

    def bijetora(self):
        # Verifica se é bijetora
        bijetora = self.dimImg == self.matriz.shape[0] and self.dimKernel == 0
        self.bijetora = bijetora

    def operador(self):
        operador = self.dimImg == self.dimKernel
        self.operador = operador

    def acha_autovalores(self):
        autovalores = np.linalg.eigvals(self.matriz)
        self.autovalores = autovalores

# Entrada:
# T: (x, y) = (x+y, y)
input_str = 'x, y, z = 5x + 4y + z, 2x * 6y, - 2x + 2y + 2z'

Matriz = MatrizTrans(input_str)

# Exemplo de string output
'''
[x,y,z, x,y,z, x,y,z]
[2,0,0, 0,2,0, 0,0,5]
'''