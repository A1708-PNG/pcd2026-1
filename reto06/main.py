import sys
import re

# Constantes definidas por el profesor
DEPARTAMENTOS_VALIDOS = {'VEN', 'ADM', 'TEC', 'LOG', 'RHH'}
SERIES_VALIDAS = {'A', 'B', 'C', 'D', 'E'}

# Pre-compilación de patrones para máximo rendimiento (1M+ registros)
# Patrones Flexibles (para detectar tipo)
P_PROD_FLEX = re.compile(r'^[a-zA-Z]{3}-\d{4}-[a-zA-Z]{2}$')
P_ENV_FLEX  = re.compile(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$')
P_EMP_FLEX  = re.compile(r'^EMP-[a-zA-Z]{3}-\d{4}$')
P_FAC_FLEX  = re.compile(r'^FAC-[a-zA-Z]-\d{6}$')

# Patrones Estrictos (para validar contenido)
P_PROD_STRICT = re.compile(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$')
P_EMP_STRICT  = re.compile(r'^EMP-([A-Z]{3})-(\d{4})$')
P_FAC_STRICT  = re.compile(r'^FAC-([A-Z])-\d{6}$')

def detectar_tipo(codigo):
    """Detecta el tipo de codigo por su estructura flexible."""
    if P_PROD_FLEX.match(codigo): return "producto"
    if P_ENV_FLEX.match(codigo):  return "envio"
    if P_EMP_FLEX.match(codigo):  return "empleado"
    if P_FAC_FLEX.match(codigo):  return "factura"
    return "desconocido"

def validar_producto(codigo):
    """Valida que categoria y pais sean mayúsculas."""
    return P_PROD_STRICT.match(codigo) is not None

def validar_envio(codigo):
    """Valida rangos de fecha (año 2020-2030, mes 01-12, dia 01-31)."""
    m = P_ENV_FLEX.match(codigo)
    if m:
        # Extraer partes usando split para evitar grupos de captura extras si no es necesario
        partes = codigo.split('-')
        try:
            anio, mes, dia = int(partes[1]), int(partes[2]), int(partes[3])
            if not (2020 <= anio <= 2030): return False
            if not (1 <= mes <= 12): return False
            if not (1 <= dia <= 31): return False
            # Opcional: validación de días por mes
            if mes in {4, 6, 9, 11} and dia > 30: return False
            if mes == 2:
                bisiesto = (anio % 4 == 0)
                if dia > (29 if bisiesto else 28): return False
            return True
        except ValueError:
            return False
    return False

def validar_empleado(codigo):
    """Valida departamento válido y número no empieza con 0."""
    m = P_EMP_STRICT.match(codigo)
    if m:
        depto = m.group(1)
        numero = m.group(2)
        # Regla: Depto válido y no empezar con 0
        return depto in DEPARTAMENTOS_VALIDOS and not numero.startswith('0')
    return False

def validar_factura(codigo):
    """Valida serie A-E en mayúscula."""
    m = P_FAC_STRICT.match(codigo)
    if m:
        serie = m.group(1)
        return serie in SERIES_VALIDAS
    return False

def validar_codigo(codigo):
    """Detecta tipo y valida. Retorna (tipo, es_valido)."""
    tipo = detectar_tipo(codigo)
    if tipo == "producto":
        return tipo, validar_producto(codigo)
    elif tipo == "envio":
        return tipo, validar_envio(codigo)
    elif tipo == "empleado":
        return tipo, validar_empleado(codigo)
    elif tipo == "factura":
        return tipo, validar_factura(codigo)
    else:
        return "desconocido", False

def main():
    # Optimización para salida masiva
    write = sys.stdout.write
    write("codigo,tipo,valido\n")
    
    for linea in sys.stdin:
        codigo = linea.strip()
        if not codigo:
            continue
        tipo, es_valido = validar_codigo(codigo)
        resultado = "VALIDO" if es_valido else "INVALIDO"
        write(f"{codigo},{tipo},{resultado}\n")

if __name__ == "__main__":
    main()