import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def jugar(self):
        return random.randint(1, 6)




class Banca:
    def __init__(self, jugadores):
        self.jugadores = jugadores
    
    def jugar(self):
        maximo = 0
        ganador = None
        
        for jugador in self.jugadores:
            numero = jugador.jugar()
            print(jugador.nombre, "ha sacado un", numero)
            
            if numero > maximo:
                maximo = numero
                ganador = jugador.nombre
        
        return ganador

jugadores = [Jugador("Jugador 1"), Jugador("Jugador 2"), Jugador("Jugador 3"), Jugador("Jugador 4"), Jugador("Jugador 5")]
banca = Banca(jugadores)

ganador = banca.jugar()
print("El ganador es:", ganador)
