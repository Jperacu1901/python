class perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.energia = 100
    def jugar(self):
        self.energia = max(0, self.energia -10)
    def descansar(self):
        self.energia = max(0, self.energia + 10)

perro1 = perro("Pepe",3)
perro2 = perro("Milo", 5)

perro1.jugar()

print(perro1.nombre)
print(perro1.energia)
print(perro2.energia)

perro1.descansar()
print(perro1.energia)