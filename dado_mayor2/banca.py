class Banca:
    def __init__(self, jugador_a, jugador_b):
        self.jugador_a = jugador_a
        self.jugador_b = jugador_b
    
    def jugar(self):
        numero_a = self.jugador_a.jugar()
        numero_b = self.jugador_b.jugar()
        
        if numero_a > numero_b:
            return "Jugador A"
        elif numero_b > numero_a:
            return "Jugador B"
        else:
            return "Empate"
