import random, os, time
from string import ascii_uppercase

class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra
        self.x = x
        self.y = y

class Tablero:
    def __init__(self, DIM, num_jugadores):
        self.DIM = DIM
        self.tablero = [['·' for _ in range(DIM)] for _ in range(DIM)]
        self.jugadores = []
        for i in range(num_jugadores):
            jugador_x = random.randint(0, DIM-1)
            jugador_y = random.randint(0, DIM-1)
            while self.tablero[jugador_x][jugador_y] != '·':
                jugador_x = random.randint(0, DIM-1)
                jugador_y = random.randint(0, DIM-1)
            self.tablero[jugador_x][jugador_y] = ascii_uppercase[i]
            self.jugadores.append(Jugador(ascii_uppercase[i], jugador_x, jugador_y))

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
        while not (0 <= nueva_x < self.DIM and 0 <= nueva_y < self.DIM) or self.tablero[nueva_x][nueva_y] != '·':
            dx, dy = random.choice(movimientos)
            nueva_x = jugador.x + dx
            nueva_y = jugador.y + dy
        self.tablero[jugador.x][jugador.y] = '·'
        jugador.x = nueva_x
        jugador.y = nueva_y
        self.tablero[jugador.x][jugador.y] = jugador.letra

class Juego:
    def __init__(self, DIM, num_jugadores):
        self.tablero = Tablero(DIM, num_jugadores)

    def jugar(self):
        print(self.tablero)
        for _ in range(6):
            for jugador in self.tablero.jugadores:
                self.tablero.mover_jugador(jugador)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.tablero)
                time.sleep(0.3)

juego = Juego(5, 3)
juego.jugar()