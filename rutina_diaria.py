rutina = input('''Mi rutina diaria.
¿levantarse temprano o no levantarse temprano? ''')
if rutina == "levantarse temprano":
    print("luego me baño y me visto. ")
elif rutina == "no levantarse temprano":
    print("llegar tarde a clase")
    
    
print("entrar a clase")
estudio = input("luego estudio o no estudio ")
if estudio == "estudio":
    print("estudiar y luego ir a break")
elif estudio == "no estudio":
    print("si no estudio, me va mal en el curso")
    
print("luego sigue el break")
descanso = input('''luego en el descanso puedo hacer tres cosas
1. salir
2. alistarme y desayunar
3. dormir ''')

if descanso == "salir":
    print("salgo")
elif descanso == "alistarme y desayunar":
    print("me alisto y desayuno")
elif descanso == "dormir":
    print("duermo")


print("luego del break, estudio de nuevo y luego almuerzo o almuerzo en el break.")
almuerzo = input("¿almuerzo o no almuerzo? ")
if almuerzo == "almuerzo":
    print("almuerzo")
elif almuerzo == " no almuerzo":
    print("almuerzo en segundo break")
    
    
print("vuelvo a entrar a clase, estudio y salgo a segundo break")
opcion2 = input("¿almuerzo o descanso? ")
if opcion2 == "almuerzo":
    print("almuerzo")
elif opcion2 == "descanso":
    print("descanso")
print("luego entro de nuevo a las ultimas clases salgo y descanso")

