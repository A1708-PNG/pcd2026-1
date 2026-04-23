import sys

def limpiar(texto):
    caracteres_validos = '0123456789.-'
    resultado = ''
    for char in texto:
        if char in caracteres_validos:
            resultado += char
    return resultado

def convertir_a_entero(texto):
    if not texto:
        return 0
    try:
        numero = float(texto)
        return int(numero)  
    except ValueError:
        return 0

def procesar_linea(linea):
    if not linea.strip():
        return 0

    valores = linea.split(',')
    suma = 0

    for valor in valores:
        valor = valor.strip()              
        valor = limpiar(valor)             
        numero = convertir_a_entero(valor) 
        suma += numero                     

    return suma


def main():
    contenido = sys.stdin.read().strip()  # ← IMPORTANTE
    lineas = contenido.split('\n')

    for linea in lineas:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()