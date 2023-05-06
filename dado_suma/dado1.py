#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Reglas del juego:
1 Son dos jugadores que realizan tiradas alternativas de un dado de seis caras. 
2 Van lanzando el dado alternativamente en cada tirada, por ejemplo, primero el jugador A y luego el jugador B, y así sucesivamente. 
3 Gana el juego el jugador que obtenga un mayor número de puntos al sumar los resultados obtenidos en las cuatro tiradas.
'''

from random import seed, randint
seed()

class Dado:
    '''Representa un dado de seis caras y 
    tiene un método para lanzarlo y obtener
     un resultado aleatorio entre 1 y 6'''
    
    def __init__(self):
        self.caras = 6
    
    def lanzar(self):
        return randint(1, self.caras)
    



class Jugador:
    '''Representa a un jugador y 
    lleva un registro de sus puntos acumulados'''

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def agregar_puntos(self, puntos):
        self.puntos += puntos




class Juego:
    '''Clase que coordina el juego, 
    incluyendo la creación de los jugadores, el dado y
    la lógica para determinar el ganador'''

    def __init__(self, jugador1, jugador2, tiradas=4):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.tiradas = tiradas
        self.dado = Dado()

    def jugar(self):
        for _ in range(self.tiradas):
            self.jugador1.agregar_puntos(self.dado.lanzar())
            self.jugador2.agregar_puntos(self.dado.lanzar())

        if self.jugador1.puntos > self.jugador2.puntos:
            ganador = self.jugador1
        elif self.jugador1.puntos < self.jugador2.puntos:
            ganador = self.jugador2
        else:
            ganador = None

        return ganador




if __name__ == "__main__":
    '''Se crean dos jugadores, Alice y Bob, y 
    luego se crea un juego con ellos.
    Finalmente el juego se juega y se determina el ganador.
    Si hay un ganador, se imprime su nombre y puntos;
    si no, se imprime que hay un empate.'''
    
    jugador1 = Jugador("Luis")
    jugador2 = Jugador("Sara")

    juego = Juego(jugador1, jugador2)

    ganador = juego.jugar()
    
    if ganador:
        print(f"Ha ganado {ganador.nombre} con {ganador.puntos} puntos.")
    else:
        print(f"¡Empate a {jugador1.puntos} puntos!")

    print(f'\t{jugador1.nombre}: {jugador1.puntos} puntos.')
    print(f'\t{jugador2.nombre}: {jugador2.puntos} puntos.')
    print()