import random
from carta import *
class Carta_bronce(Carta):
    def __init__(self, nombre,club, pais, habilidad):
        super().__init__(nombre,club, pais, habilidad)
        
    def asignar_valores(self):
        super().agregar_valores(49, 65, 2, None)