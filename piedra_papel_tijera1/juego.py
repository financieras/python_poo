# Importamos las clases Juez y Jugador de los ficheros Juez.py y Jugador.py
from juez import Juez
from jugador import Jugador

# Creamos una instancia de la clase Juez pasando como argumento el número de rondas que se van a jugar (por ejemplo, 3)
juez = Juez(3)

# Creamos dos instancias de la clase Jugador pasando como argumento el nombre de cada jugador (por ejemplo, A y B)
jugador_A = Jugador("A")
jugador_B = Jugador("B")

# Imprimimos un mensaje de inicio del juego
print("Comienza el juego de piedra, papel o tijera")

# Mientras no se haya terminado el juego, repetimos los siguientes pasos
while not juez.fin_del_juego():
  # El juez elige una opción al azar
  juez.elegir_opcion()
  # El juez muestra la opción elegida a los jugadores
  juez.mostrar_opcion()
  # Los jugadores eligen una opción según su algoritmo
  jugador_A.elegir_opcion()
  jugador_B.elegir_opcion()
  # Los jugadores envían sus opciones al juez y las muestran por pantalla
  jugador_A.enviar_opcion(juez)
  jugador_B.enviar_opcion(juez)
  # El juez compara las opciones de los jugadores y determina el ganador de la ronda
  juez.comparar_opciones(jugador_A.eleccion, jugador_B.eleccion)
  # Imprimimos un salto de línea para separar las rondas
  print()

# Cuando se termina el juego, el juez muestra el resultado final y el ganador o si hay un empate
juez.mostrar_resultado()