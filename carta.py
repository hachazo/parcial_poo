import random
from abc import ABC
class Carta(ABC):
    def __init__(self, nombre,club, pais, habilidad=None):
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
        self._quimica = 0

    def get_quimica(self):
        return self._quimica
    
    def agregar_valores(self,min,max,suma,porcentaje):
            self._velocidad = self.__porcentaje(min,max,suma,porcentaje)
            self._tiro = self.__porcentaje(min,max,suma,porcentaje)
            self._regate = self.__porcentaje(min,max,suma,porcentaje)
            self._defensa = self.__porcentaje(min,max,suma,porcentaje)
            self._pase = self.__porcentaje(min,max,suma,porcentaje)
            self._fisico = self.__porcentaje(min,max,suma,porcentaje)
            
    
    def __porcentaje(self,min,max,suma,porcentaje):
        
        if suma != 0 and suma != None:
            total = random.randint(min, max)
            return total + suma
        
        if porcentaje != 0 and porcentaje != None:
            total = random.randint(min, max)
            return total + (total * porcentaje)  

    def calcular_quimica(self,pais_favorito,equipo_favorito):
        if self._pais == pais_favorito and self._club == equipo_favorito:
            return 100
        elif self._pais == pais_favorito or self._club == equipo_favorito:
            return 80
        else:
            return 0 
        
        
    def imprimir(self):
        print(self._club)
        print("")
        if self._habilidad != None:
            print("Habilidad especial:")
            print(self._habilidad)
            print("")
        print(self._nombre)
        print(self._pais)
        print(f"Velocidad: {self._velocidad} Tiro: {self._tiro}")
        print(f"Regate: {self._regate} Defensa: {self._defensa}")
        print(f"Pases: {self._pase} Fisico: {self._fisico}")
        print("----------------------------")
        