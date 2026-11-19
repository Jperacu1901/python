inventario = {
    "P01": {"nombre": "Teclado", "stock": 8},
    "P02": {"nombre": "Ratón", "stock": 12},
    "P03": {"nombre": "Monitor", "stock": 4}
}

print("1. Producto P02:", inventario["P02"]["nombre"])

print("2. Stock de P03:", inventario["P03"]["stock"])

inventario["P01"]["stock"] = 10


inventario["P04"] = {"nombre": "Auriculares", "stock": 6}

print("\nInventario completo:")
for codigo, datos in inventario.items():
    print(f"Código: {codigo} | Producto: {datos['nombre']} | Stock: {datos['stock']} unidades")