'''Crea un programa que simule una tienda de ropa donde
el usuario preguntará el precio de algun producto y se
mostrara el valor de es producto:
Pantalon cuesta 1.000
Camiseta cuesta 700
Zapatos cuesta 500
El programa deberá mostrar un menú inicial de los
productos y luego le preguntará al usuario de los
productos disponibles cual desea conocer su precio
(si el usuario ingresa un producto que no es valido le dirá
que ese producto no está disponible que elija uno
disponible)'''


# Definir los precios de los productos
precios = {
    "Pantalon": 1000,
    "Camiseta": 700,
    "Zapatos": 500
}

def mostrar_menu():
    """
    Función que muestra el menú de productos disponibles.
    """
    print("Bienvenido a la tienda de ropa.")
    print("Estos son los productos disponibles:")
    for producto in precios:
        print(f"{producto} - ${precios[producto]}")

def consultar_precio():
    """
    Función que solicita al usuario el producto del que desea conocer el precio.
    """
    producto = input("¿Qué producto desea conocer el precio? ").capitalize()
    if producto in precios:
        print(f"El precio del {producto} es ${precios[producto]}")
    else:
        print(f"Lo siento, no tenemos '{producto}' disponible en la tienda.")

# Ejecutar el programa
mostrar_menu()
consultar_precio()