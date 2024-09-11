from carta import *
import random

class oro(Carta):
    def __init__(self, nombre, club, pais, habilidad):
        super().__init__(nombre, club, pais, habilidad)
    
    def asignar_valores(self):
        super().agregar_valores(74, 90, None, 0.05)
        