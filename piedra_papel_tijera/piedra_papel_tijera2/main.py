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

# Definimos una subclase Opcion que hereda de Jugada y representa una opción genérica del juego
class Opcion(Jugada):
    # Definimos el método constructor que recibe el nombre y la lista de opciones a las que gana
    def __init__(self, nombre, gana_a):
        self.nombre = nombre # Asignamos el nombre de la opción
        self.gana_a = gana_a # Asignamos la lista de opciones a las que gana

    # Definimos el método comparar para la clase Opcion
    def comparar(self, otra):
        # Usamos el atributo nombre para verificar el tipo de la otra jugada
        if self.nombre == otra.nombre:
            return 0 # Empate
        elif otra.nombre in self.gana_a:
            return 1 # Victoria
        else:
            return -1 # Derrota

    # Definimos el método que devuelve el nombre de la opción
    def __str__(self):
        return self.nombre

# Definimos una lista con las posibles opciones del juego
opciones = [
    Opcion("piedra", ["tijera"]), # La piedra gana a la tijera
    Opcion("papel", ["piedra"]), # El papel gana a la piedra
    Opcion("tijera", ["papel"]) # La tijera gana al papel
]

# Definimos una función que simula una partida entre dos jugadores
def partida(jugador1, jugador2):
    # Elegimos una opción al azar para cada jugador
    opcion1 = random.choice(opciones)
    opcion2 = random.choice(opciones)
    # Imprimimos las opciones elegidas
    print(f"{jugador1} elige {opcion1}")
    print(f"{jugador2} elige {opcion2}")
    # Comparamos las opciones y devolvemos el resultado
    resultado = opcion1.comparar(opcion2)
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
juego(5)