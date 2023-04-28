cantidad = int(input("Ingrese la cantidad de números de las listas: "))

list1 = []
list2 = []

for i in range(cantidad):
    list1.append(int(input("Digite los numeros de la lista 1: ")))
print(list1)

for j in range(cantidad):
    list2.append(int(input("Digite el números de la lista 2: ")))
print(list2)
for k in range(cantidad):
    print("suma list1 + list2: ", list1[k]+list2[k])
