'''Crear un programa en Python que, al solicitar al usuario
su peso en kilogramos y su altura en metros, calcule el
Índice de Masa Corporal utilizando la fórmula imc= peso(kg)/altura(m)2
Luego, determinar en qué categoría de peso se encuentra
la persona según los estándares de la Organización
Mundial de la Salud (OMS): bajo peso (IMC < 18.5), peso
normal (18.5 <= IMC < 25), sobrepeso (25 <= IMC < 30) y
obesidad (IMC >= 30). Finalmente, imprimir el IMC
calculado y la categoría de peso correspondiente.
'''# Función para obtener un valor numérico válido
def obtener_valor_valido(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que cero. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

# Función para determinar la categoría de peso según el IMC
def determinar_categoria_peso(imc):
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    return categoria

# Solicitar el peso y la altura al usuario
peso = obtener_valor_valido("Ingresa tu peso en kilogramos: ")
altura = obtener_valor_valido("Ingresa tu altura en metros: ")

# Calcular el IMC
imc = peso / (altura ** 2)

# Determinar la categoría de peso
categoria_peso = determinar_categoria_peso(imc)

# Mostrar el resultado
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
print(f"Categoría de peso: {categoria_peso}")