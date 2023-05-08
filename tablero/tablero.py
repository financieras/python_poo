class Tablero:
    def __init__(self, dimension):
        self.dimension = dimension   # dimensión del tablero nxn
        self.matrix = [['·'] * dimension for _ in range(dimension)]
    def imprimir_tablero(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.matrix[i][j], end=" ")
            print()