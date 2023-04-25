egg = print('''¿quieres saber como se hace un huevo frito?
paso 1. necesitaras un huevo.
paso 2. necesitaras una sarten.''')

sarten = input("sarten grande o pequeña? ")
if sarten == "pequeña":
    print("paso 3.ahora sigue la mantequilla ")
    mantequilla = input("para cocinar o para untar ")
    if mantequilla == "para cocinar":
        print("paso 4.aplicar en la sarten por 40 seg")
        tiempo = input('''¿que pasa si la aplico por mas,menos o el tiempo exacto? 
escribe mas,menos o tiempo exacto para saber el resultado ''')
        if tiempo == "mas":
            print("la mantequilla se va a quemar")
        elif tiempo == "menos":
            print("la mantequilla no se va a derretir")
        elif tiempo == "tiempo exacto":
            print("paso 5.ahora echamos el huevo por 5 minutos a llama media")
            tiempo2 = input('''¿que pasa si lo dejo por mas o menos tiempo? 
escribe mas o menos para saber el resultado.
Escribe tiempo exacto para saber el resultado ''')
            if tiempo2 == "mas":
                print("el huevo queda con la yema dura y se quema")
            elif tiempo2 == "menos":
                print("el huevo queda crudo")
            elif tiempo2 == "tiempo exacto":
                print('''resultado final:
ahora que dejaste el huevo por 5 minutos, lo puedes servir en un plato y te lo comes :)''')
    elif mantequilla == "para untar":
        print("se puede quemar, no sirve")
elif sarten == "grande":
    print("no se puede hace un huevo frito en una sarten grande porque quedaria sin forma")



    


    
