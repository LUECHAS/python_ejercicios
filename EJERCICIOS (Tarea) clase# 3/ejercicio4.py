'''Escribe un programa en Python para una pizzería que permite al cliente 
seleccionar una pizza del menú y la cantidad deseada, 
y luego calcula el costo total de la orden.
El menú de la pizzería es el siguiente:
Margarita - $10.00
Pepperoni - $12.00
Vegetariana - $11.50
Hawaiana - $13.50
El programa solicita al cliente que seleccione una opción del menú ingresando 
un número del 1 al 4. Luego, solicita al cliente que ingrese la cantidad 
de pizzas que desea ordenar. Basándose en la selección del cliente, 
el programa calcula el costo total de la orden y lo
muestra al cliente.En caso de que el cliente ingrese una opción no válida 
fuera del rango del 1 al 4, el programamuestra un mensaje de error y 
vuelve a solicitar al cliente que ingrese una opción válida.'''

# Menú de la pizzería
menu = {
    1: ("Margarita", 10.00),
    2: ("Pepperoni", 12.00),
    3: ("Vegetariana", 11.50),
    4: ("Hawaiana", 13.50)
}

# Función para obtener una opción válida del menú
def obtener_opcion_menu():
    while True:
        opcion = input("Por favor, seleccione una opción del menú (1-4): ")
        if opcion.isdigit() and int(opcion) in menu:
            return int(opcion)
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú válida.")

# Función para obtener una cantidad válida
def obtener_cantidad():
    while True:
        cantidad = input("Ingrese la cantidad de pizzas que desea ordenar: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            return int(cantidad)
        else:
            print("Cantidad inválida. Intenta nuevamente.")

# Función para calcular el costo total
def calcular_costo_total(opcion, cantidad):
    pizza, precio = menu[opcion]
    costo_total = cantidad * precio
    return costo_total

# Mostrar el mensaje de bienvenida y el menú
print("Bienvenido a la Pizzería Andrés!")
print("\nMenú:")
for opcion, (pizza, precio) in menu.items():
    print(f"{opcion}. {pizza} - ${precio:.2f}")

# Obtener la opción del menú y la cantidad
opcion_menu = obtener_opcion_menu()
cantidad = obtener_cantidad()

# Calcular el costo total
costo_total = calcular_costo_total(opcion_menu, cantidad)

# Mostrar el resultado
pizza, precio = menu[opcion_menu]
print(f"\nEl costo total de su orden es: ${costo_total:.2f}")