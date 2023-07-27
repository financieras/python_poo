from jugador import Jugador
from banca import Banca

jugador_a = Jugador("A")
jugador_b = Jugador("B")
banca = Banca(jugador_a, jugador_b)

resultado = banca.jugar()
print(resultado)
