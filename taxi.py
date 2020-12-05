import threading
import random
import time
import os

tablero = []
taxis = []
buses = []
peatones = []

class taxi (threading.Thread):
    def __init__(self,TIDTaxi,esta_ocupado):
        threading.Thread__init__(self)
        self.TIDTaxi = TIDTaxi
        self.esta_ocupado = esta_ocupado

    def inicializar(self):
        print("Escribo cosas de hilos")


class bus (threading.Thread):
    capacidad = []

    def __init__(self,TIDBus,capacidad):
        threading.Thread__init__(self)
        self.TIDBus = TIDBus
        self.capacidad = capacidad
    def inicializar(self):
        print("Escribo cosas de hilos")

class peatones (threading.Thread):
    def __init__(self,TIDPeaton,destino):
        threading.Thread__init__(self)
        self.TIDPeaton = TIDPeaton
        self.destino = destino

    def inicializar(self):
        print("Escribo cosas de hilos")

def iniciarTablero():
    global tablero
    for i in range(15):
        tablero.append([])
        for j in range(15):
            tablero[i].append("[ ]")

def printTablero():
    print(len(tablero))
    for i in range(len(tablero)):
        print(tablero[i])

if __name__ == '__main__':
    iniciarTablero()
    printTablero()
    n_taxis = int(input("Escriba el número de taxis que quiere que se inicialicen"))
    for i in n_taxis:
        # Se crea el hilo del taxi
        taxi = taxi()
        taxis.append(taxi)
    n_buses = int(input("Escriba el nímero de buses que quiere que se inicialicen"))

    n_peatones = int(input("Escriba el número de peatones que quiere que se inicialicen"))
    while True:
        fR = random.randint(0,len(tablero)-1)
        cR = random.randint(0,len(tablero)-1)
        tablero[fR][cR] = "[ TAXI ]"
        printTablero()
        tablero[fR][cR] = "[ ]"
        time.sleep(1)


