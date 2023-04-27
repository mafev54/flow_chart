cantidad_palabras = int(
    (input("Ingrese la cantidad de palabras que va a escribir : ")))

for i in range(1, cantidad_palabras+1):
    palabras = str((input(
        "Digite las palabras, ¡Esto solo imprimira las palabras que empiecen por p!: ")))
    if (palabras[0] == ("p")):
        print(palabras)
