from random import randint
import os
import time


# Constants
RED = "\033[1;91m"        # Red Bold High Intensty
GREEN = "\033[1;92m"      # Green Bold High Intensty
YELLOW = "\033[0;33m"     # Yellow                      #"\033[1;93m"     # Yellow Bold High Intensty
BLUE = "\033[1;94m"       # Blue Bold High Intensty
PURPLE = "\033[1;95m"     # Purple Bold High Intensty
CYAN = "\033[1;96m"       # Cyan Bold High Intensty
RESET = "\033[0m"


class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra  # La letra mayúscula del alfabeto es el nombre del jugador
        self.x = x          # Posición x del jugador en el tablero. x representa el número de fila
        self.y = y          # Posición y del jugador en el tablero. y representa el número de columna
        self.puntaje = 0    # Acumulado de puntos, se inicializa en cero

    def __str__(self):
        return f'{self.letra} → {self.puntaje}.     \tx: {self.x} \ty: {self.y}'
    
    def posicion_factible(self, posicion_propuesta):  # si la posición propuesta es factible da True
        nueva_x, nueva_y = posicion_propuesta
        if (0 <= nueva_x < HEIGHT and 0 <= nueva_y < WIDTH) and not(self.matrix[nueva_x][nueva_y].isalpha()):
            return True
        return False

    def mover_aleatorio(self, libertades):
        while True:
            dado = randint(0,3) # dado de 4 caras para determinar aleatoriamente uno de los 4 movimientos
            if libertades[dado]:    # solo es True si se elige un movimiento válido
                return MOVIMIENTOS[dado]    # retorna la tupla con el movimiento elegido
    
    def mover_hacia_comida_inmediata(self, jugador, libertades, board):
        maximo_comidas_cercanas = 0
        dx_max = dy_max = 0
        for count, libertad in enumerate(libertades):
            if libertad:    # si es libre en esa dirección
                dx, dy = MOVIMIENTOS[count]
                (nueva_x, nueva_y) = (jugador.x + dx, jugador.y + dy)
                contenido_celda = board[nueva_x][nueva_y]
                if contenido_celda.isdigit() and int(contenido_celda) > maximo_comidas_cercanas:   # si encuentra comida y su valor numérico es > que el maximo
                    maximo_comidas_cercanas = int(contenido_celda)
                    (dx_max, dy_max) = (dx, dy)     # marca la dirección en la que obtendríamos la máxima comida al finalizar el bucle for
        if dx_max == 0 and dy_max == 0:             # en este caso no hay comida inmediata y se mueve aleatoriamente
            return jugador.mover_aleatorio(libertades)
        else:   # en este caso si hay comida inmediata y se retorna la dirección de máximo valor de la comida
            return dx_max, dy_max   # se debe retornar la tupla (dx, dy) que marca la dirección de máxima comida cercana en alguna celda contígua
    
    def distancia(self, posicion_inicial, posicion_final):    # las posiciones son tuplas con la componentes (x,y)
        return abs(posicion_final[0]-posicion_inicial[0]) + abs(posicion_final[1]-posicion_inicial[1])  # retorna un int

    def mover_hacia_comida(self, jugador, libertades, matrix):  # determinamos el movimiento dx,dy necesario para ir hacia la comida más cercana aunque no sea inmediata
        # CALCULAMOS LA POSICIÓN DE LA COMIDA MÁS CERCANA
        min_distancia = None            # inicializamos la variable
        posicion_comida_cercana = None  # tupla con la posición a la comida más cercana
        for i in range(HEIGHT):         # HEIGHT representa la altura (filas)
            for j in range(WIDTH):      # WIDTH representa el ancho (columnas)
                distance = self.distancia((jugador.x, jugador.y), (i, j))
                if (min_distancia == None or distance < min_distancia) and matrix[i][j].isdigit():
                    posicion_comida_cercana = (i, j)    # al finalizar los dos bucles tendremos en esta variable la posición a la comida más cercana
                    min_distancia = distance            # y tendremos la distancia que separa al jugador de la comida más cercana
        # PROBAMOS LOS 4 POSIBLES MOVIMIENTOS para ver en cuál obtendríamos la min_distancia-1 y que no se monte encima de otro jugador
        for movimiento in MOVIMIENTOS:
            dx, dy = movimiento
            new_x, new_y = jugador.x + dx, jugador.y + dy
            if self.distancia((new_x, new_y), posicion_comida_cercana) == min_distancia-1 and not(matrix[new_x][new_y].isalpha()):
                return dx, dy
        return jugador.mover_aleatorio(libertades)
        

class Comida:
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor


