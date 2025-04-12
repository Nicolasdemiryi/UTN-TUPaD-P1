# Ejercicio 1

for num in range (0, 101, 1):
    print (num)

# Utilicé el bucle for porque se donde termina mi ciclo.

# Ejercicio 2

numero_ingresado = (input("Ingrese un numero entero: ")) # No definimos como entero porque luego no se pueden contar los caracteres
digito = len(numero_ingresado)     # Nueva función len se usa para contar caracteres de un string
print("El numero ingresado tiene", digito, " digitos")

# Ejercicio 3

numero_1 = int(input("Ingrese un numero entero : "))
numero_2 = int(input("Ingrese otro numero entero: "))

if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1 # Esto permite intercambiar valores para que numero_1 sea siempre menor que numero_2

suma = 0

for cont in range (numero_1 + 1, numero_2):
    suma += cont

print("La suma entre los numeros enteros", numero_1, "y", numero_2, "es igual a: ", suma)


# Ejercicio 4

suma = 0
numero_ingresado = int(input("Ingrese numeros enteros para saber su suma, utilice 0 para cortar. "))

while numero_ingresado != 0:
    suma += numero_ingresado
    numero_ingresado = int(input("Ingrese numeros enteros para saber su suma, utilice 0 para cortar. "))
    

print("El total acumulado es igual a ", suma)


# Ejercicio 5

import random
numero_aleatorio = random.randint(1, 9)
print(numero_aleatorio)
numero_ingresado = int(input("Ingrese un número entre 1 y 9 para ganar la adivinanza"))
suma = 0

while numero_ingresado != numero_aleatorio:
    suma += 1
    numero_ingresado = int(input("Ingrese otro numero del 1 al 9: "))


print("Acertaste el número es ", numero_aleatorio, "e intentaste ", suma, " veces")


# Ejercicio 6

numero_inicio = 0
numero_final = 100

for cont in range (numero_final, numero_inicio - 2, -2):
    print(cont)


# Ejercicio 7

numero_ingresado = int(input("Ingrese un numero entero: "))
numero_inicial = 0
suma = 0
for cont in range (numero_inicial, numero_ingresado + 1, 1):
    suma = suma + cont

print(suma)



# Ejercicio 8
CANTIDAD_NUMEROS = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

print("Ingresa ", CANTIDAD_NUMEROS, "numeros enteros: ")

for cont in range (CANTIDAD_NUMEROS):
    numero_ingresado = int(input(f"Numero {cont + 1} : "))
    
    if numero_ingresado > 0:
        positivos += 1
    elif numero_ingresado < 0:
        negativos += 1

    if (numero_ingresado % 2 == 0):
        pares = pares + 1
    else:
        impares = impares + 1


print("Numeros pares ", pares)
print("Numeros impares", impares)
print("Positivos", positivos)
print("Negativos", negativos)


# Ejercicio 9
CANTIDAD_NUMEROS = 5
suma = 0

print("Ingresa ", CANTIDAD_NUMEROS, "numeros enteros: ")

for cont in range (CANTIDAD_NUMEROS):
    numero_ingresado = int(input(f"Numero {cont + 1} : "))
    suma += numero_ingresado

print("La media de valores ingresados es de: ", (suma/CANTIDAD_NUMEROS))


# Ejercicio 10
numero_ingresado = input("Ingrese el número que desea invertir: ")
numero_invertido = numero_ingresado[::-1]
print(numero_invertido)