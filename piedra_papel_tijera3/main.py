# Importamos el módulo random para generar números aleatorios
import random

# Definimos una clase abstracta Jugada que representa una elección del juego
class Jugada:
    # Definimos un método abstracto que compara dos jugadas y devuelve el resultado
    def comparar(self, otra):
        pass

    # Definimos un método que devuelve el nombre de la jugada
    def __str__(self):
        return self.__class__.__name__

# Definimos una subclase Piedra que hereda de Jugada
class Piedra(Jugada):
    # Definimos el método comparar para la clase Piedra
    def comparar(self, otra):
        # Usamos el operador isinstance para verificar el tipo de la otra jugada
        if isinstance(otra, Piedra):
            return 0 # Empate
        elif isinstance(otra, Papel):
            return -1 # Derrota
        elif isinstance(otra, Tijera):
            return 1 # Victoria

# Definimos una subclase Papel que hereda de Jugada
class Papel(Jugada):
    # Definimos el método comparar para la clase Papel
    def comparar(self, otra):
        if isinstance(otra, Piedra):
            return 1 # Victoria
        elif isinstance(otra, Papel):
            return 0 # Empate
        elif isinstance(otra, Tijera):
            return -1 # Derrota

# Definimos una subclase Tijera que hereda de Jugada
class Tijera(Jugada):
    # Definimos el método comparar para la clase Tijera
    def comparar(self, otra):
        if isinstance(otra, Piedra):
            return -1 # Derrota
        elif isinstance(otra, Papel):
            return 1 # Victoria
        elif isinstance(otra, Tijera):
            return 0 # Empate

# Definimos una lista con las posibles jugadas
opciones = [Piedra(), Papel(), Tijera()]

# Definimos una función que simula una partida entre dos jugadores
def partida(jugador1, jugador2):
    # Elegimos una jugada al azar para cada jugador
    jugada1 = random.choice(opciones)
    jugada2 = random.choice(opciones)
    # Imprimimos las jugadas elegidas
    print(f"{jugador1} elige {jugada1}")
    print(f"{jugador2} elige {jugada2}")
    # Comparamos las jugadas y devolvemos el resultado
    resultado = jugada1.comparar(jugada2)
    return resultado

# Definimos una función que simula un juego de varias partidas hasta que haya un ganador
def juego(partidas):
    # Inicializamos los contadores de victorias para cada jugador
    victorias1 = 0
    victorias2 = 0
    # Iteramos hasta que uno de los jugadores alcance el número de partidas requerido para ganar el juego
    while victorias1 < partidas and victorias2 < partidas:
        # Simulamos una partida entre los dos jugadores y guardamos el resultado
        resultado = partida("Jugador 1", "Jugador 2")
        if resultado == 1:
            victorias1 += 1 # El jugador 1 gana la partida y suma una victoria
        elif resultado == -1:
            victorias2 += 1 # El jugador 2 gana la partida y suma una victoria
        # Imprimimos el marcador actual del juego
        print(f"Marcador: Jugador 1 {victorias1} - Jugador 2 {victorias2}")
        print()
    # Imprimimos el resultado final del juego según el número de victorias de cada jugador
    if victorias1 > victorias2:
        print(f"Jugador 1 gana el juego por {victorias1} a {victorias2}")
    else:
        print(f"Jugador 2 gana el juego por {victorias2} a {victorias1}")

# Llamamos a la función juego con el número de partidas que se deben ganar para terminar el juego (por ejemplo, 3)
juego(3)