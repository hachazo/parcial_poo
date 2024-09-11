from bronce import *
from especial import *
from oro import *
from plantilla import *

habilidades_especiales = ["Ataque", "Pase", "Defensa"]
clubes = ["Arsenal", "Montevideo City Torque", "Inter Miami", "Manchester City"]
paises = ["Argentina", "Inglaterra", "Holanda", "Japón"]

# creamos dos plantillas
plantilla1 = Plantilla("Usuario1", "Argentina", "Arsenal")
plantilla2 = Plantilla("Usuario2", "Inglaterra", "Manchester City")

# creamos una lista de 11 cartas
cartas = []

for i in range(11):
    carta_bronce = Carta_bronce(f"Jugador{random.randint(1,30)}", random.choice(clubes), random.choice(paises), random.choice(habilidades_especiales))
    cartas.append(carta_bronce)
    
    carta_oro = oro(f"Jugador{random.randint(1,30)}", random.choice(clubes), random.choice(paises))
    cartas.append(carta_oro)
    
    carta_especial = Carta_especial(f"Jugador{random.randint(1,30)}", random.choice(clubes), random.choice(paises), random.choice(habilidades_especiales))
    cartas.append(carta_especial)

# nezclamos las cartas y las añadimos a la plantilla
random.shuffle(cartas)
for carta in cartas:
    carta.asignar_valores()
    plantilla1.agregar_carta(carta)

random.shuffle(cartas)
for carta in cartas:
    carta.asignar_valores()
    plantilla2.agregar_carta(carta)

# imprimimos las plantillas
print("Plantilla 1:")
plantilla1.imprimir_plantilla()
plantilla1.calcular_quimica()

print("Plantilla 2:")
plantilla2.imprimir_plantilla()
plantilla2.calcular_quimica()