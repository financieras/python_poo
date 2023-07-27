from jugadorA import JugadorA
from jugadorB import JugadorB
from jugadorC import JugadorC
from jugadorD import JugadorD
from banca import Banca
# Importar más clases Jugador según el número de jugadores

num_final = 10 # Número final del dado
jugadores = [JugadorA(num_final), JugadorB(num_final), JugadorC(num_final), JugadorD(num_final)] # lista de objetos Jugador
banca = Banca(jugadores)

ganador = banca.jugar()
print("El ganador es:", ganador)
