class Tablero:
    def __init__(self, n=10):
        self.n = n   # dimensión del tablero nxn
        self.matrix = [['·']*n for _ in range(n)]
    def imprimir_tablero(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.matrix[i][j], end=" ")
            print()