multiplicando = int(input("Ingrese un numero entero positivo: "))

if multiplicando > 0:
    for multiplicador in range(11):
        print(multiplicando, " x ", multiplicador,
              " = ", multiplicando*multiplicador)
else:
    print("¡NO ES CORRECTO!")
