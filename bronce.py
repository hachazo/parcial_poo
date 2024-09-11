import random
from carta import *
class Carta_bronce(Carta):
    def __init__(self, nombre,club, pais, habilidad):
        super().__init__(nombre,club, pais, habilidad)
        
    def asignar_valores(self):
        super().agregar_valores(49, 65, 2, 0)
        
    def calcular_quimica(self,pais_favorito,equipo_favorito):
        return super().calcular_quimica(pais_favorito,equipo_favorito)