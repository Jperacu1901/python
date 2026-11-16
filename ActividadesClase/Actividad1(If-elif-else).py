print("Calculadora de caramelos")
edad = int(input("Cuantos años tienes? "))
nombre = input("Cual es tu nombre? ")
ncaramelos = 0

if edad < 6:
    ncaramelos = 10
elif edad > 6 and edad < 12:
    ncaramelos = 7
elif edad > 12 and edad < 17:
    ncaramelos = 4
else:
    ncaramelos = 1

print(f"{nombre} tienes {edad} años por lo que consigues {ncaramelos}")
