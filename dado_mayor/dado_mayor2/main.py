from jugador_a import JugadorA
from jugador_b import JugadorB
from banca import Banca

jugador_a = JugadorA()
jugador_b = JugadorB()
banca = Banca(jugador_a, jugador_b)

resultado = banca.jugar()
print("Resultado del juego: ", resultado)
