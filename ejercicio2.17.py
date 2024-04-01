'''
Escribe un programa que solicite al usuario ingresar el
nombre de un mes y luego indique cuantos dias tiene
ese mes.
'''
#Solicitar al usuario ingresar el nombre del mes
mes = input("Ingrese el nombre del mes: ")

#Convertir el nombre del mes a minúsculas
mes = mes.lower()

#Determinar cuántos días tiene el mes
if mes in ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"):
  dias = 31
elif mes == "febrero":
  # Comprobar si el año es bisiesto
  año = int(input("Ingrese el año: "))
  bisiesto = (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))
  dias = 28 if not bisiesto else 29
else:
  dias = 30

#Imprimir el número de días
print(f"El mes de {mes} tiene {dias} días.")
