nombre =input("Introduce tu nombre, por favor: ")
print("Buenos dias " + nombre + " Para ingresar a esta plataforma debes ser mayor de edad")
edad =int(input("Introduce tu edad, por favor "))
if edad >= 18:
    print("Bienvenido " + nombre + " ya puedes ingresar a la plataforma")
elif edad < 18:
    print("lo siento, no puedes ingresar a la plataforma")