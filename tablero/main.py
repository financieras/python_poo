from tablero import Tablero
from random import seed, randint
seed()

# Crear tablero
# dimensión del tablero dado por una matriz cuadrada nxn
n = 10
t = Tablero(n)
t.imprimir_tablero()
print()