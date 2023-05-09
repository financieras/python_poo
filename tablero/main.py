from tablero import Tablero
from jugador import Jugador
from random import seed, randint
seed()

if __name__ == "__main__":
    # Crear tablero
    dimension = 10   # tablero dado por una matriz cuadrada nxn
    t = Tablero(dimension)
    t.imprimir_tablero()
    print()