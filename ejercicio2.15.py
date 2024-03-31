'''Escribe un programa que solicite al usuario ingresar un
numero entero e indique si es par o impar.'''
#Solicitar al usuario ingresar un número entero
numero = int(input("Ingrese un número entero: "))

#Verificar si el número es par
if numero % 2 == 0:
  print(f"El número {numero} es par.")
else:
  print(f"El número {numero} es impar.")
