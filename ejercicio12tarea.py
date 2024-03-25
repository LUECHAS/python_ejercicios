'''
Escribe un programa que te ayude a saber si un número es
positivo, negativo o cero. Primero, pídele al usuario que te
dé un número. Después, verifica si el número que te dio es
mayor que 0, menor que 0 o igual a 0. Si es mayor que 0,
dile al usuario que el número es positivo. Si es menor que 0,
dile que es negativo. Y si es igual a 0, dile que es cero.
Finalmente, muéstrale al usuario el resultado.

(Sin usar if, else o elif)
'''
def verificar_numero():
    numero = float(input("Por favor, ingresa un número: "))
    resultado = {numero > 0: "El número ingresado  es positivo", 
                 numero < 0: "El número ingresado es negativo", 
                 numero == 0: "El número ingresado es cero"}
    print(resultado[True])

verificar_numero()
