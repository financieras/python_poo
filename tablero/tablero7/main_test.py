from random import randint, choice
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

    def mover_aleatorio(self):
        dx, dy = choice(MOVIMIENTOS)    # elección aleatoria del movimiento
        return dx, dy

    def mover_hacia_comida_inmediata(self, tablero):
        mejores_movimientos = []
        max_valor_comida = 0

        for movimiento in MOVIMIENTOS:
            dx, dy = movimiento
            (nueva_x, nueva_y) = (self.x+dx, self.y+dy)

            if 0 <= nueva_x < DIM and 0 <= nueva_y < DIM:
                if tablero.tablero[nueva_x][nueva_y].isdigit():
                    valor_comida = int(tablero.tablero[nueva_x][nueva_y])
                    if valor_comida > max_valor_comida:
                        max_valor_comida = valor_comida
                        mejores_movimientos = [(dx, dy)] # si hay nuevo máximo sustituye al anterior
                    elif valor_comida == max_valor_comida:
                        mejores_movimientos.append((dx, dy)) # si hay empate en el máximo

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
    def __init__(self, NUM_PLAYERS, AMOUNT_FOOD):
        self.tablero = [['·']*DIM for _ in range(DIM)]
        self.jugadores = []     # array de objetos de la clase Jugador
        self.comidas = []       # array de objetos de la clase Comida
        for i in range(NUM_PLAYERS):    # ubicar jugadores
            while True:
                (jugador_x, jugador_y) = (randint(0, DIM-1), randint(0, DIM-1))
                if self.tablero[jugador_x][jugador_y] == '·':
                    break   # ya hemos encontrado sitio libre para el jugador
            self.tablero[jugador_x][jugador_y] = chr(65 + i)    # letras
            self.jugadores.append(Jugador(chr(65 + i), jugador_x, jugador_y))   # instanciación de un objeto de la clase Jugador
        for i in range(AMOUNT_FOOD):   # ubicar comida
            while True:
                comida_x, comida_y = randint(0, DIM-1), randint(0, DIM-1)
                if self.tablero[comida_x][comida_y] == '·':
                    break   # ya hemos encontrado un sitio libre para la comida
            valor_comida = randint(1, 9)
            self.tablero[comida_x][comida_y] = str(valor_comida)    # los números del tablero van como strings
            self.comidas.append(Comida(comida_x, comida_y, valor_comida))   # instanciación de un objeto de la clase Comida

    def __str__(self):
        tablero_color = [row[:] for row in self.tablero]    # Deep Copy
        res = ''
        for fila in tablero_color:
            for cont, caracter in enumerate(fila):
                if caracter in [chr(i) for i in range(66, 91)]: # todas las letras mayúsculas menos A
                    fila[cont] = f'{GREEN}{caracter}{RESET}'    # cambia el caracter letra mayúscula por ella misma con color
                elif caracter == 'A':                           # color específico para esta letra
                    fila[cont] = f'{RED}{caracter}{RESET}'
            res += ' '.join(fila) + '\n'
        return res

    def mover_jugador(self, jugador):
        libertades = [True] * 4   # Inicialmente suponemos que el jugador tiene todas las libertades de movimiento
        for count, movimiento in enumerate(MOVIMIENTOS):
            dx, dy = movimiento
            (nueva_x, nueva_y) = (jugador.x + dx, jugador.y + dy)
            if not (0 <= nueva_x < DIM and 0 <= nueva_y < DIM) or self.tablero[nueva_x][nueva_y].isalpha():
                libertades[count] = False   # jugador ahogado en esa dirección, no puede moverse al tener pared u otro jugador
        if any(libertades):  # da False cuando el jugador está ahogado en todas las direcciones, y entonces pasa turno
            while True:
                if jugador.letra == 'C':
                    dx, dy = jugador.mover_hacia_comida_inmediata(self.tablero)
                else:
                    dx, dy = jugador.mover_aleatorio()
                (nueva_x, nueva_y) = (jugador.x + dx, jugador.y + dy)
                if (0 <= nueva_x < DIM and 0 <= nueva_y < DIM) and not(self.tablero[nueva_x][nueva_y].isalpha()):
                    break   # ya hemos encontrado un sitio válido al que movernos
            if self.tablero[nueva_x][nueva_y].isdigit():
                valor_comida = int(self.tablero[nueva_x][nueva_y])
                jugador.puntaje += valor_comida
                self.comidas = [comida for comida in self.comidas if not (comida.x == nueva_x and comida.y == nueva_y)]

            self.tablero[jugador.x][jugador.y] = '·'    # reponemos el punto en la celda abandonada
            (jugador.x, jugador.y) = (nueva_x, nueva_y) # asignamos la nueva posición al jugador
            self.tablero[jugador.x][jugador.y] = jugador.letra  # ponemos la letra en la nueva posición


class Juego:
    def __init__(self, NUM_PLAYERS, AMOUNT_FOOD):
        self.tablero = Tablero(NUM_PLAYERS, AMOUNT_FOOD)   # instanciamos un objeto de la clase Tablero

    def imprimir_ranking(self):
        jugadores_ordenados = sorted(self.tablero.jugadores, key=lambda jugador: jugador.puntaje, reverse=True)
        print("Ranking de jugadores:")
        for jugador in jugadores_ordenados:
            print(jugador)  # usa el str del jugador

    def jugar(self):
        print(self.tablero)
        while self.tablero.comidas:
            for jugador in self.tablero.jugadores:
                if not self.tablero.comidas:    # si ya no hay comida en el tablero
                    break   # finaliza el juego sin terminar el turno de los otros jugadores
                else:       # mientras haya comida en el tablero
                    self.tablero.mover_jugador(jugador)     # invocamos el método mover_jugador
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.tablero)
                    print()
                    time.sleep(0.03)
        ganador = max(self.tablero.jugadores, key=lambda j: j.puntaje)
        print(f"¡El ganador es el jugador {ganador.letra} con {ganador.puntaje} puntos!\n")
        self.imprimir_ranking()


if "__main__" == __name__:
    DIM = 10
    NUM_PLAYERS = 2
    AMOUNT_FOOD = DIM**2-NUM_PLAYERS
    MOVIMIENTOS = [(0, 1), (0, -1), (1, 0), (-1, 0)]    # tuplas: Derecha, Izquierda, Arriba, aBajo
    partida = Juego(NUM_PLAYERS, AMOUNT_FOOD)
    partida.jugar()