class Banca:
    def __init__(self, jugador_a, jugador_b):
        self.jugador_a = jugador_a
        self.jugador_b = jugador_b
    
    def jugar(self):
        numero_a = self.jugador_a.lanzar_dado()
        numero_b = self.jugador_b.lanzar_dado()

        if numero_a > numero_b:
            return f"El ganador es {self.jugador_a.nombre} con {numero_a} puntos, {self.jugador_b.nombre} sacó solo {numero_b} {'punto' if numero_b==1 else 'puntos'}."
        elif numero_b > numero_a:
            return f"El ganador es {self.jugador_b.nombre} con {numero_b} puntos, {self.jugador_a.nombre} sacó solo {numero_a} {'punto' if numero_a==1 else 'puntos'}."
        else:
            return f"Se ha producido un Empate a {numero_a} {'punto' if numero_a==1 else 'puntos'}."
        # se usa el operador ternario para escribir punto o puntos