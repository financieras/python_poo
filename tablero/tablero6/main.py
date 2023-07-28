'''
Tengo un juego sencillo programado en Python. Es un juego de cero jugadores que desarrolla la partida sobre un tablero. Al ejecutar el juego en Python se ve en la terminal cómo se desarrolla la partida movimiento a moviento, esto es paso a paso. Me gustaría que los movimientos del tablero se pudieran ver en página web por parte de unos pocos clientes, no más de 5. Me gustaría utilizar Flask y WebSockets. Supongamos que el juego utiliza un tablero que  viene dado por una matriz de dimensiones nxn donde n=5. En todos los elementos de la matriz hay un punto medio · salvo en una posición aleatoria donde hay una letra mayúscula A. La letra se mueve aleatoriamente por el tablero. Me gustaría representar este movimiento contínuo utilizando Flask para que se viera en página web. ¿Me puedes ayudar con el código?: 1 Python 2 Flask 3 HTML 4 CSS 5 JS
Comencemos por el código Python que crea la clase Tablero y luego introduzcamos la letra en el tablero en una posición aleatoria y hagamos que se mueva.
'''

import random

class Tablero:
    def __init__(self, n):
        self.n = n
        self.tablero = [['·' for _ in range(n)] for _ in range(n)]
        self.letra_pos = (random.randint(0, n-1), random.randint(0, n-1))
        self.tablero[self.letra_pos[0]][self.letra_pos[1]] = 'A'

    def mover_letra(self):
        x, y = self.letra_pos
        self.tablero[x][y] = '·'
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
        x = max(0, min(x, self.n-1))
        y = max(0, min(y, self.n-1))
        self.letra_pos = (x, y)
        self.tablero[x][y] = 'A'
