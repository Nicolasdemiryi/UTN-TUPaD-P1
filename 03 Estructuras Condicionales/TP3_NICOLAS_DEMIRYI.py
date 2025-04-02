# Ejercicio 1
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("Es mayor de edad.")

    # Ejercicio 2
nota_usuario = int(input("Ingrese su nota: "))
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

    # Ejercicio 3
numero_ingresado = int(input("Ingrese un número par: "))
if (numero_ingresado % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")

    # Ejercicio 4
edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada < 12: 
    print ("Niño/a")
elif edad_ingresada >= 12 and edad_ingresada < 18:
    print("Adolescente")
elif edad_ingresada >= 18 and edad_ingresada < 30:
    print("Adulto/a joven")
else:
    print("Adulto")

    # Ejercicio 5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if (len(contraseña) >= 8) and (len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    # Ejercicio 6
from statistics import mode, mean, median
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
if (mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Sesgo positivo o a la derecha")
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)) and (median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print("Sesgo negativo o a la izquierda")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo")


# Ejercicio 7
frase_usuario = input("Ingrese una palabra: ")
if (frase_usuario[-1] == "a") or (frase_usuario[-1] == "e") or (frase_usuario[-1] == "i") or (frase_usuario[-1] == "o") or (frase_usuario[-1] == "u") :
    print(f"{frase_usuario}!")
else: 
    print(frase_usuario)

    # Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("Ingrese el número 1 si quiere su nombre en mayúsculas.")
print("Ingrese el número 2 si quiere su nombre en minúsculas")
print("Ingrese el número 3 si quiere su nombre con la primera letra mayúscula.")
numero_elegido = int(input("Ingrese su número: "))

if numero_elegido == 1:
    print(nombre.upper())
elif numero_elegido == 2:
    print(nombre.lower())
else:
    print(nombre.title())

    # Ejercicio 9

escala = float(input("Ingrese la magnitud del terremoto: "))

if escala < 3:
    print("Muy leve (imperceptible)")
elif escala >=3 and escala < 4:
    print("Leve (ligeramente perceptible)")
elif escala >=4 and escala < 5:
    print("Moderado (sentido por personas pero generalmente no causa daños)")
elif escala >=5 and escala < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")   
elif escala >=6 and escala < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif escala >=7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Ha ingresado un número incorrecto intente nuevamente")

    # Ejercicio 10
hemisferio = input("Ingrese en que hemisferio se encuentra sea N (hemisferio norte) o S (hemisferio sur): ")
mes = int(input("Ingrese en que mes del año se encuentra (formato 1- 12): "))
dia = int(input("Ingrese el día del mes en el que se encuentra: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno") 
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 20) or (7 <= mes <=8) or (mes == 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano") 
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 20) or (7 <= mes <=8) or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio incorrecto")