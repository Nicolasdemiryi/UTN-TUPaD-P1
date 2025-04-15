# Ejercicio 1

# Definicion de la funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")



# Prpograma principal
imprimir_hola_mundo()

# Ejercicio 2

# Definicion de la funcion
def saludo_usuario(nombre):
    return f"Hola {nombre}!"



# Prpograma principal
nombre_usuario = input("Ingresa tu nombre: ")
saludo = saludo_usuario(nombre_usuario)
print(saludo)


# Ejercicio 3
# Deficion de funciones
def informacion(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Programa principal
nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("¿Dónde vivís?: ")

informacion(nombre, apellido, edad, residencia)


# Ejercicio 4
import math

# Definicion de funciones
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresá el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


# Ejercicio 5
# Definicion de funciones
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos_ingresados = float(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos_ingresados)

print(f"{segundos_ingresados} segundos equivalen a {horas:.2f} horas.")


# Ejercicio 6
# Definicion de funciones
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# Ejercicio 7
# Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

resultado = operaciones_basicas(a, b)

print(f"Resultados para los números {a} y {b}:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")


# Ejercicio 8
# Definicion de funciones
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresá tu peso en kilogramos: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")


# Ejercicio 9
# Definicion de funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


# Ejercicio 10
# Definicion de funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los números {a}, {b} y {c} es: {promedio:.2f}")