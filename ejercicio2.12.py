
'''
Escribe un programa que solicite al usuario
ingresar un numero y luego le diga si ese numero
es positivo,negativo o igual a cero.
'''
# Solicitar al usuario que ingrese un número
numero = float(input("Ingresa un número: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número", numero, "es positivo.")
elif numero < 0:
    print("El número", numero, "es negativo.")
else:
    print("El número es igual a cero.")