'''Escribe un programa en Python que solicite al usuario
que ingrese tres notas y luego clasifique el promedio de
estas notas en una de las siguientes categorías:

"Sobresaliente" si el promedio es mayor o igual a 90.
"Notable" si el promedio está entre 70 y 89.
"Aprobado" si el promedio está entre 60 y 69.
"Reprobado" si el promedio es menor a 60.
'''
# Función para obtener y validar las notas
def obtener_notas():
    notas = []
    for i in range(3):
        while True:
            nota = input(f"Ingresa la nota {i+1}: ")
            if nota.replace(".", "").isdigit() and 0 <= float(nota) <= 100:
                notas.append(float(nota))
                break
            else:
                print("Entrada inválida. Ingresa un valor numérico entre 0 y 100.")
    return notas

# Función para calcular el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Función para clasificar el promedio
def clasificar_promedio(promedio):
    if promedio >= 90:
        categoria = "Sobresaliente"
    elif promedio >= 70:
        categoria = "Notable"
    elif promedio >= 60:
        categoria = "Aprobado"
    else:
        categoria = "Reprobado"
    return categoria

# Solicitar las notas al usuario
notas = obtener_notas()

# Calcular el promedio
promedio = calcular_promedio(notas)

# Clasificar el promedio
categoria = clasificar_promedio(promedio)

# Mostrar el resultado
print(f"El promedio de tus notas es: {promedio:.2f}")
print(f"Categoría: {categoria}")