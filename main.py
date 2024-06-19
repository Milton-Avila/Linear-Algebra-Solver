import numpy as np

class Transform:
    def __init__(self, vector) -> list:
        # Represents all the operation (Domain + Codomain)
        self.vector: list = vector

        # Domain Var
        self.dom: str = ''

        # Codoman Var
        self.cDom: str = ''

        # Codomain Dimension
        self.dim: list = [0]*2
        self.dicIndex: dict = {'x': 0,
                         'y': 1,
                         'z': 2}

        self.splitVector()
        self.createTransMatrix()
        
        if(self.matTrans != None):
            self.createMatrix()
            self.imgDimension()
            self.findKernel()
            self.isItBijector()
            self.isItOperator()

            if(self.isOperator):
                self.findEigvals()

    # Find Dimension Informing Domain & coDomain
    def dimensionFinder(self, vec: list) -> int:
        dim = 1

        for i in vec:
            if i == ',':
                dim += 1
        
        return dim

    def splitVector(self) -> None:
        vector = self.vector.replace(' ', '')

        # Splits Vector in Dom & coDom
        splited = vector.split('=')
        self.dom: list = splited[0]
        self.cDom: list = splited[1]

        # Rows = coDomain Dimension
        self.dim[0] = self.dimensionFinder(self.cDom)

        # Columns = Domain Dimension
        self.dim[1] = self.dimensionFinder(self.dom)

    def createTransMatrix(self) -> None:

        # Split in Individual Systems
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

            self.matTrans: list = matTrans

        except:
            self.matTrans = None

    def createMatrix(self) -> None:
        matrix = np.array(self.matTrans)
        matrix.shape = (self.dim)
        self.matrix: list = matrix
        
    def imgDimension(self) -> None:
        dimImg = np.linalg.matrix_rank(self.matrix)       
        self.dimImg: int = dimImg

    def findKernel(self) -> None:
        dimKernel = self.matrix.shape[1] - self.dimImg
        self.dimKernel: int = dimKernel

    def findEigvals(self) -> None:
        eighvals = np.linalg.eigvals(self.matrix)
        self.eighvals: list = eighvals

    def isItBijector(self) -> None:
        isBijector = self.dimImg == self.matrix.shape[0] and self.dimKernel == 0
        self.isBijector: bool = isBijector

    def isItOperator(self) -> None:
        isOperator = self.dim[0] == self.dim[1]
        self.isOperator: bool = isOperator

    # Console Print Data
    def showData(self) -> None:
        print(" Related Matrix: ")
        print(self.matrix)
        print(" Image Dimension: ", self.dimImg)
        print(" Kernel Dimension: ", self.dimKernel)

        if(self.isBijector): print(" Bijector: YES ")
        else: print(" Bijector: NO ")

        if(self.isOperator): 
            print(" Operator: YES ")
            print(" Eigenvalue: ")
            print(self.eighvals)

        else:
            print(" Operator: NO ")
    
    def getData(self) -> dict:
        if(self.matTrans != None):
            data = {'matrix': self.matrix, 'imageDimension': self.dimImg, 
                    'kernelDimension': self.dimKernel, 'isBijector': self.isBijector, 
                    'isOperator': self.isOperator}
            
            if(self.isOperator):
                data.update({'eighvals': self.eighvals})
                
            else:
                data.update({'eighvals': False})

        else:
            data = None

        return data


# Entry Sample:
'''
x, y, z = 5x + 4y + z, 2x + 6y + z, - 2x + 2y + 2z
'''

# Out Sample
'''
[x,y,z, x,y,z, x,y,z]
[2,0,0, 0,2,0, 0,0,5]
'''