import random

class Tablero:
    def __init__(self, dim=10, num_comida=10, num_jugadores=2):
        self.dim = dim
        self.num_comida = num_comida
        self.num_jugadores = num_jugadores
        self.matriz = [['·' for _ in range(dim)] for _ in range(dim)]
        self.jugadores = []
        self.comida = []
        self.letras = [chr(i) for i in range(65, 91)]
        self.generar_jugadores()
        self.generar_comida()

    def generar_jugadores(self):
        for i in range(self.num_jugadores):
            letra = self.letras[i]
            x, y = self.generar_posicion_aleatoria()
            while self.matriz[x][y] != '·':
                x, y = self.generar_posicion_aleatoria()
            jugador = Jugador(letra, x, y)
            self.jugadores.append(jugador)
            self.matriz[x][y] = letra

    def generar_comida(self):
        for i in range(self.num_comida):
            x, y = self.generar_posicion_aleatoria()
            while self.matriz[x][y] != '·':
                x, y = self.generar_posicion_aleatoria()
            valor = random.randint(1, 9)
            self.comida.append((x, y, valor))
            self.matriz[x][y] = str(valor)

    def generar_posicion_aleatoria(self):
        x = random.randint(0, self.dim - 1)
        y = random.randint(0, self.dim - 1)
        return x, y

    def imprimir_tablero(self):
        for fila in self.matriz:
            print(' '.join(fila))


class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra
        self.x = x
        self.y = y
        self.puntos = 0

    def mover(self, direccion, tablero):
        if direccion == 'arriba':
            if self.x > 0:
                if tablero.matriz[self.x - 1][self.y] == '·':
                    tablero.matriz[self.x][self.y] = '·'
                    self.x -= 1
                    tablero.matriz[self.x][self.y] = self.letra
                elif tablero.matriz[self.x - 1][self.y].isdigit():
                    self.comer(tablero)
                    tablero.matriz[self.x][self.y] = '·'
                    self.x -= 1
                    tablero.matriz[self.x][self.y] = self.letra
        elif direccion == 'abajo':
            if self.x < tablero.dim - 1:
                if tablero.matriz[self.x + 1][self.y] == '·':
                    tablero.matriz[self.x][self.y] = '·'
                    self.x += 1
                    tablero.matriz[self.x][self.y] = self.letra
                elif tablero.matriz[self.x + 1][self.y].isdigit():
                    self.comer(tablero)
                    tablero.matriz[self.x][self.y] = '·'
                    self.x += 1
                    tablero.matriz[self.x][self.y] = self.letra
        elif direccion == 'izquierda':
            if self.y > 0:
                if tablero.matriz[self.x][self.y - 1] == '·':
                    tablero.matriz[self.x][self.y] = '·'
                    self.y -= 1
                    tablero.matriz[self.x][self.y] = self.letra
                elif tablero.matriz[self.x][self.y - 1].isdigit():
                    self.comer(tablero)
                    tablero.matriz[self.x][self.y] = '·'
                    self.y -= 1
                    tablero.matriz[self.x][self.y] = self.letra
        elif direccion == 'derecha':
            if self.y < tablero.dim - 1:
                if tablero.matriz[self.x][self.y + 1] == '·':
                    tablero.matriz[self.x][self.y] = '·'
                    self.y += 1
                    tablero.matriz[self.x][self.y] = self.letra
                elif tablero.matriz[self.x][self.y + 1].isdigit():
                    self.comer(tablero)
                    tablero.matriz[self.x][self.y] = '·'
                    self.y += 1
                    tablero.matriz[self.x][self.y] = self.letra

    def comer(self, tablero):
        if tablero.matriz[self.x][self.y].isdigit():
            valor = int(tablero.matriz[self.x][self.y])
            self.puntos += valor
            tablero.matriz[self.x][self.y] = '·'
            tablero.comida.remove((self.x, self.y, valor))


def jugar(tablero):
    while tablero.comida:
        todos_atrapados = True
        for jugador in tablero.jugadores:
            direccion = random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
            jugador.mover(direccion, tablero)
            jugador.comer(tablero)
            if not tablero.comida:
                break
            if jugador.x > 0 and tablero.matriz[jugador.x - 1][jugador.y] == '·':
                todos_atrapados = False
            elif jugador.x < tablero.dim - 1 and tablero.matriz[jugador.x + 1][jugador.y] == '·':
                todos_atrapados = False
            elif jugador.y > 0 and tablero.matriz[jugador.x][jugador.y - 1] == '·':
                todos_atrapados = False
            elif jugador.y < tablero.dim - 1 and tablero.matriz[jugador.x][jugador.y + 1] == '·':
                todos_atrapados = False
        tablero.imprimir_tablero()
        print()
        if todos_atrapados:
            break
    max_puntos = max(jugador.puntos for jugador in tablero.jugadores)
    ganadores = [jugador for jugador in tablero.jugadores if jugador.puntos == max_puntos]
    if len(ganadores) == 1:
        print(f"El ganador es el jugador {ganadores[0].letra} con {ganadores[0].puntos} puntos.")
    else:
        letras_ganadoras = ', '.join([jugador.letra for jugador in ganadores])
        print(f"Hay un empate entre los jugadores {letras_ganadoras} con {max_puntos} puntos.")




if __name__ == '__main__':
    tablero = Tablero(3,2,2)
    tablero.imprimir_tablero()
    jugar(tablero)
