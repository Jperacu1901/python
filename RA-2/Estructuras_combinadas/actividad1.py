libros = [
    {"titulo": "Python fácil", "autor": "Ana", "paginas": 120},
    {"titulo": "Redes básicas", "autor": "Luis", "paginas": 95},
    {"titulo": "Bases de datos", "autor": "Marta", "paginas": 150}
]

print("1 -> Titulo del libro 1:", libros[0]["titulo"])
print("2 -> Autor del libro 2:", libros[1]["autor"])

libros[1]["paginas"] = 110

libros.append({"titulo": "HTML inicial", "autor": "Eva", "paginas": 80})

print("\nListado de libros:")
for libro in libros:
    print(f"- {libro['titulo']} ({libro['paginas']} páginas)")

print(f"Total de libros en la biblioteca: {len(libros)}")