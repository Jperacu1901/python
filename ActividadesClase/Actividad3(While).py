Nombre = input("Introduce tu nombre: ")

bucle = 0

while bucle == 0:
    Nota = int(input("Introduce tu nota: "))
    if Nota >= 5 and Nota <=10:
        print("Felicidades aprobaste")
        bucle = bucle + 1
    elif Nota < 5:
        print("Suspendiste")
    else:
        print("Introduce una nota valida")
        