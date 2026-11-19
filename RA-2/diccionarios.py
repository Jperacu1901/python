notas = {
    "Ana": 8,
    "Luis": 6,
    "Marta": 9,
    "Pedro": 5
}

print("\n1 -> Consultar informacion")
print(f"La nota de Ana es {notas['Ana']}")

nota_luis = notas["Luis"]
print(f"La nota de Luis es {nota_luis}")

print("\n2 -> Consultar una clave inexistente")
print(notas.get("Elena", "Alumno no encontrado"))

print("\n3 -> Añadir y modificar datos")
notas["Elena"] = 7
notas["Pedro"] = 6
print("Diccionario actualizado:", notas)

print("4 -> Eliminar informacion")
del notas["Luis"]
print("Diccionario actualizado (borrar):", notas)

print("\n5 -> Recorrer claves y valores")
print("Nobres de los alumnos:")
for nombre in notas.keys():
    print(f"- {nombre}")

print("\nNotas del grupo")
for nota in notas.values():
    print(f"- {nota}")

print("\nListado completo")
for nombre in sorted(notas.keys()):
    print(f"{nombre}: {notas[nombre]}")

print("\n7 -> Comprobar si existe un alumno")
if "Marta" in notas:
    print("Marta esta registrada")
else:
    print("Marta no esta registrada")

if "Luis" not in notas:
    print("Luis no esta registrado")
else:
    print("Luis esta registrado")

print("\n8 -> Mostrar notas sin repetir")
notas_unicas = sorted(set(notas.values()))
print("Notas diferentes ordenadas:")
for nota in notas_unicas:
    print(f"- {nota}")