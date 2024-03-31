'''Escribe un programa que solicite al usuario ingresar dos numeros
y luego determine cual es el mayor de los dos.
Solicitar al usuario ingresar dos numeros'''
#Solicitar al usuario ingresar dos numeros
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Ahora, ingresa el segundo número: "))

#Verificar cual es el mayor
if numero1 > numero2:
  print("El primer número ingresado es mayor.")
elif numero1 < numero2:
  print("El segundo número ingresado es mayor.")
else:
  print("Ambos números son iguales.")
