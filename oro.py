from carta import *
import random

class oro(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
    
    def asignar_valores(self):
        super().agregar_valores(74, 90, 0, 0.05)
        
    def calcular_quimica(self,pais_favorito,equipo_favorito):
        return super().calcular_quimica(pais_favorito,equipo_favorito)