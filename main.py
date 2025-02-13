#Piedra papel o tijera.
import random
import time
#Bad Evil Hippo
def juego():
    computadora = random.randint(1, 3)
    usuario = int(input("Piedra (1) papel (2) o tijera (3)?"))

    if usuario == computadora:
        print("Empate")
    elif usuario == 1 and computadora == 3:
        print("Ganaste! la computadora eligio tijera")
    elif usuario == 2 and computadora == 1:
        print("Ganaste, la computadora eligio piedra")
    elif usuario == 3 and computadora == 2:
        print("Ganaste, la computadora eligio papel")
    else:
        print("perdistes.")
    jugarotravez = input("Quieres jugar denuevo? (S/N)")
    if jugarotravez.lower() == "s":
        juego()
    else:
        print("gracias por jugar")

juego()