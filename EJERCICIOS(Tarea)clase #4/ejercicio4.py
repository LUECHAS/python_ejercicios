'''Crea un programa donde el usuario tenga que adivinar una palabra
secreta para eso el usuario tendrá intentos infinitos y le darás una
pista al iniciar el programa, si el usuario ingresa una palabra
incorrecta le darás otra pista eso significa que el usuario tendrá dos
pistas la que le darás al iniciar el programa y al equivocarse, si el
usuario acierta el programa le dirá: ¡Felicidades! ¡Has adivinado la
palabra secreta! Gracias por jugar.

Al iniciar el programa decirle al usuario: Bienvenido al juego de
adivinar la palabra secreta.
Aquí tienes una pista: (la pista según tu palabra secreta)'''

import random

# Definir las palabras secretas y sus pistas
palabras_secretas = {
    "python": "Es un lenguaje de programación muy popular.",
    "libro": "Se usa para leer y escribir.",
    "manzana": "Es una fruta roja y crujiente.",
    "computadora": "Es un dispositivo electrónico que procesa información."
}

# Elegir una palabra secreta al azar
palabra_secreta = random.choice(list(palabras_secretas.keys()))
pista_inicial = palabras_secretas[palabra_secreta]

def adivinar_palabra():
    """
    Función que permite al usuario adivinar la palabra secreta.
    """
    intentos = 0
    pista_extra = ""

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print(f"Aquí tienes una pista: {pista_inicial}")

    while True:
        intento = input("Ingresa tu intento: ").lower()

        if intento == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            print("Gracias por jugar.")
            return
        else:
            intentos += 1
            if intentos == 1:
                pista_extra = ", y aquí tienes otra pista: " + palabras_secretas[palabra_secreta]
                print(f"Incorrecto. Tienes {intentos} intento{'' if intentos == 1 else 's'}{pista_extra}")
            else:
                print(f"Incorrecto. Tienes {intentos} intentos{pista_extra}")

adivinar_palabra()