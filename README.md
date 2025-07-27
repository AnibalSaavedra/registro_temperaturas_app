
# Registro Automático de Temperaturas - Laboratorio

Esta aplicación permite registrar automáticamente las mediciones de temperatura de equipos de laboratorio, asociándolas con fecha, hora y operador. Todos los registros son almacenados automáticamente en un archivo Excel.

## 🧪 Funcionalidades

- Ingreso de nombre del equipo
- Registro automático de fecha y hora
- Registro de temperatura en °C
- Selección de operador desde una lista desplegable
- Visualización en tiempo real de los registros
- Exportación automática a Excel (`registro_temperaturas.xlsx`)

## ▶️ Cómo usar

1. Instala Streamlit y dependencias:
```bash
pip install streamlit pandas openpyxl
```

2. Ejecuta la app:
```bash
streamlit run registro_temperaturas_app.py
```

## 📁 Archivos del repositorio

- `registro_temperaturas_app.py` – Código fuente de la app
- `registro_temperaturas.xlsx` – Archivo donde se almacenan los registros
- `README.md` – Descripción del proyecto
- `LICENSE.txt` – Licencia de uso restringido

## ⚠️ Licencia

Este software es de uso restringido. No está permitido distribuir, modificar ni usar sin autorización escrita del autor.

© Aníbal Saavedra 2025.
