from carta import *
import random

class Carta_especial(Carta):
    def __init__(self, nombre, club, pais, habilidad):
        super().__init__(nombre, club, pais, habilidad)
        
    def asignar_valores(self):
        super().agregar_valores(89, 98.8, None, 0.02)
        