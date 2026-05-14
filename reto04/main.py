#!/usr/bin/env python3

import math
from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"

def crear_productos(datos_raw):
    productos = []

    for datos in datos_raw:
        sku = datos.get('sku')
        nombre = datos.get('nombre', '').strip()
        categoria = datos.get('categoria')
        precio_raw = datos.get('precio')
        stock_raw = datos.get('stock')
        stock_min_raw = datos.get('stock_minimo')

        es_valido, error = validar_producto(
            sku, nombre, categoria, precio_raw, stock_raw, stock_min_raw
        )

        if not es_valido:
            continue

        try:
            precio = float(precio_raw)
            stock = int(stock_raw)
            stock_minimo = int(stock_min_raw)

            if not math.isfinite(precio):
                continue
                
        except (ValueError, TypeError):
            continue

        producto = Producto(
            sku,
            nombre,
            categoria,
            precio,
            stock,
            stock_minimo
        )
        productos.append(producto)

    return productos

def main():
    datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    productos = crear_productos(datos_raw)

    necesitan = [p for p in productos if p.necesita_reorden()]

    # ORDENAMIENTO DOBLE:
    # 1. Unidades faltantes descendente (-p.unidades_faltantes())
    # 2. Nombre alfabético ascendente (p.nombre)
    necesitan.sort(key=lambda p: (-p.unidades_faltantes(), p.nombre))

    escribir_reporte(necesitan, ARCHIVO_REPORTE)

if __name__ == "__main__":
    main()