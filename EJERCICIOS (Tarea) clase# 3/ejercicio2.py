'''Este ejercicio en Python solicita la edad de un estudiante y la
clasifica en categorías como niño, adolescente, adulto joven,
adulto y anciano. Luego de ingresar la edad, el programa
devuelve la categoría correspondiente. Si se ingresa una edad
negativa, el programa solicita una entrada válida.'''

# Función para solicitar y validar la edad
def obtener_edad():
    while True:
        edad = input("por favor, Ingresa tu edad: ")
        
        # Verificar si la edad es un número entero válido
        if edad.isdigit():
            edad = int(edad)
            
            # Verificar si la edad es mayor o igual a cero
            if edad >= 0:
                return edad
            else:
                print("La edad debe ser un número positivo. Intenta nuevamente.")
        else:
            print("Entrada inválida. Ingresa un número entero.")

# Función para clasificar la edad
def clasificar_edad(edad):
    if edad < 13:
        categoria = "Niño"
    elif edad < 20:
        categoria = "Adolescente"
    elif edad < 30:
        categoria = "Adulto joven"
    elif edad < 60:
        categoria = "Adulto"
    else:
        categoria = "Anciano"
    
    return categoria

# Solicitar la edad al usuario
edad = obtener_edad()

# Clasificar la edad y mostrar la categoría
categoria = clasificar_edad(edad)
print(f"Con {edad} años, eres un(a) {categoria}.")