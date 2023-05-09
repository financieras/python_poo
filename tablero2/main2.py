
from random import seed, randint
from termcolor import colored
seed()

class Tablero:
    def __init__(self, dimension, num_jugadores):
        self.dimension = dimension   # dimensión del tablero nxn
        self.matrix = [['·'] * dimension for _ in range(dimension)]
        self.jugadores = []
        self.letras_disponibles = [chr(i) for i in range(65, 91)]  # letras mayúsculas del alfabeto
        self.num_jugadores = num_jugadores
        self.celdas_comida = []

    def imprimir_tablero(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                caracter = self.matrix[i][j]
                if caracter == 'A':
                    print(colored(caracter,'red', attrs=["bold"]), end=" ")
                elif caracter == 'B':
                    print(colored(caracter, 'green', attrs=["bold"]), end=" ")
                elif caracter == 'C':
                    print(colored(caracter, 'yellow', attrs=["bold"]), end=" ")
                elif caracter == 'D':
                    print(colored(caracter, 'magenta', attrs=["bold"]), end=" ")
                else:
                    print(caracter, end=" ")

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
            if self.matrix[x][y] == '·' and (x, y) not in self.celdas_comida and not any(jugador.posicion == (x, y) for jugador in self.jugadores):
                self.matrix[x][y] = jugador.letra
                jugador.posicion = (x, y)
                break

    def agregar_comida(self, cantidad, valor):
        for i in range(cantidad):
            while True:
                x = randint(0, self.dimension - 1)
                y = randint(0, self.dimension - 1)
                if self.matrix[x][y] == '·' and (x, y) not in self.celdas_comida and not any(jugador.posicion == (x, y) for jugador in self.jugadores):
                    self.matrix[x][y] = str(valor)
                    self.celdas_comida.append((x, y))
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

    # Agregar comida al tablero
    t.agregar_comida(3, 1)
    t.agregar_comida(3, 2)
    t.agregar_comida(3, 3)
    t.agregar_comida(2, 4)
    t.agregar_comida(2, 5)
    t.agregar_comida(2, 6)
    t.agregar_comida(2, 7)
    t.agregar_comida(2, 8)
    t.agregar_comida(1, 9)

    # Imprimir tablero con jugadores y comida
    t.imprimir_tablero()
