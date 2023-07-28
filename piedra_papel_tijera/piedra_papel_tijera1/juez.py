# Importamos el módulo random para generar números aleatorios
import random

# Definimos la clase Juez
class Juez:

  # Definimos el constructor de la clase que recibe el número de rondas que se van a jugar
  def __init__(self, rondas):
    # Asignamos el número de rondas al atributo self.rondas
    self.rondas = rondas
    # Creamos un diccionario que guarda las opciones posibles y sus valores numéricos
    self.opciones = {"piedra": 0, "papel": 1, "tijera": 2}
    # Creamos una lista que guarda los nombres de las opciones en orden
    self.nombres = ["piedra", "papel", "tijera"]
    # Creamos un atributo que guarda la opción elegida por el juez en cada ronda
    self.eleccion = None
    # Creamos un atributo que guarda el número de rondas ganadas por cada jugador
    self.puntuacion = {"A": 0, "B": 0}

  # Definimos un método que elige una opción al azar y la guarda en self.eleccion
  def elegir_opcion(self):
    # Generamos un número aleatorio entre 0 y 2
    numero = random.randint(0, 2)
    # Asignamos la opción correspondiente al número a self.eleccion
    self.eleccion = self.nombres[numero]

  # Definimos un método que muestra la opción elegida por el juez a los jugadores
  def mostrar_opcion(self):
    # Imprimimos un mensaje con la opción elegida por el juez
    print(f"El juez ha elegido {self.eleccion}")

  # Definimos un método que recibe las opciones de los jugadores y las compara con la del juez para determinar el ganador de la ronda
  def comparar_opciones(self, opcion_A, opcion_B):
    # Obtenemos los valores numéricos de las opciones de los jugadores usando el diccionario self.opciones
    valor_A = self.opciones[opcion_A]
    valor_B = self.opciones[opcion_B]
    # Calculamos la diferencia entre los valores de las opciones de los jugadores y la del juez
    diferencia_A = (valor_A - self.opciones[self.eleccion]) % 3
    diferencia_B = (valor_B - self.opciones[self.eleccion]) % 3
    # Si la diferencia es 0, hay un empate entre el jugador y el juez
    if diferencia_A == 0 and diferencia_B == 0:
      # Imprimimos un mensaje de empate
      print("Empate entre los dos jugadores y el juez")
    # Si la diferencia es 1, el jugador gana al juez
    elif diferencia_A == 1 and diferencia_B == 1:
      # Imprimimos un mensaje de victoria de los dos jugadores sobre el juez
      print("Los dos jugadores ganan al juez")
      # Aumentamos en uno el número de rondas ganadas por cada jugador
      self.puntuacion["A"] += 1
      self.puntuacion["B"] += 1
    # Si la diferencia es 2, el jugador pierde contra el juez
    elif diferencia_A == 2 and diferencia_B == 2:
      # Imprimimos un mensaje de derrota de los dos jugadores contra el juez
      print("Los dos jugadores pierden contra el juez")
    # Si solo uno de los jugadores tiene una diferencia de 1, ese jugador gana al juez y al otro jugador
    elif diferencia_A == 1 and diferencia_B != 1:
      # Imprimimos un mensaje de victoria del jugador A sobre el jugador B y el juez
      print(f"El jugador A gana al jugador B y al juez con {opcion_A}")
      # Aumentamos en uno el número de rondas ganadas por el jugador A
      self.puntuacion["A"] += 1
    elif diferencia_A != 1 and diferencia_B == 1:
      # Imprimimos un mensaje de victoria del jugador B sobre el jugador A y el juez
      print(f"El jugador B gana al jugador A y al juez con {opcion_B}")
      # Aumentamos en uno el número de rondas ganadas por el jugador B
      self.puntuacion["B"] += 1

  # Definimos un método que determina si se ha alcanzado el número de rondas necesario para terminar el juego y devuelve True o False
  def fin_del_juego(self):
    # Si alguno de los jugadores ha ganado más rondas que las necesarias para ganar el juego, devolvemos True
    if self.puntuacion["A"] > self.rondas / 2 or self.puntuacion["B"] > self.rondas / 2:
      return True
    # Si no, devolvemos False
    else:
      return False

  # Definimos un método que muestra la puntuación final del juego y el ganador o si hay un empate
  def mostrar_resultado(self):
    # Imprimimos un mensaje con la puntuación final de cada jugador
    print(f"Puntuación final: Jugador A: {self.puntuacion['A']}, Jugador B: {self.puntuacion['B']}")
    # Si el jugador A tiene más puntos que el jugador B, imprimimos un mensaje de victoria del jugador A
    if self.puntuacion["A"] > self.puntuacion["B"]:
      print("El jugador A es el ganador del juego")
    # Si el jugador B tiene más puntos que el jugador A, imprimimos un mensaje de victoria del jugador B  
    elif self.puntuacion["A"] < self.puntuacion["B"]:
      print("El jugador B es el ganador del juego")
    # Si los dos jugadores tienen la misma puntuación, imprimimos un mensaje de empate  
    else:
      print("Hay un empate entre los dos jugadores")