import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def jugar(self):
        return random.randint(1, 6)   # dado
