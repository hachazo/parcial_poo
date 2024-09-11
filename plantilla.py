class Plantilla:
    def __init__(self,usuario,pais_favorito,equipo_favorito):
        self.__usuario = usuario
        self.__pais_favorito = pais_favorito
        self.__equipo_favorito = equipo_favorito
        self.__cartas = []
        
    def agregar_carta(self,carta):
        self.__cartas.append(carta)
    
    def imprimir_plantilla(self):
        for carta in self.__cartas:
            carta.imprimir()
            
    def calcular_quimica(self):
        quimica_total = 0
        for carta in self.__cartas:
            quimica_total += carta.calcular_quimica(self.__pais_favorito,self.__equipo_favorito)
        print(f"La quimica total de la plantilla es: {quimica_total}")