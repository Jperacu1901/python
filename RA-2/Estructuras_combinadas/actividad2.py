talleres = {
    "Python": ["Ana", "Luis"],
    "Robótica": ["Marta", "Pablo"],
    "Diseño": ["Eva"]
}

print("1 -> Participantes en Python:", talleres["Python"])

print("2 -> Participante 1 de Robótica:", talleres["Robótica"][0])

talleres["Python"].append("Sara")

talleres["Robótica"].remove("Pablo")

print("\nListado de talleres y participantes:")

for taller, participantes in talleres.items():
    print(f"Taller: {taller}")
    for alumno in participantes:
        print(f"  - {alumno}")