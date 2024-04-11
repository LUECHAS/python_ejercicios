'''Crea el mismo programa anterior esta vez solo con 5
intentos y por cada intento le darás una pista diferente de
adivinar o descubrir la palabra correcta'''


import random

# Definir las palabras secretas y sus pistas
palabras_secretas = {
    "python": [
        "Es un lenguaje de programación muy popular.",
        "Empieza con 'P' y termina con 'N'.",
        "Tiene 6 letras.",
        "Es un reptil que también es un lenguaje de programación.",
        "Fue creado a finales de los años 80."
    ],
    "libro": [
        "Se usa para leer y escribir.",
        "Empieza con 'L' y termina con 'O'.",
        "Tiene 5 letras.",
        "Puedes encontrarlos en una biblioteca.",
        "Se hacen con papel y encuadernación."
    ],
    "manzana": [
        "Es una fruta roja y crujiente.",
        "Empieza con 'M' y termina con 'A'.",
        "Tiene 7 letras.",
        "Crece en los árboles.",
        "Contiene vitamina C."
    ],
    "computadora": [
        "Es un dispositivo electrónico que procesa información.",
        "Empieza con 'C' y termina con 'A'.",
        "Tiene 10 letras.",
        "Es fundamental para el trabajo y el entretenimiento.",
        "Funciona con electricidad."
    ]
}

def adivinar_palabra():
    """
    Función que permite al usuario adivinar la palabra secreta.
    """
    palabra_secreta = random.choice(list(palabras_secretas.keys()))
    pistas = palabras_secretas[palabra_secreta]
    intentos_restantes = 5

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print(f"Tienes {intentos_restantes} intentos. ¡Suerte!")

    while intentos_restantes > 0:
        print(f"Pista: {pistas[5 - intentos_restantes]}")
        intento = input("Ingresa tu intento: ").lower()

        if intento == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            print("Gracias por jugar.")
            return
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"Incorrecto. Te quedan {intentos_restantes} intento{'' if intentos_restantes == 1 else 's'}.")
            else:
                print(f"Lo siento, has agotado tus intentos. La palabra secreta era '{palabra_secreta}'.")

adivinar_palabra()