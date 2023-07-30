import random
import os
import time

# Constants
RED = "\033[1;91m"        # Red Bold High Intensty
GREEN = "\033[1;92m"      # Green Bold High Intensty
YELLOW = "\033[1;93m"     # Yellow Bold High Intensty
BLUE = "\033[1;94m"       # Blue Bold High Intensty
PURPLE = "\033[1;95m"     # Purple Bold High Intensty
CYAN = "\033[1;96m"       # Cyan Bold High Intensty
RESET = "\033[0m"


class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra
        self.x = x
        self.y = y
        self.puntaje = 0

    def __str__(self):
        return f'{self.letra} → {self.puntaje}'
    
    def mover_hacia_comida(self, tablero):
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]    # tuplas: arriba, abajo, derecha, izquierda
        mejores_movimientos = []
        max_valor_comida = 0

        for movimiento in movimientos:
            dx, dy = movimiento
            nueva_x = self.x + dx
            nueva_y = self.y + dy

            if 0 <= nueva_x < tablero.DIM and 0 <= nueva_y < tablero.DIM:
                if tablero.tablero[nueva_x][nueva_y].isdigit():
                    valor_comida = int(tablero.tablero[nueva_x][nueva_y])
                    if valor_comida > max_valor_comida:
                        max_valor_comida = valor_comida
                        mejores_movimientos = [(dx, dy)]
                    elif valor_comida == max_valor_comida:
                        mejores_movimientos.append((dx, dy))

        if mejores_movimientos:
            dx, dy = random.choice(mejores_movimientos)
            nueva_x = self.x + dx
            nueva_y = self.y + dy

            tablero.tablero[self.x][self.y] = '·'
            self.x = nueva_x
            self.y = nueva_y
            tablero.tablero[self.x][self.y] = self.letra



class Comida:
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor


class Tablero:
    def __init__(self, DIM, num_jugadores, num_comida):
        self.DIM = DIM
        self.tablero = [['·']*DIM for _ in range(DIM)]
        self.jugadores = []     # array de objetos de la clase Jugador
        self.comidas = []       # array de objetos de la clase Comida
        for i in range(num_jugadores):
            jugador_x = random.randint(0, DIM-1)
            jugador_y = random.randint(0, DIM-1)
            while self.tablero[jugador_x][jugador_y] != '·':
                jugador_x = random.randint(0, DIM-1)
                jugador_y = random.randint(0, DIM-1)
            self.tablero[jugador_x][jugador_y] = chr(65 + i)
            self.jugadores.append(Jugador(chr(65 + i), jugador_x, jugador_y))
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
        tablero_color = [row[:] for row in self.tablero]    # Deep Copy de la matriz
        #print(self.tablero)
        num_letras = len([element for row in self.tablero for element in row if element.isupper()])
        res = ''
        for fila in tablero_color:
            for cont, caracter in enumerate(fila):
                if caracter in [chr(i) for i in range(66, 91)]:
                    fila[cont] = f'{GREEN}{caracter}{RESET}'   # cambia el caracter letra mayúscula por ella misma con color
                elif caracter == 'A':
                    fila[cont] = f'{RED}{caracter}{RESET}'
            res += ' '.join(fila) + '\n'
            #res += num_letras
        return res

    def mover_jugador(self, jugador):
        if jugador.letra == 'A':
            jugador.mover_hacia_comida(self)
        else:   # Resto del código para mover los otros jugadores de forma aleatoria
            movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]    # tuplas: arriba, abajo, derecha, izquierda
            libertades = [True] * 4   # Inicialmente suponemos que el jugador tiene todas las libertades de movimiento
            for count, movimiento in enumerate(movimientos):
                dx, dy = movimiento
                nueva_x = jugador.x + dx
                nueva_y = jugador.y + dy
                if not (0 <= nueva_x < self.DIM and 0 <= nueva_y < self.DIM) or self.tablero[nueva_x][nueva_y].isalpha():
                    libertades[count] = False   # jugador ahogado en esa dirección, no puede moverse al tener pared u otro jugador
            if any(libertades):  # da False cuando el jugador está ahogado en todas las direcciones, y entonces pasa turno
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
                    self.comidas = [comida for comida in self.comidas if not (comida.x == nueva_x and comida.y == nueva_y)]

                self.tablero[jugador.x][jugador.y] = '·'
                jugador.x = nueva_x
                jugador.y = nueva_y
                self.tablero[jugador.x][jugador.y] = jugador.letra


class Juego:
    def __init__(self, DIM, num_jugadores, num_comida):
        self.tablero = Tablero(DIM, num_jugadores, num_comida)

    def imprimir_ranking(self):
        jugadores_ordenados = sorted(self.tablero.jugadores, key=lambda jugador: jugador.puntaje, reverse=True)
        print("Ranking de jugadores:")
        for jugador in jugadores_ordenados:
            print(jugador)  # usa el str del jugador

    def jugar(self):
        print(self.tablero)
        while self.tablero.comidas:
            for jugador in self.tablero.jugadores:
                if not self.tablero.comidas:
                    break   # si ya no hay comida en el tablero finaliza el juego sin terminar el turno de los otros jugadores
                self.tablero.mover_jugador(jugador)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.tablero)
                print()
                time.sleep(0.1)
        ganador = max(self.tablero.jugadores, key=lambda j: j.puntaje)
        print(f"¡El ganador es el jugador {ganador.letra} con {ganador.puntaje} puntos!\n")
        self.imprimir_ranking()


if "__main__" == __name__:
    DIM = 10
    NUM_PLAYERS = 26
    AMOUNT_FOOD = 74
    partida = Juego(DIM, NUM_PLAYERS, AMOUNT_FOOD)
    partida.jugar()