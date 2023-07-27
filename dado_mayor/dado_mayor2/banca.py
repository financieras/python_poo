class Banca:
    def __init__(self, jugador_a, jugador_b):
        self.jugador_a = jugador_a
        self.jugador_b = jugador_b
    
    def jugar(self):
        numero_a = self.jugador_a.lanzar_dado()
        numero_b = self.jugador_b.lanzar_dado()
        
        if numero_a > numero_b:
            return "Gana el jugador A"
        elif numero_b > numero_a:
            return "Gana el jugador B"
        else:
            return "Empate"
