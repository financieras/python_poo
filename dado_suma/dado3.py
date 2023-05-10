#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Reglas del juego:
1 Son dos o más jugadores que realizan 4 tiradas alternativas de un dado de seis caras. 
2 Van lanzando el dado alternativamente en cada tirada y acumulando puntos.
3 Gana el juego el jugador que obtenga un mayor número de puntos al sumar los resultados obtenidos en las cuatro tiradas.
4 Los nombres de los jugadores se asignan automaticante con las 26 letras mayúsculas del alfabeto.
5 El juego de juega de forma automática y finalmente se imprimen el ganador o ganadores si hay empate y las puntuaciones de todos.
'''

from random import seed, randint
seed()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0

    def tirar_dado(self):
        return randint(1, 6)

class Juego:
    def __init__(self, num_jugadores):
        self.num_jugadores = num_jugadores
        self.jugadores = []
        self.letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(num_jugadores):
            nombre = self.letras[i]
            jugador = Jugador(nombre)
            self.jugadores.append(jugador)

    def jugar(self):
        for i in range(4):
            for jugador in self.jugadores:
                jugador.puntuacion += jugador.tirar_dado()
    
        max_puntuacion = max(jugador.puntuacion for jugador in self.jugadores)
        ganadores = [jugador for jugador in self.jugadores if jugador.puntuacion == max_puntuacion]
    
        if len(ganadores) == 1:
            print("El ganador es el jugador", ganadores[0].nombre, "con", ganadores[0].puntuacion, "puntos.")
        else:
            print("Hay un empate entre los siguientes jugadores:")
            for ganador in ganadores:
                print("Jugador", ganador.nombre, "con", ganador.puntuacion, "puntos.")
    
        print("\nPuntuaciones:")
        for jugador in self.jugadores:
            print("Jugador", jugador.nombre, ":", jugador.puntuacion)

if __name__ == "__main__":
    num_jugadores = 4
    juego = Juego(num_jugadores)
    juego.jugar()