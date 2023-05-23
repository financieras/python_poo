# Importamos el módulo random para generar números aleatorios
import random

# Definimos la clase Jugador
class Jugador:

  # Definimos el constructor de la clase que recibe el nombre del jugador
  def __init__(self, nombre):
    # Asignamos el nombre al atributo self.nombre
    self.nombre = nombre
    # Creamos una lista que guarda las opciones posibles
    self.opciones = ["piedra", "papel", "tijera"]
    # Creamos un atributo que guarda la opción elegida por el jugador en cada ronda
    self.eleccion = None

  # Definimos un método que elige una opción según algún algoritmo y la guarda en self.eleccion
  def elegir_opcion(self):
    # En este caso, vamos a usar un algoritmo muy simple que elige una opción al azar
    # Generamos un número aleatorio entre 0 y 2
    numero = random.randint(0, 2)
    # Asignamos la opción correspondiente al número a self.eleccion
    self.eleccion = self.opciones[numero]

  # Definimos un método que envía la opción elegida al juez y la muestra por pantalla
  def enviar_opcion(self, juez):
    # Enviamos la opción elegida al juez usando el método recibir_opcion del juez y pasando como argumentos el nombre y la elección del jugador
    juez.recibir_opcion(self.nombre, self.eleccion)
    # Imprimimos un mensaje con la opción elegida por el jugador
    print(f"El jugador {self.nombre} ha elegido {self.eleccion}")