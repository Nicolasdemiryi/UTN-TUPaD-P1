print("Ingrese un número del 1 al 10 para ver su tabla de multiplicar: ")
numero = int(input())
i = int()
for i in range (1, 11):
    print(f"{numero} x {i} = {numero*i}")
    