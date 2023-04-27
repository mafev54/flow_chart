contador = 0
e_mail = input("Introduce tu direccion de email: ")

for i in e_mail:
    if (i == "@" or i == "."):

        contador = contador+1

if contador == 2:
    print("email es correcto")
else:
    print("El email no es correcto")
