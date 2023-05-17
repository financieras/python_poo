#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sin usar POO programamos un tablero, unos jugadores y una comida.
Los jugadores se mueven por el tablero y van atrapando la comida
que da puntos. Gana el que más puntos tenga cuando se acaba la comida"""

from random import seed, randint
seed()

def imprime_matriz():
    """Imprime el tablero en forma de matriz"""
    for fila in range(len(matriz[0])):
        print(*matriz[fila])

def generar_jugadores(num_jugadores):
    """Genera aleatoriamente los jugadores automaticamete asignándoles 
    una letra como nombre y una posición aleatoria única"""
    for i in range(num_jugadores):
        letra = LETRAS[i]
        x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        while matriz[x][y] != '·':
            x, y = randint(0, len(matriz)-1), randint(0, len(matriz)-1)
        matriz[x][y] = letra

def generar_comida(num_comida):
    """Generamos aleatoriamente posiciones únicas de comida en el tablero
    con un valor aleatorio que indica la cantidad de comida en esa celda."""
    for _ in range(num_comida):
        x, y = randint(0, len(matriz)-1), randint(0, len(matriz)-1)
        while matriz[x][y] != '·':
            x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        matriz[x][y] = str(randint(1, 9))    # la cantidad de comida es aleatoria, como str

def contar_comida():
    """Cuenta el número de celdas con comida que existen en la matriz"""
    contador = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if (matriz[fila][columna]).isnumeric():
                contador += 1
    return contador

def quien_comienza():
    """Devuelve el primer jugador que comienza el juego, como index"""
    primer_jugador = randint(0, NUM_JUGADORES-1)
    primera_letra = LETRAS[primer_jugador]
    print("Comienza jugando", primera_letra)    # imprime la letra del premer jugador
    return primer_jugador   # como index

def localiza(jugador):
    """Devuelve la posición de la letra del jugador en el tablero"""
    for y in range(len(matriz)):                # y da la posición vertical (son las filas)
        for x in range(len(matriz[0])):         # x da la posición horizontal (son las columnas)
            if matriz[y][x] == LETRAS[jugador]:
                return x, y
            
def posibilidades(jugador):
    """Devuelve un vector con cuatro posiciones True o False
    que indican si se puede mover el jugador o no en esa dirección.
    Las direcciones son en este orden: UP, DOWN, LEFT, RIGHT"""
    x, y = localiza(jugador)
    # Inicializamos el array con las 4 direcciones en True
    arr_posibilidades = [True] * 4  # [Up, Down, Left, Right] las 4 direcciones en ese orden
    # Los 'False' pueden ser por dos motivos:
    # Motivo 1. nos salimos del tablero
    if y == 0: arr_posibilidades[0] = False   # UP
    if y == DIM-1: arr_posibilidades[1] = False   # DOWN
    if x == 0: arr_posibilidades[2] = False   # LEFT
    if x == DIM-1: arr_posibilidades[3] = False   # RIGHT
    # Motivo 2. la celda de destino ya está ocupada por otro jugador
    if y > 0 and matriz[x][y-1] in LETRAS: arr_posibilidades[0] = False   # UP
    if y < DIM-1 and matriz[x][y+1] in LETRAS: arr_posibilidades[1] = False   # DOWN
    if x > 0 and matriz[x-1][y] in LETRAS: arr_posibilidades[2] = False   # LEFT
    if x < DIM-1 and matriz[x+1][y] in LETRAS: arr_posibilidades[3] = False   # RIGHT
    return arr_posibilidades

def elegir_mover(jugador, arr_posibilidades):
    """Elige la dirección a mover del jugador considerando las posiciones
     a las que está permitido moverse dadas por el vector arr_posibilidades
    Elegimos a que posición contígua movernos dentro de los True que da el vector arr_posibilidades
    Si hay varias celdas con comida dadas por un valor numérico nos movemos al mayor
    Si solo hay un valor numérico elegimos la dirección hacia esa celda con comida
    Si no hay ningún valor numérico elegimos aleatoriamente alguno de los True"""
    x, y = localiza(jugador)
    print(f"{LETRAS[jugador]} está en (x,y)=({x},{y}) y su arr_posibilidades es {arr_posibilidades}")
    mi_max = 0  # si la celda contigua es numérica es que hay comida y buscamos su máximo
    if arr_posibilidades[0] and matriz[x][y-1].isnumeric(): mi_max = max(mi_max, eval(matriz[x][y-1])); return 0  # UP
    if arr_posibilidades[1] and matriz[x][y+1].isnumeric(): mi_max = max(mi_max, eval(matriz[x][y+1])); return 1  # DOWN
    if arr_posibilidades[2] and matriz[x-1][y].isnumeric(): mi_max = max(mi_max, eval(matriz[x-1][y])); return 2  # LEFT
    if arr_posibilidades[3] and matriz[x+1][y].isnumeric(): mi_max = max(mi_max, eval(matriz[x+1][y])); return 3  # RIGHT
    if mi_max == 0: # Si no hay comida contígua entonces “elegir un True aleatorio”
        direccion_index = randint(0, 3)
        while arr_posibilidades[direccion_index] != True:
            direccion_index = randint(0, DIM-1)
        return direccion_index

def mover(jugador, direccion_index):
    print(f"{LETRAS[jugador]} se mueve hacia {direccion_index}")


def jugando():
    """Lógica principal del juego. Bucle while que repite tiradas hasta
    que el juego finaliza al comerse la última comida del tablero"""
    turno = 1
    while contar_comida() > 0:
        print("\tTurno", turno, "\n")
        for i in range(NUM_JUGADORES):
            # Si el primer jugador es 2, los valores de jugador son 2,3,0,1
            jugador = (i+primer_jugador) % NUM_JUGADORES    # como index
            print("Mueve", LETRAS[jugador])
            arr_posibilidades= posibilidades(jugador)
            if not any(arr_posibilidades):  # si el array es [False, False, False, False]
                print(f"El jugador {LETRAS[jugador]} está bloquedao y pasa al siguiente")
                continue
            direccion_index = elegir_mover(jugador, arr_posibilidades) # elegimos en que dirección movernos
            mover(jugador, direccion_index) # ahora nos movemos según la direccion_index: 0:Up 1:Down 2:Left 3:Rigth

        turno += 1
        if turno == 2: break

def anuncia_ganadores():
    """Anuncia el jugador o jugadores ganadores cuando finaliza el juego. 
    El juego finaliza cuando ya no queda comida en el tablero.
    Proporciona el ranking de los juegadores con su puntuación."""
    pass

if __name__ == "__main__":
    DIM = 5             # dimensión de un tablero cuadrado nxn
    LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUM_JUGADORES = 4   # elegir entre 2 y 26
    NUM_COMIDA = 1      # número de celdas con comida
    matriz = [['·']*DIM for _ in range(DIM)]    # tablero inicial
    generar_jugadores(NUM_JUGADORES)
    generar_comida(NUM_COMIDA)
    imprime_matriz()
    print(matriz)
    print()
    #print("Celdas con comida:", contar_comida())
    primer_jugador = quien_comienza()   # como index
    jugando()
    anuncia_ganadores()
    