mision = input("bienvenido a la isla tu mision sera encontrar el tesoro.Escribe izquierda o derecha para continuar ")
if mision == "izquierda":
    mision2 = input("nadar o esperar ")
    if mision2 == "esperar":
        puerta = input("Hay tres puertas:roja, amarilla y azul . ¿cual puerta escoges? ")
        if puerta == "amarilla":
            bosque = input('''elije un bosque
1.bosque encantado
2.bosque con animales
3.bosque con zombies y humanos''')
            if bosque == "bosque encantado":
                print("te encuentras con criaturas misticas nunca antes vistas y sigues en la busqueda del tesoro ")
                decision = input('''que decides:
1.encontrar el tesoro
2. no encontrar el tesoro ''')
                if decision == "encontrar el tesoro":
                    print("encontrarte tu tesoro. FELICIDADES!! ")
                elif decision == "no encontrar el tesoro":
                    print("¡nunca podras salir del bosque encantado! ")
            elif bosque == "bosque con animales":
                print("en este bosque tienes que sobrevivir ya que solo hay animales salvajes y eres el único humano ")
                decision2 = input("¿decides encontrar el tesoro? responde si o no segun lo que quieras ")
                if decision2 == "si":
                    print("en tu gran busqueda del tesoro, lo has encontrado")
                elif decision2== "no":
                    print("has muerto en una estampida de bufalos ")
            elif bosque =="bosque con zombies y humanos":
                print("eres atacado por zombies y tienes que encontrar refugio con los humanos ")
                decision3 = input("elige zombie o no zombie ")
                if decision3 == "zombie":
                    print("resulta que te mueres a los pocos dias, y encuentras el tesoro en uno de tus sueños. felicidades has encontrado el tesoro ")
                elif decision3 == "no zombie":
                    print("buscas el tesoro y lo encuentras ")
        elif puerta == "roja":
            print("eres quemado GAME OVER ")
        elif puerta == "azul":
            print("devorado por bestias, GAME OVER ")
    elif mision2 == "nadar": 
        print("atacado por una tribu, GAME OVER ")
elif mision == "derecha":
    print("caiste en un agujero, GAME OVER ")