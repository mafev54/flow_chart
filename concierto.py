concierto = input("hay tres generos rock, metal, reggae. elige uno: ")
if concierto == "rock":
    banda = input(" elige una banda: queen, nirvana, guns N' roses")
    if banda == "queen":
        print("precio boleta:US$5.602 ")
    elif banda == "nirvana":
        print("precio boleta:US$2.200 ")
    elif banda == "guns N' roses":
        print("precio boleta:US$2.200 ")
elif concierto == "metal":
    banda2 = input(" elige una banda: black sabbath, metallica, judas priest")
    if banda2 == "black sabbath":
        print("precio boleta:Preferencial : $374000 general 143.000")
    elif banda2 == "metallica":
        print('''precio boleta:Hard Wire (Platino): $380.000 (aforo 10.000)
Battery (VIP): $270.000 (aforo 15.000)
Orion (Gradería): $150.000 (aforo 8.000) ''')
    elif banda2 == "judas priest":
        print('''precio boleta:general (primera etapa):275.000(aforo 9.000
vip (primera etapa): 449.000 (1.500)''')
elif concierto == "reggae":
    print("no hay mas boletas, para ningún concierto de reggae")