class Board:
    def __init__(self, NUM_PLAYERS, AMOUNT_FOOD):
        self.matrix = [['·']*WIDTH for _ in range(HEIGHT)]  # inicializamos la matriz rectangular que representa el tablero
        self.jugadores = []     # array de objetos de la clase Jugador
        self.comidas = []       # array de objetos de la clase Comida
        for i in range(NUM_PLAYERS):    # ubicar jugadores
            while True:
                (jugador_x, jugador_y) = (randint(0, HEIGHT-1), randint(0, WIDTH-1))
                if self.matrix[jugador_x][jugador_y] == '·':
                    break   # ya hemos encontrado sitio libre para el jugador
            self.matrix[jugador_x][jugador_y] = chr(65 + i)    # letras
            jugador = Jugador(chr(65 + i), jugador_x, jugador_y)    # instanciación de un objeto de la clase Jugador
            self.jugadores.append(jugador)                          # añadimos el objeto al array de objetos
        for i in range(AMOUNT_FOOD):    # ubicar comida
            while True:
                comida_x, comida_y = randint(0, HEIGHT-1), randint(0, WIDTH-1)
                if self.matrix[comida_x][comida_y] == '·':
                    break   # ya hemos encontrado un sitio libre para la comida
            valor_comida = randint(1, 9)
            self.matrix[comida_x][comida_y] = str(valor_comida)     # los números del board van como strings
            comida = Comida(comida_x, comida_y, valor_comida)       # instanciación de un objeto de la clase Comida
            self.comidas.append(comida)                             # añadimos el objeto al array de objetos

    def __str__(self):
        board_color = [row[:] for row in self.matrix]    # Deep Copy
        res = ''
        for fila in board_color:
            for cont, caracter in enumerate(fila):
                if caracter == 'A':                                 # color específico para esta letra
                    fila[cont] = f'{RED}{caracter}{RESET}'
                elif caracter == 'B':                               # color específico para esta letra
                    fila[cont] = f'{GREEN}{caracter}{RESET}'
                elif caracter in [chr(i) for i in range(67, 91)]:   # todas las letras mayúsculas menos A y B
                    fila[cont] = f'{YELLOW}{caracter}{RESET}'       # cambia el caracter letra mayúscula por ella misma con color
            res += ' '.join(fila) + '\n'
        return res

    def mover_jugador(self, jugador):
        libertades = [True] * 4   # Inicialmente suponemos que el jugador tiene todas las libertades de movimiento
        for count, movimiento in enumerate(MOVIMIENTOS):
            dx, dy = movimiento
            (nueva_x, nueva_y) = (jugador.x + dx, jugador.y + dy)
            if not(Jugador.posicion_factible(self, (nueva_x, nueva_y))):
                libertades[count] = False   # jugador ahogado en esa dirección, no puede moverse al tener pared u otro jugador
        if any(libertades):  # da False cuando el jugador está ahogado en todas las direcciones, y entonces pasa turno
            if jugador.letra == 'A' or jugador.letra == 'B':                                        # <----- Caso del jugador A y B
                dx, dy = jugador.mover_hacia_comida(jugador, libertades, self.matrix)
            elif jugador.letra == 'C' or jugador.letra == 'D':                                      # <----- Caso del jugador C y D 
                dx, dy = jugador.mover_hacia_comida_inmediata(jugador, libertades, self.matrix)
            else:                                                                                   # para el resto de jugadores se mueve de forma aleatoria
                dx, dy = jugador.mover_aleatorio(libertades)
            (nueva_x, nueva_y) = (jugador.x + dx, jugador.y + dy)

            if self.matrix[nueva_x][nueva_y].isdigit():            # si encuentra comida
                valor_comida = int(self.matrix[nueva_x][nueva_y])
                jugador.puntaje += valor_comida
                self.comidas = [comida for comida in self.comidas if not (comida.x == nueva_x and comida.y == nueva_y)]

            self.matrix[jugador.x][jugador.y] = '·'             # reponemos el punto en la celda abandonada
            (jugador.x, jugador.y) = (nueva_x, nueva_y)         # asignamos la nueva posición al jugador
            self.matrix[jugador.x][jugador.y] = jugador.letra   # ponemos la letra en la nueva posición


class Juego:
    def __init__(self, NUM_PLAYERS, AMOUNT_FOOD):
        self.board = Board(NUM_PLAYERS, AMOUNT_FOOD)   # instanciamos un objeto de la clase Board

    def imprimir_ranking(self):
        jugadores_ordenados = sorted(self.board.jugadores, key=lambda jugador: jugador.puntaje, reverse=True)
        print("Ranking de jugadores:")
        for jugador in jugadores_ordenados:
            print(jugador)  # usa el str del jugador

    def jugar(self):
        print(self.board)
        print()
        while self.board.comidas:           # mientras haya comida en el array de comidas
            for jugador in self.board.jugadores:
                if not self.board.comidas:  # si ya no hay comida en el board
                    break                   # finaliza el juego sin terminar el turno de los otros jugadores
                else:                                   # mientras haya comida en el board
                    self.board.mover_jugador(jugador)   # invocamos el método mover_jugador
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.board)
                    print()
                    time.sleep(0.01)
        ganador = max(self.board.jugadores, key=lambda j: j.puntaje)
        print(f"¡El ganador es el jugador {ganador.letra} con {ganador.puntaje} puntos!\n")
        self.imprimir_ranking()


if "__main__" == __name__:
    HEIGHT = 18 # Altura: número de filas que hay en el tablero
    WIDTH = 32  # Anchura: número de columnas. La dimensión debe ser suficiente para todos los jugadores y al menos una comia
    NUM_PLAYERS = 6 # tienen que estar entre min=2 y max=26
    AMOUNT_FOOD = HEIGHT * WIDTH - NUM_PLAYERS  # Llenando todo el tablero de comida
    MOVIMIENTOS = [(0, 1), (0, -1), (1, 0), (-1, 0)]    # tuplas: Derecha, Izquierda, aBajo, Arriba, o bien EWSN (Este, West, Sur, Norte)
    partida = Juego(NUM_PLAYERS, AMOUNT_FOOD)
    partida.jugar()
    # Si HEIGHT = 45 y WIDTH = 80 esquina inferior derecha tiene las coordenadas (x, y) = (44, 79)
    # x oscilaría entre 0 y 44, e y oscliaría entre 0 y 79.