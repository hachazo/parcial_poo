import random

class Carta:
    def __init__(self, nombre,club, pais, habilidad):
        self._nombre = nombre
        self._club = club
        self._pais = pais
        self._habilidad = habilidad
        self._velocidad = 0
        self._tiro = 0
        self._regate = 0
        self._defensa = 0
        self._pase = 0
        self._fisico = 0

    def agregar_valores(self,min,max,suma,porcentaje):
        if suma != None:
            self._velocidad = random.randint(min, max) + suma
            self._tiro = random.randint(min, max) + suma
            self._regate = random.randint(min, max) + suma
            self._defensa = random.randint(min, max) + suma
            self._pase = random.randint(min, max) + suma
            self._fisico = random.randint(min, max) + suma
        
        if porcentaje != None:
            self._velocidad = (random.randint(min, max) + (random.randint(1, 2)) * porcentaje)
            self._tiro = (random.randint(min, max) + (random.randint(1, 2)) * porcentaje)
            self._regate = (random.randint(min, max) + (random.randint(1, 2)) * porcentaje)
            self._defensa = (random.randint(min, max) + (random.randint(1, 2)) * porcentaje)
            self._pase = (random.randint(min, max) + (random.randint(1, 2)) * porcentaje)
            self._fisico = (random.randint(min, max) + (random.randint(1, 2)) * porcentaje)

    def imprimir(self):
        print(self._club)
        print("")
        print("Habilidad especial:")
        print(self._habilidad)
        print("")
        print(self._nombre)
        print(self._pais)
        print(f"Velocidad: {self._velocidad} Tiro: {self._tiro}")
        print(f"Regate: {self._regate} Defensa: {self._defensa}")
        print(f"Pases: {self._pase} Fisico: {self._fisico}")
        print("----------------------------")
        