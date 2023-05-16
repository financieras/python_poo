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
    una letra como nombre y una posición aleatoria"""
    for i in range(num_jugadores):
        letra = LETRAS[i]
        x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        while matriz[x][y] != '·':
            x, y = randint(0, len(matriz)-1), randint(0, len(matriz)-1)
        matriz[x][y] = letra

def generar_comida(num_comida):
    """Generamos aleatoriamente posiciones de comida en el tablero
    con un valor aleatorio"""
    for _ in range(num_comida):
        x, y = randint(0, len(matriz)-1), randint(0, len(matriz)-1)
        while matriz[x][y] != '·':
            x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        matriz[x][y] = str(randint(1, 9))    # el valor de la comida es aleatorio, como str

def contar_comida():
    """Cuenta el número de celdas con comida que existen en la matriz"""
    contador = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if (matriz[fila][columna]).isnumeric():
                contador += 1
    return contador

def quien_comienza():
    """Devuelve la primera letra de la matriz"""
    primer_jugador = randint(0, NUM_JUGADORES-1)
    primera_letra = LETRAS[primer_jugador]
    print("Comienza jugando", primera_letra)
    return primer_jugador   # como index

def localiza(jugador):
    """Devuelve la posición de la letra en la matriz"""
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == LETRAS[jugador]:
                return fila, columna
            
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

def mover(jugador, arr_posibilidades):
    """Mueve el jugador considerando las posiciones a las que está permitido
     moverse dadas por el vector arr_posibilidades"""
    x, y = localiza(jugador)
    # LANZAMOS UNA FUNCIÓN QUE ASIGNA EL MÉTODO ELEGIDO PARA MOVERNOS:
    #  PARA EL JUGADOR A, SERÁ EL SIGUIENTE, Y PARA OTROS JUGADORES DEJAR LA POSIBILIDAD DE QUE LUEGO
    #  SE HAGAN OTROS MÉTODOS (CADA UNO EL SUYO) PARA IR OPTIMIZANDO ESTRATEGIAS DE MOVIMIENTO.

    # MÉTODO A: LLAMAR A UNA FUNCIÓN QUE ELIGE SI MOVERSE HACIA UN LADO O HACIA OTRO DENTRO DE LOS True QUE DA EL VECTOR arr_posibilidades
    # SI HAY VARIOS True QUE CONDUCEN A UN VALOR NUMÉRICO (CON COMIDA) SE IRÁ AL MAYOR
    # SI SOLO HAY UN VALOR NUMÉRICO SE IRÁ A ESE
    # SI NO HAY NINGÚN VALOR NUMÉRICO SE ELIGE ALEATORIAMENTE ALGUNO DE LOS True

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
            mover(jugador, arr_posibilidades)

        turno += 1
        if turno == 5: break

def anuncia_ganadores():
    """Anuncia el jugador o jugadores ganadores cuando finaliza el juego. 
    El juego finaliza cuando ya no queda comida en el tablero.
    Proporciona todos los puntajes, la clasificación por orden."""
    pass

if __name__ == "__main__":
    DIM = 3             # dimensión de un tablero cuadrado nxn
    LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUM_JUGADORES = 4   # elegir entre 2 y 26
    NUM_COMIDA = 4      # número de celdas con comida
    matriz = [['·']*DIM for _ in range(DIM)]    # tablero inicial
    generar_jugadores(NUM_JUGADORES)
    generar_comida(NUM_COMIDA)
    imprime_matriz()
    print()
    #print("Celdas con comida:", contar_comida())
    primer_jugador = quien_comienza()   # como index
    jugando()
    anuncia_ganadores()
    