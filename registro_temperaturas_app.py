
import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Nombre del archivo donde se guardarán los registros
EXCEL_FILE = "registro_temperaturas.xlsx"

# Inicializar archivo si no existe
if not os.path.exists(EXCEL_FILE):
    df_init = pd.DataFrame(columns=[
        "Nombre del Equipo", 
        "Fecha y Hora de Medición", 
        "Temperatura (°C)", 
        "Operador"
    ])
    df_init.to_excel(EXCEL_FILE, index=False)

# Título
st.title("🌡️ Registro Automático de Temperaturas - Laboratorio")

# Formulario
with st.form("form_temperatura"):
    nombre_equipo = st.text_input("Nombre del Equipo")
    temperatura = st.number_input("Temperatura (°C)", step=0.1, format="%.1f")
    operador = st.selectbox("Operador", [
        "Anibal Saavedra", "Stefanie Maureira", "Nycole Farias", "Juan Ramos", 
        "Maria Vera", "Pamela Montenegro", "Keyla Orrego", 
        "Felipe Fernandez", "Paula Gutierrez", "Paola Araya", "Maria Rodriguez"
    ])
    submitted = st.form_submit_button("Registrar")

    if submitted:
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nuevo_registro = pd.DataFrame([{
            "Nombre del Equipo": nombre_equipo,
            "Fecha y Hora de Medición": fecha_hora,
            "Temperatura (°C)": temperatura,
            "Operador": operador
        }])
        df_existente = pd.read_excel(EXCEL_FILE)
        df_actualizado = pd.concat([df_existente, nuevo_registro], ignore_index=True)
        df_actualizado.to_excel(EXCEL_FILE, index=False)
        st.success(f"✅ Registro guardado correctamente a las {fecha_hora}")

# Mostrar registros existentes
if os.path.exists(EXCEL_FILE):
    st.subheader("📋 Registros Anteriores")
    df = pd.read_excel(EXCEL_FILE)
    st.dataframe(df, use_container_width=True)
