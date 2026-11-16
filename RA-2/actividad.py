NombreCompleto = input("Introuduce su nombre y apelliddos:")
Edad = int(input("Introduce su edad:"))
NModulos = int(input("Introduce el numero de modulos que has cursado:"))
PrecioM = float(input("Introduce el precio de los modulos:"))
NotaMedia = float(input("Introduce su nota media:"))
Distancia = float(input("Introduce su distancia al centro(KM):"))
ayuda = False

importe_inicial = NModulos * PrecioM

if NModulos >= 6:
    descuento = importe_inicial * 0.10
else:
    descuento = 0

importe_final = importe_inicial - descuento

if NotaMedia >= 7 and Distancia >= 20:
    ayuda = True
else:
    ayuda = False

print("====== RESUMEN DE MATRÍCULA ======\n")
print("Alumno:",NombreCompleto)
print("Edad:", Edad, "años")
print("Modulos matriculados:", NModulos)
print("Precio por modulo:",PrecioM,"\n")

print("Importe inicial:", importe_inicial)
print("Descuento:",descuento)
print("Importe final:",importe_final,"\n")

print("Nota media:", NotaMedia)
print("Distancia al centro:",Distancia,"KM")
print("Cumple con los requisitos para solicitar la ayuda:", ayuda)
