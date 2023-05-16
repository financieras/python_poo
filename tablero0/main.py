#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sin usar POO programamos 
un tablero, unos jugadores y una comida """

from random import seed, randint
seed()

def imprime_matriz():
    """Imprime el tablero en forma de matriz"""
    global matriz
    for fila in range(len(matriz[0])):
        print(*matriz[fila])

def generar_jugadores(num_jugadores):
    """Genera aleatoriamente los jugadores automaticamete asignándoles 
    una letra como nombre y una posición aleatoria"""
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(num_jugadores):
        letra = letras[i]
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

if __name__ == "__main__":
    DIM = 5             # dimensión de un tablero cuadrado nxn
    NUM_JUGADORES = 4   # elegir entre 2 y 26
    NUM_COMIDA = 4      # número de celdas con comida
    matriz = [['·']*DIM for _ in range(DIM)]    # tablero inicial
    generar_jugadores(NUM_JUGADORES)
    generar_comida(NUM_COMIDA)
    imprime_matriz()
    print()
    print("Celdas con comida:", contar_comida())
    