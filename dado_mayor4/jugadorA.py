import random

class JugadorA:
    def __init__(self, num_final):
        self.nombre = "A"
        self.num_final = num_final

    def jugar(self):
        return random.randint(1, self.num_final)