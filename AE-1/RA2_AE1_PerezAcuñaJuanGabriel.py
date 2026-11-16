Nequipos = 0

while True:
    try:
        Nequipos = int(input("Introduce el numero de equipos: "))
        if 1 <= Nequipos <= 30:
            break
        else:
            print("El valor debe ser entre 1-30")
    except ValueError:
        print("Error: Debe ingresar un numero entero")

Estados = []
Incidencia_Leve = 0
Incidencia_Grave = 0
Correctos = 0

for equipo_id in range(1, Nequipos + 1):
    while True:
        try:
            print("\n--- Equipo {equipo_id} ---")
            print("0 -> Equipo Correcto")
            print("1 -> Incidencia Leve")
            print("2 -> Incidencia Grave")
            print("9 -> Salir del sistema")
            
            codigo = int(input(f"Equipo {equipo_id} - Introduce estado: "))

            if codigo not in (0, 1, 2, 9):
                print("Codigo no valido")
                continue
            break  
        except ValueError:
            print("Error: Ingrese un valor numerico")
            continue

    if codigo == 9:
        print("Saliendo del registro de equipos...")
        break

    Estados.append(codigo)

    if codigo == 0:
        Correctos += 1
    elif codigo == 1:
        Incidencia_Leve += 1
    elif codigo == 2:
        Incidencia_Grave += 1

if Incidencia_Grave or Incidencia_Leve > (Nequipos/2):
    Situacion = "Atencion"
else:
    Situacion = "Bien" 

total_registrados = len(Estados)

print("\nEstado de los equipos\n")
print(f"Total de equipos a registrar iniciales: {Nequipos}")
print(f"Total de equipos registrados: {total_registrados}")
print(f"- Equipos Correctos (0): {Correctos}")
print(f"- Incidencias Leves (1): {Incidencia_Leve}")
print(f"- Incidencias Graves (2): {Incidencia_Grave}")

if total_registrados > 0:
    correctos = (Correctos / total_registrados) * 100
    leves = (Incidencia_Leve / total_registrados) * 100
    graves = (Incidencia_Grave / total_registrados) * 100

    print("\nPorcentajes:")
    print(f"Correctos: {correctos:.2f}%")
    print(f"Incidencias Leves: {leves:.2f}%")
    print(f"Incidencias Graves: {graves:.2f}%")
    print(f"Situacion del aula: {Situacion}")
else:
    print("No se registraron datos de ningun equipo")