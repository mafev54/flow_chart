menu = print("en este restaurante se venden hamburguesas")
tamaño = input("grande o pequeña")
tipo = input("vegana, carne o pollo")
if tipo == "vegana":
    print("aqui tienes tu hamburguesa vegana, disfrutala")
elif tipo == "carne":
    carne = input("res o cerdo")
    if carne == "res":
        input("burguer alemana, burguer golosa, burguer mexicana")
        print("disfruta tu hamburguesa")
    elif carne == "cerdo":
        input("burguer clasica, burguer deliciosa, burguer master")
        print("que la disfrutes")
elif tipo == "pollo":
    print("a nadie le gusta la hamburguesa de pollo")
