import sys

lineas = sys.stdin.read().strip().split('\n')

productos = {}

for linea in lineas[1:]:
    partes = linea.split(',')

    if len(partes) != 4:
        continue

    fecha = partes[0]
    producto = partes[1].strip()

    if producto == "":
        continue

    try:
        cantidad = int(partes[2])
        precio = float(partes[3])
    except:
        continue

    if producto not in productos:
        productos[producto] = {
            "unidades": 0,
            "ingreso": 0.0
        }

    productos[producto]["unidades"] += cantidad
    productos[producto]["ingreso"] += cantidad * precio

for producto in productos:
    unidades = productos[producto]["unidades"]
    ingreso = productos[producto]["ingreso"]

    if unidades > 0:
        productos[producto]["promedio"] = ingreso / unidades
    else:
        productos[producto]["promedio"] = 0

lista_ordenada = sorted(
    productos.items(),
    key=lambda x: x[1]["ingreso"],
    reverse=True
)

print("producto,unidades_vendidas,ingreso_total,precio_promedio")

for nombre, datos in lista_ordenada:
    unidades = datos["unidades"]
    ingreso = datos["ingreso"]
    promedio = datos["promedio"]

    print(f"{nombre},{unidades},{ingreso:.2f},{promedio:.2f}")