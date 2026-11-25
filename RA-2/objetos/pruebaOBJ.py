class perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.energia = 100
    def jugar(self):
        self.energia = max(0, self.energia -10)
    def descansar(self):
        self.energia = max(0, self.energia + 10)
    def ladrar(self):
        print(self.nombre + " GUAU!")

class PerroRescate(perro):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

perro1 = PerroRescate("Enrique", 3, "Cena")
print(perro1.nombre)
print(perro1.energia)
perro1.jugar()
print(perro1.energia)



perro1 = perro("Pepe",3)
perro2 = perro("Milo", 5)
perro3 = perro("Ricardo", 67)

perro3.ladrar()

perro1.jugar()

print(perro1.nombre)
print(perro1.energia)
print(perro2.energia)

perro1.descansar()
print(perro1.energia)