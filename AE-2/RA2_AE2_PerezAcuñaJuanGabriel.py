def calcular_precio(precio_base, edad):
    if edad < 18:
        return precio_base * 0.80
    return float(precio_base)

def contar_reservas(codigos, codigo_taller):
    contador = 0
    for c in codigos:
        if c == codigo_taller:
            contador += 1
    return contador

def plazas_disponibles(codigos, codigo_taller, capacidad):
    ocupadas = contar_reservas(codigos, codigo_taller)
    return capacidad - ocupadas

def calcular_recaudacion(importes):
    total = 0
    for imp in importes:
        total += imp
    return total

def mostrar_reservas(nombres, codigos, importes):
    if len(nombres) == 0:
        print("No hay reservas registradas\n")
        return
    print("LISTADO DE RESERVAS\n")
    for i in range(len(nombres)):
        if codigos[i] == 1:
            taller_nombre = "Python básico"
        elif codigos[i] == 2:
            taller_nombre = "Automatización"
        else:
            taller_nombre = "Desarrollo web"

        print(f"{i + 1}. Nombre: {nombres[i]} | Taller: {taller_nombre} | Importe: {importes[i]:.2f} €")

def mostrar_informe(codigos, importes):
    cap1, cap2, cap3 = 6, 4, 5
    capacidad_total = cap1 + cap2 + cap3

    res1 = contar_reservas(codigos, 1)
    res2 = contar_reservas(codigos, 2)
    res3 = contar_reservas(codigos, 3)

    total_reservas = len(codigos)

    rec1, rec2, rec3 = 0.0, 0.0, 0.0
    for i in range(len(codigos)):
        if codigos[i] == 1:
            rec1 += importes[i]
        elif codigos[i] == 2:
            rec2 += importes[i]
        elif codigos[i] == 3:
            rec3 += importes[i]

    recaudacion_total = calcular_recaudacion(importes)
    porcentaje_ocupacion = (total_reservas / capacidad_total) * 100

    print("\nINFORME ECONÓMICO Y DE OCUPACIÓN\n")
    print(f"Reservas totales: {total_reservas}")
    print(f"Python básico: {res1} reservas | {rec1:.2f} €")
    print(f"Automatización: {res2} reservas | {rec2:.2f} €")
    print(f"Desarrollo web: {res3} reservas | {rec3:.2f} €")
    print(f"Recaudación total: {recaudacion_total:.2f} €")
    print(f"Ocupación global: {porcentaje_ocupacion:.2f}%")


def main():
    nombres = []
    codigos = []
    importes = []

    cap_python, p_python = 6, 25.0
    cap_auto, p_auto = 4, 40.0
    cap_web, p_web = 5, 35.0

    opcion = 0
    while opcion != 5:
        print("\nSistema de gestion")
        print("1 Nueva reserva")
        print("2 Ver reservas")
        print("3 Consultar plazas")
        print("4 Informe")
        print("5 SALIR")

        opcion_str = input("Seleccione una opcion (1-5): ")

        if opcion_str not in ["1", "2", "3", "4", "5"]:
            print("Opcion no valida")
            continue

        opcion = int(opcion_str)

        if opcion == 1:
            print("Nueva reserva")
            nombre = ""
            while nombre == "":
                nombre = input("Ingrese el nombre: ")
                if nombre == "":
                    print("El nombre no puede estar vacio")

            edad = 0
            while edad < 12 or edad > 99:
                edad = int(input("Ingrese la edad (12-99): "))
                if edad < 12 or edad > 99:
                    print("Error la edad debe estar entre 12 y 99")

            codigo = 0
            while codigo < 1 or codigo > 3:
                print("Talleres:")
                print("1 Python basico 25€")
                print("2 Automatizacion 40€")
                print("3 Desarrollo web 35€")
                codigo = int(input("Seleccione taller (1-3): "))
                if codigo < 1 or codigo > 3:
                    print("Seleccione un codigo correcto")

            if codigo == 1:
                libres = plazas_disponibles(codigos, 1, cap_python)
                precio_base = p_python
            elif codigo == 2:
                libres = plazas_disponibles(codigos, 2, cap_auto)
                precio_base = p_auto
            else:
                libres = plazas_disponibles(codigos, 3, cap_web)
                precio_base = p_web

            if libres <= 0:
                print("No se pudo realizar la reserva: El taller esta lleno")
            else:
                importe_final = calcular_precio(precio_base, edad)
                nombres.append(nombre)
                codigos.append(codigo)
                importes.append(importe_final)
                print(f"Reserva confirmada. Importe: {importe_final:.2f} €")

        elif opcion == 2:
            mostrar_reservas(nombres, codigos, importes)

        elif opcion == 3:
            print("Plazas disponibles")
            libres1 = plazas_disponibles(codigos, 1, cap_python)
            libres2 = plazas_disponibles(codigos, 2, cap_auto)
            libres3 = plazas_disponibles(codigos, 3, cap_web)
                
            print(f"Python básico: {libres1} plazas libres")
            print(f"Automatización: {libres2} plazas libres")
            print(f"Desarrollo web: {libres3} plazas libres")

        elif opcion == 4:
            mostrar_informe(codigos, importes)

        elif opcion == 5:
            print("Adios")

main()