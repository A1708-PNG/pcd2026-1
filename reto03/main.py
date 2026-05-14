import sys
import math

def main():
    productos = {}
    
    linea_header = sys.stdin.readline()
    if not linea_header:
        return

    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue
        
        partes = linea.split(',')
        if len(partes) != 4:
            continue
            
        nombre_producto = partes[1].strip()
        
        try:
            cantidad = int(partes[2])
            precio_unitario = float(partes[3])
            
            if cantidad < 0 or not math.isfinite(precio_unitario) or precio_unitario < 0:
                continue
                
        except (ValueError, IndexError):
            continue 
           
        if nombre_producto not in productos:
            productos[nombre_producto] = [0, 0.0]
    
        stats = productos[nombre_producto]
        stats[0] += cantidad
        stats[1] += cantidad * precio_unitario

    reporte_final = []
    for prod, datos in productos.items():
        unidades = datos[0]
        ingreso = datos[1]
        promedio = ingreso / unidades if unidades > 0 else 0.0
        reporte_final.append((prod, unidades, ingreso, promedio))
    
    reporte_ordenado = sorted(
        reporte_final, 
        key=lambda x: (-x[2], x[0])
    )

    sys.stdout.write("producto,unidades_vendidas,ingreso_total,precio_promedio\n")
    for prod, unidades, ingreso, promedio in reporte_ordenado:
        sys.stdout.write(f"{prod},{unidades},{ingreso:.2f},{promedio:.2f}\n")

if __name__ == "__main__":
    main()