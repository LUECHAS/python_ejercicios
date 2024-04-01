'''
Escribe un programa que pida al usuario ingresar
su edad y Luego le diga si es mayor de edad o no.
'''
# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")