# Programado sin POO

from random import seed, randint
seed()

def imprime_matriz():
    global matriz
    for fila in range(len(matriz[0])):
        print(*matriz[fila])

def generar_jugadores(num_jugadores):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(num_jugadores):
        letra = letras[i]
        x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        while matriz[x][y] != '·':
            x, y = randint(0, len(matriz)-1), randint(0, len(matriz)-1)
        matriz[x][y] = letra

def generar_comida(num_comida):
    for i in range(num_comida):
        x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        while matriz[x][y] != '·':
            x, y = randint(0,len(matriz)-1), randint(0, len(matriz)-1)
        matriz[x][y] = randint(1, 9)

if __name__ == "__main__":
    dim = 5
    num_jugadores = 4   # elegir entre 2 y 26
    num_comida = 4      # número de celdas con comida
    matriz = [['·']*dim for _ in range(dim)]
    generar_jugadores(num_jugadores)
    generar_comida(num_comida)
    imprime_matriz()
    print()