#Ejercicio1
print("Hola mundo!")

#Ejercicio2
print("Ingrese su nombre")

nombre = input()

print(f"Hola {nombre}!")


#Ejercicio3
print("Ingrese su nombre: ")
nombre = input()

print ("Ingrese su apellido: ")
apellido = input()

print ("Ingrese su edad: ")
edad = input()

print("Ingrese su lugar de residencia")
residencia =input()

print(f"Su nombre completo es {nombre} {apellido} , reside en {residencia} y tiene {edad} años")

#Ejercicio4
print("Ingrese el rádio de el círculo para así calcular su área y perímetro")
radio = float (input())

pi = 3.14
area = pi * radio * radio

perimetro = 2 * pi * radio

print(f"El área del círculo es igual a {area} mientras que el perímetro es igual a {perimetro} ")

#Ejercicio5
print("Ingrese la cantidad de segundo para luego calcular a cuantas horas equivale")
segundos = int(input ())

horas = segundos / 3600

print(f"{segundos} segundos equivale a {horas} horas ")

#Ejercicio6
print("Ingrese un número del 1 al 10 para ver su tabla de multiplicar: ")
numero = int(input())
i = int()
for i in range (1, 11):
    print(f"{numero} x {i} = {numero*i}")

#Ejercicio7
print("Ingrese dos números enteros distintos de 0")
numero1 = int(input())
numero2 = int(input())

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = float(numero1 / numero2)

print(f"El resultado de sumar ambos números es igual a {suma}")
print(f"El resultado de restar el numero 1 menos el numero 2 es igual a {resta}")
print(f"El resultado de multiplicar ambos numeros es igual a {multiplicacion}")
print(f"El resultado de dividir el primero por el segundo es igual a {division}")

#Ejercicio8
print("Ingrese su peso: ")
peso = int(input())
print("Ingrese su altura expresado en metros")
altura = float(input())

imc = peso/ (altura * altura)

print(f"Su índice de masa corporal es {imc}")

#Ejercicio9
print("Ingrese la temperatura en grados Celcius para luego convertirla en Farenheit")
gradosc = int(input())

farenheit = (9/5 * gradosc) + 32

print(f"La temperatura en grados farenheit es igual a {farenheit}")

#Ejercicio10
print ("Ingrese tres números")
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

promedio = (numero1 + numero2 + numero3)/3
print(f"El promedio es igual a {promedio}")


