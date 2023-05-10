#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Reglas del juego:
1 Son dos o más jugadores que realizan tiradas alternativas de un dado de seis caras. 
2 Van lanzando el dado alternativamente en cada tirada.
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

    def __init__(self, jugadores, tiradas=4):
        self.jugadores = jugadores   # lista de jugadores
        self.tiradas = tiradas
        self.dado = Dado()

    def jugar(self):
        for _ in range(self.tiradas):
            for jugador in self.jugadores:
                jugador.agregar_puntos(self.dado.lanzar())

        max_puntos = max(jugador.puntos for jugador in self.jugadores)
        jugadores_con_max_puntos = [jugador for jugador in self.jugadores if jugador.puntos == max_puntos]

        return jugadores_con_max_puntos


if __name__ == "__main__":
    '''Se crean varios jugadores y luego se crea un juego con ellos.
    Finalmente el juego se juega y se determina el o los ganadores.
    Verificamos si hay más de un jugador en la lista jugadores_con_max_puntos 
    para determinar si hay un empate o un ganador único.'''
    
    jugadores = [Jugador("A"), Jugador("B"), Jugador("C")]

    juego = Juego(jugadores)

    jugadores_con_max_puntos = juego.jugar()

    if len(jugadores_con_max_puntos) == 1:
        ganador = jugadores_con_max_puntos[0]
        print(f"Ha ganado {ganador.nombre} con {ganador.puntos} puntos.")
    else:
        print("¡Empate entre los siguientes jugadores!")
        for jugador in jugadores_con_max_puntos:
            print(f'\t{jugador.nombre}: {jugador.puntos} puntos.')

    print("\nPuntuaciones finales:")
    for jugador in jugadores:
        print(f'\t{jugador.nombre}: {jugador.puntos} puntos.')
    print()