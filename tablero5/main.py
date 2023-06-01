import random
import os
import time
from string import ascii_uppercase


class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra
        self.x = x
        self.y = y
        self.puntaje = 0


class Comida:
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor


class Tablero:
    def __init__(self, DIM, num_jugadores, num_comida):
        self.DIM = DIM
        self.tablero = [['·' for _ in range(DIM)] for _ in range(DIM)]
        self.jugadores = []
        self.comidas = []
        for i in range(num_jugadores):
            jugador_x = random.randint(0, DIM-1)
            jugador_y = random.randint(0, DIM-1)
            while self.tablero[jugador_x][jugador_y] != '·':
                jugador_x = random.randint(0, DIM-1)
                jugador_y = random.randint(0, DIM-1)
            self.tablero[jugador_x][jugador_y] = ascii_uppercase[i]
            self.jugadores.append(
                Jugador(ascii_uppercase[i], jugador_x, jugador_y))
        for i in range(num_comida):   # comida
            comida_x = random.randint(0, DIM-1)
            comida_y = random.randint(0, DIM-1)
            while self.tablero[comida_x][comida_y] != '·':
                comida_x = random.randint(0, DIM-1)
                comida_y = random.randint(0, DIM-1)
            valor_comida = random.randint(1, 9)
            self.tablero[comida_x][comida_y] = str(valor_comida)
            self.comidas.append(Comida(comida_x, comida_y, valor_comida))

    def __str__(self):
        res = ''
        for fila in self.tablero:
            res += ' '.join(fila) + '\n'
        return res

    def mover_jugador(self, jugador):
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(movimientos)
        nueva_x = jugador.x + dx
        nueva_y = jugador.y + dy
        while not (0 <= nueva_x < self.DIM and 0 <= nueva_y < self.DIM) or self.tablero[nueva_x][nueva_y].isalpha():
            dx, dy = random.choice(movimientos)
            nueva_x = jugador.x + dx
            nueva_y = jugador.y + dy
        if self.tablero[nueva_x][nueva_y].isdigit():
            valor_comida = int(self.tablero[nueva_x][nueva_y])
            jugador.puntaje += valor_comida
            self.comidas = [comida for comida in self.comidas if not (
                comida.x == nueva_x and comida.y == nueva_y)]

        self.tablero[jugador.x][jugador.y] = '·'
        jugador.x = nueva_x
        jugador.y = nueva_y
        self.tablero[jugador.x][jugador.y] = jugador.letra


class Juego:
    def __init__(self, DIM, num_jugadores, num_comida):
        self.tablero = Tablero(DIM, num_jugadores, num_comida)

    def jugar(self):
        print(self.tablero)
        while self.tablero.comidas:
            for jugador in self.tablero.jugadores:
                self.tablero.mover_jugador(jugador)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.tablero)
                time.sleep(0.1)
        ganador = max(self.tablero.jugadores, key=lambda j: j.puntaje)
        print(
            f"¡El ganador es el jugador {ganador.letra} con {ganador.puntaje} puntos!")


if "__main__" == __name__:
    DIM = 6
    num_jugadores = 9
    num_comida = 20
    # Juego(DIM, num_jugadores)
    partida = Juego(DIM, num_jugadores, num_comida)
    partida.jugar()