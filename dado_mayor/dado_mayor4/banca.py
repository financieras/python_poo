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
