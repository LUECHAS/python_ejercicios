'''Escribe un programa en python que solicite al usuario
ingresar su nombre y luego verifique si el
nombre es "Andres".Si el nombre es "Andres",
imprime un mensaje especial de saludo para
Andres de lo contrario,imprime un saludo
generico.'''
#Solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

#Verificar si el nombre es "Andres"
if nombre.lower() == "andres":
  #Mensaje especial de saludo para Andres
  print("¡Hola Andres! Me alegra mucho verte por aquí.")
else:
  #Saludo generico
  print("¡Hola " + nombre + "! Encantado de conocerte.")
