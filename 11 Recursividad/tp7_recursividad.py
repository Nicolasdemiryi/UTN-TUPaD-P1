# Ejercicio 1

def factorial(n):
    if n ==0 :
        return 1
    else:
        return n * factorial(n - 1)
        



print(factorial(4))


# Ejercicio 2
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la posición
limite = int(input("Introduce la posición hasta la que quieres ver la serie de Fibonacci: "))

# Mostrar la serie completa hasta esa posición
print(f"Serie de fibonacci hasta la posición {limite}: ")
for i in range (limite):
    print(fibonacci(i), end=" ")

# Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1 # Caso base
    else:
        return base * potencia(base, exponente - 1)



base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")



# Ejercicio 4
# Funcion que calcula de binario a decimal
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario (n // 2) + str(n % 2)





# Programa principal que pide un número al usuario
numero = int(input("Ingrese número entero positivo: "))

if numero < 0:
    print("El numero debe ser positivo")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} pasado a decimal es igual a {binario}")



# Ejercicio 5
# Definicion de la funcion
def es_palindromo(palabra):
    if len(palabra) <=1:  # Caso base: una letra (o ninguna) siempre es palíndromo
        return True 
    if palabra [0] != palabra[-1]:  # Si la primera y la última letra no coinciden, no es palíndromo
        return False
    
    return es_palindromo(palabra[1:-1])   # Llamada recursiva con la palabra sin la primera y la última letra





# Programa principal
palabra = input("Introduce una palabra sin espacios ni tildes: ").lower()
if es_palindromo(palabra):
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es palindromo")



# Ejercicio 6
# Funcion recursiva
def suma_digitos(n):
    if n < 10: # Caso base
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)



# Programa principal
print(suma_digitos(451))



# Ejercicio 7
# Funcion Recursiva
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

# Programa principal
print(contar_bloques(3))


# Ejercicio 8

# Funcion Recursiva
def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        # Verificamos el último dígito y llamamos recursivamente con el resto
        ultimo = numero % 10
        resto = numero // 10
        return (1 if ultimo == digito else 0) + contar_digito(resto, digito)

# Programa Principal
print(contar_digito(12233421, 2))
