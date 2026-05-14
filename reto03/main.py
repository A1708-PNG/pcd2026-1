import sys
import math

def solucionar():
    header = sys.stdin.readline()
    if not header:
        return

    productos = {}

    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue
            
        partes = linea.split(',')
        if len(partes) != 4:
            continue

        nombre = partes[1].strip()
        if not nombre:
            continue

        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
            
            if not math.isfinite(precio):
                continue
                
        except ValueError:
            continue

        if nombre in productos:
            datos = productos[nombre]
            datos[0] += cantidad
            datos[1] += cantidad * precio
        else:
            productos[nombre] = [cantidad, cantidad * precio]

    resultado = []
    for nombre, (unidades, ingreso) in productos.items():
        promedio = ingreso / unidades if unidades > 0 else 0.0
        resultado.append((nombre, unidades, ingreso, promedio))

    resultado.sort(key=lambda x: (-x[2], x[0]))

    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for nombre, unidades, ingreso, promedio in resultado:
        sys.stdout.write(f"{nombre},{unidades},{ingreso:.2f},{promedio:.2f}\n")

if __name__ == "__main__":
    solucionar()