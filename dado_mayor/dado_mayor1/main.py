from jugador import Jugador
from banca import Banca

jugador_a = Jugador("A")
jugador_b = Jugador("B")
banca = Banca(jugador_a, jugador_b)     # los argumentos son dos instancias de la clase Jugador

resultado = banca.jugar()
print(resultado)