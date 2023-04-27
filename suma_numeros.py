cantidad = int(input("Igrese la cantidad de números: "))
suma = 0

for i in range(1, cantidad+1):
    num = int(input("Digite el número: "))
    suma = suma+num
print("La suma de todos los numeros es: ", suma)
