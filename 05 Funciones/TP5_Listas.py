# Ejercicio 1

lista = list(range(4, 101, 4)) # Creamos una lista que contiene los multiplos de 4 entre 1 y 100

# Aunque la consigna menciona "del 1 al 100", el primer múltiplo de 4 dentro de ese rango es el 4.
print(lista)


# Ejercicio 2

# Creamos una lista que contiene distintos tipos de datos

listae2 = ["Nicolas", 2.2, True, False, 9]

# Accedemos al cuarto elemento de la lista (índice 3)
impresion_lista = listae2[3]

print(impresion_lista)



# Ejercicio 3

# Creamos la lista vacía 
lista_vacia = []

# Agregamos tres strings en este caso mis nombres y apellido
lista_vacia.append("Nicolas")
lista_vacia.append("Gabriel")
lista_vacia.append("Demiryi")

# Mostramos en consola

print(lista_vacia)



# Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos gato por loro
animales[1] = "loro"

# Reemplazamos pez por oso
animales[3] = "oso"

# Imprimimos en consola
print(animales)



# Ejercicio 5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# El programa muestra una lista de 5 elementos, en este caso números enteros.
# A través de la función remove(max) se quita de la lista el número mayor.



# Ejercicio 6

# Creamos la lista que irá de 5 en 5 de 10 a 30 inclusive.
lista_numeroe6 = list(range(10, 35, 5))

# Definimos lo que queremos mostrar en pantalla indice 0 y 1 
impresion = lista_numeroe6[0:2]

print(impresion)



# Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "golf"
autos[2] = "vento"

print(autos)



# Ejercicio 8

dobles = []

dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)



# Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Agrego "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# Reemplazo "fideos" por "tallarines" en la lista del segundo cliente
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

# Elimino "pan" de la lista del primer cliente
compras[0].remove("pan")

print(compras)



# Ejercicio 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)