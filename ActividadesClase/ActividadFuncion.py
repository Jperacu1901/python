def recomendar_visita(destino):
    if destino == 1:
        print("Puedes visitar la playa y disfrutar del mar")
    elif destino == 2:
        print("Puedes hacer senderismo y disfrutar de la montaña")
    elif destino == 3:
        print("Puedes visitar museos y monumentos")
    else:
        print("Opción no válida")

nombre = input("Cual es tu nombre?:")

destino = int(input("¿A dónde quieres ir?\n 1) Playa\n 2) Montaña\n 3) Ciudad\n"))
recomendar_visita(destino)


print(f"ADIOS {nombre}")