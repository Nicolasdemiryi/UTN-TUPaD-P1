print("Ingrese su peso: ")
peso = int(input())
print("Ingrese su altura expresado en metros")
altura = float(input())

imc = peso/ (altura * altura)

print(f"Su índice de masa corporal es {imc}")