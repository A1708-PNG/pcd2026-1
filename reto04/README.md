# Sistema de Inventario Modular

## Descripción
Este proyecto es un sistema de inventario que permite:

- Leer productos desde un archivo CSV
- Validar los datos
- Detectar productos con stock bajo
- Generar un reporte de reorden

---

## Estructura del Proyecto
reto_semana_04/
├── main.py
├── README.md
├── .gitignore
├── models/
│ ├── init.py
│ └── producto.py
├── utils/
│ ├── init.py
│ ├── io.py
│ └── validators.py
├── data/
│ └── inventario.csv
└── outputs/
└── reporte_inventario.csv


---

## Como Ejecutar

```bash
python main.py