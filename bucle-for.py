frutas = ["manzana", "pera", "banano", "cereza", "fresa"]
for i in frutas:
    print(f"{i}")

for idx, i in enumerate(frutas):
    print("===================")
    for v in range(len(frutas[idx])):
        print("%d - %s" % (v, frutas[idx][v]))
    print("===================")


# idx = 0, i = manzana
# 1 pera
# 2 banano
# 3 cereza
# 4 fresa

# v = 0
