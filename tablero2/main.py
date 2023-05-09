from random import seed, randint
seed()

class Tablero:
    def __init__(self, dimension, num_jugadores):
        self.dimension = dimension   # dimensión del tablero nxn
        self.matrix = [['·'] * dimension for _ in range(dimension)]
        self.jugadores = []
        self.letras_disponibles = [chr(i) for i in range(65, 91)]  # letras mayúsculas del alfabeto
        self.num_jugadores = num_jugadores

    def imprimir_tablero(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.matrix[i][j], end=" ")
            print()

    def agregar_jugador(self, jugador):
        if len(self.jugadores) < self.num_jugadores:
            letra = self.letras_disponibles.pop(0)
            jugador.letra = letra
            self.jugadores.append(jugador)
            self.actualizar_tablero(jugador)
            #print(f"El jugador {jugador.nombre} ha sido agregado al tablero con la letra {letra}")
        else:
            print("No se pueden agregar más jugadores al tablero")

    def actualizar_tablero(self, jugador):
        while True:
            x = randint(0, self.dimension - 1)
            y = randint(0, self.dimension - 1)
            if self.matrix[x][y] == '·':
                self.matrix[x][y] = jugador.letra
                jugador.posicion = (x, y)
                break

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = None
        self.letra = None

if __name__ == "__main__":
    # Crear tablero
    dimension = 10   # tablero dado por una matriz cuadrada nxn
    num_jugadores = 4
    t = Tablero(dimension, num_jugadores)

    # Crear lista de nombres de jugadores
    nombres_jugadores = [chr(i) for i in range(65, 65+num_jugadores)]

    # Agregar jugadores al tablero
    jugadores = []
    for nombre in nombres_jugadores:
        jugador = Jugador(nombre)
        t.agregar_jugador(jugador)
        jugadores.append(jugador)

    # Imprimir tablero con jugadores
    t.imprimir_tablero()

