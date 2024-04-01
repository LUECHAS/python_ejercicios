'''
Supongamos que estas creando un sistema para verificar la elegibilidad de los
programadores que desean unirse al grupo Elite Programmers GlobaL.
Este grupo tiene
ciertos criterios de elegibilidad que deben cumplir los programadores 
para ser admitidos.
Los criterios son:
Tener al menos 18 anos de edad.
Tener al menos 3 anos de experiencia en programacion.
Haber completado al menos 3 proyectos de programacion.
Escribe un programa en Python que solicite al usuario su edad,anos de 
experiencia en programacion y el numero de proyectos 
de programacion completados.Luego,determina si el programador 
es elegible para unirse al grupo Elite Programmers Global segun tos
criterios de elegibilidad y muestra un mensaje apropiado en consecuencia.
'''



# Solicitar la información al usuario
edad = int(input("por favor, Ingresa tu edad: "))
años_experiencia = int(input("por favor, Ingresa tus años de experiencia en programación: "))
proyectos_completados = int(input("por favor, Ingresa el número de proyectos de programación completados: "))

# Verificar los criterios de elegibilidad
es_elegible = True

# Criterio 1: Tener al menos 18 años de edad
if edad < 18:
    es_elegible = False
    print("No cumples con el requisito de edad mínima (18 años).")

# Criterio 2: Tener al menos 3 años de experiencia en programación
if años_experiencia < 3:
    es_elegible = False
    print("No tienes la experiencia mínima requerida (3 años).")

# Criterio 3: Haber completado al menos 3 proyectos de programación
if proyectos_completados < 3:
    es_elegible = False
    print("No has completado el número mínimo de proyectos requeridos (3 proyectos).")

# Mostrar el resultado final
if es_elegible:
    print("¡Felicidades! Eres elegible para unirte al grupo Elite Programmers Global.")
else:
    print("Lo siento, no cumples con los criterios de elegibilidad para unirte al grupo Elite Programmers Global.")