'''
Escribe un programa que solicite al usuario ingresar
tres numeros enteros y determine cual es el mayor de
Los tres.
'''#Solicitar al usuario ingresar tres números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

#Determinar el mayor de los tres
mayor = numero1
if numero2 > mayor:
  mayor = numero2
if numero3 > mayor:
  mayor = numero3

#Imprimir el mayor
print(f"El mayor de los tres números es {mayor}")
