import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def lanzar_dado(self):
        return random.randint(1, 6)   # dado