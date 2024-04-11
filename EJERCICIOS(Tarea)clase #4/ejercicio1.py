'''Crea una calculadora sea capaz de operar dos números con varias
funciones como suma, resta, multiplicacion y division, Este programa
deberá tener un menú inicial que le pregunte al usuario que operación
desea realizar una vez el usuario seleccione la operación a realizar le
pedirá los dos números a operar .'''

def sumar(a, b):
    """Función que realiza la suma de dos números"""
    return a + b

def restar(a, b):
    """Función que realiza la resta de dos números"""
    return a - b

def multiplicar(a, b):
    """Función que realiza la multiplicación de dos números"""
    return a * b

def dividir(a, b):
    """Función que realiza la división de dos números"""
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return a / b

def calculadora():
    """Función principal que maneja el menú y la lógica de la calculadora"""
    print("Bienvenido a la calculadora")
    print("por favor, Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación (1-5): ")

    # Verifica la opción seleccionada por el usuario
    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = sumar(a, b)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = restar(a, b)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = multiplicar(a, b)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = dividir(a, b)
        print(f"El resultado de la división es: {resultado}")
    elif opcion == "5":
        print("¡Hasta luego!")
        return
    else:
        print("Opción inválida. Intenta de nuevo.")

    # Llama recursivamente a la función calculadora() para permitir más operaciones
    calculadora()

# Llama a la función principal calculadora()
calculadora()