Nombre = input("Introduce tu nombre: ")
Cantidad = int(input("Cuantas asignaturas cursas?: "))

print("LISTA DE ASIGNATURAS")

for i in range(Cantidad):
    asignatura = input("Introduce el nombre de la asignatura: ")
    print(f"Asignatura  {i + 1}: {asignatura}")
    
