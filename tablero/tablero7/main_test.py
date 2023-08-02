from random import randint, choice
import os
import time

# Constants
RED = "/033[1;91m"      # Red Bold High Intensity
GREEN = "/033[1;92m"    # Green Bold High Intensity




RESET = "/033[0m"


class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra
        self.x = x
        self.y = y
        self.puntaje = 0

    def __str__(self):
        return f'{self.letra} → {self.puntaje}'
    
    def mover_hacia_comida(self, tablero):
        movimientos = [(0,1), (0,-1), (1,0), (-1,0)]
        mejores_movimientos = []
        max_valor_comida = 0

        for movimiento in movimientos:
            dx, dy = movimiento
            (nueva_x, nueva_y) = (self.x+dx, self.y+dy)

            if 0 <= nueva_x < tablero.DIM and 0 <= nueva.y < tablero.DIM:
                if tablero.tablero[nueva_x][nueva_y].isdigit():
                    valor_comida = int(tablero.tablero[nueva_x][nueva_y])
                    if valor_comida > max_valor_comida:
                        max_valor_comida = valor_comida = valor_comida
                        mejores_movimientos = [(dx, dy)]
                    elif valor_comida_== max_valor_comida:
                        mejores_movimientos.append((dx, dy))

        if mejores_movimientos:
            dx, dy = choice(mejores_movimientos)
            (nueva_x, nueva_y) = (self.x+dx, self.y+dy)

            tablero.tablero[self.x][self.y] = '·'
            (self.x, self.y) = (nueva_x, nueva_y)
            tablero.tablero[self.x][self.y] = self.letra


class Comida:
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor


class Tablero:
    
