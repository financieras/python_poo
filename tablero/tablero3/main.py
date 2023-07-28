import random

class Tablero:
    def __init__(self, dimension, num_jugadores, num_comida):
        self.dimension = dimension
        self.num_jugadores = num_jugadores
        self.num_comida = num_comida
        self.matrix = [['·' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.jugadores = {}
        self.comida = {}
        
    def colocar_jugadores(self):
        letras = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
        for i in range(self.num_jugadores):
            letra = letras[i]
            x, y = random.randint(0, self.dimension-1), random.randint(0, self.dimension-1)
            while self.matrix[x][y] != '·':
                x, y = random.randint(0, self.dimension-1), random.randint(0, self.dimension-1)
            self.matrix[x][y] = letra
            self.jugadores[letra] = [x, y, 0]
            
    def colocar_comida(self):
        for i in range(self.num_comida):
            x, y = random.randint(0, self.dimension-1), random.randint(0, self.dimension-1)
            while self.matrix[x][y] != '·' or (x, y) in self.comida:
                x, y = random.randint(0, self.dimension-1), random.randint(0, self.dimension-1)
            valor = random.randint(1, 9)
            self.matrix[x][y] = str(valor)
            self.comida[(x, y)] = valor
            
    def mostrar_tablero(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.matrix[i][j], end=' ')
            print()
            
    def actualizar_tablero(self):
        for letra in self.jugadores:
            x, y, puntuacion = self.jugadores[letra]
            if (x, y) in self.comida:
                puntuacion += self.comida[(x, y)]
                del self.comida[(x, y)]
                self.matrix[x][y] = '·'
            self.jugadores[letra] = [x, y, puntuacion]
            self.matrix[x][y] = letra
            print(f"El jugador {letra} tiene {puntuacion} puntos.")


class Jugador:
    def __init__(self, letra, x, y):
        self.letra = letra
        self.x = x
        self.y = y
        self.puntuacion = 0
        
    def mover(self, direccion):
        if direccion == 'arriba':
            self.x -= 1
        elif direccion == 'abajo':
            self.x += 1
        elif direccion == 'izquierda':
            self.y -= 1
        elif direccion == 'derecha':
            self.y += 1
            
    def recolectar_comida(self, valor):
        self.puntuacion += valor


class Juego:
    def __init__(self, dimension, num_jugadores, num_comida):
        self.tablero = Tablero(dimension, num_jugadores, num_comida)
        self.jugadores = []
        self.turno = 0
        
        for letra in self.tablero.jugadores:
            x, y, _ = self.tablero.jugadores[letra]
            jugador = Jugador(letra, x, y)
            self.jugadores.append(jugador)
            
    def iniciar_juego(self):
        self.tablero.colocar_jugadores()
        self.tablero.colocar_comida()
        self.tablero.mostrar_tablero()
        
        while len(self.tablero.comida) > 0:
            print("turno:", self.turno)
            print("jugadores:", self.jugadores)
            jugador = self.jugadores[self.turno % len(self.jugadores)]
            print(f"Turno del jugador {jugador.letra}")
            direccion = self.obtener_direccion(jugador)
            jugador.mover(direccion)
            x, y = jugador.x, jugador.y
            if x < 0 or x >= self.tablero.dimension or y < 0 or y >= self.tablero.dimension:
                print("Movimiento inválido, el jugador se sale del tablero.")
                jugador.mover(self.obtener_direccion_aleatoria())
            elif self.tablero.matrix[x][y] != '·':
                print("Movimiento inválido, la celda está ocupada.")
                jugador.mover(self.obtener_direccion_aleatoria())
            else:
                self.tablero.actualizar_tablero()
                self.turno += 1
                
        self.mostrar_resultados()
        
    def obtener_direccion(self, jugador):
        # Implementar algoritmo para determinar la dirección del movimiento del jugador
        pass
    
    def obtener_direccion_aleatoria(self):
        direcciones = ['arriba', 'abajo', 'izquierda', 'derecha']
        return random.choice(direcciones)
    
    def mostrar_resultados(self):
        puntuaciones = [(j.puntuacion, j.letra) for j in self.jugadores]
        puntuaciones.sort(reverse=True)
        print("Resultados finales:")
        for puntuacion, letra in puntuaciones:
            print(f"El jugador {letra} ha obtenido {puntuacion} puntos.")


if __name__ == '__main__':
    dimension = 10
    num_jugadores = 2
    num_comida = 20
    
    juego = Juego(dimension, num_jugadores, num_comida)
    juego.iniciar_juego()