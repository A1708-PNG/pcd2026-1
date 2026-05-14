# Reto Semana 06 - Validador de Códigos con Regex

Este programa procesa códigos de identificación (productos, envíos, empleados y facturas) utilizando expresiones regulares para validar su estructura y reglas de negocio.

## Estructura de Códigos Soportada
- **Productos**: `XXX-NNNN-XX` (Letras mayúsculas, 4 números).
- **Envíos**: `ENV-YYYY-MM-DD-NNNNNN` (Rango 2020-2030, fechas reales).
- **Empleados**: `EMP-XXX-NNNN` (Solo áreas VEN, TEC, ADM).
- **Facturas**: `FAC-X-NNNNNN` (Series A a la E).

## Uso
Para ejecutar el validador con un archivo de texto:
```bash
python main.py < tests/codigos.txt

##Requisitos
Python 3.x

Módulo re (estándar)
