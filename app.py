
import streamlit as st
import pandas as pd
from datetime import datetime
import os
from io import BytesIO

st.set_page_config(page_title="Registro de Temperaturas", page_icon="🌡️", layout="centered")
st.title("🌡️ Registro de Temperaturas de Equipos de Laboratorio")

EXCEL_FILE = "registro_temperaturas.xlsx"

# Cargar o crear DataFrame
if os.path.exists(EXCEL_FILE):
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame(columns=["Nombre del Equipo", "Fecha y Hora de Medición", "Temperatura (°C)", "Operador"])

# Formulario
with st.form("formulario_temperaturas"):
    equipo = st.text_input("🔧 Nombre del Equipo", placeholder="Ej: REFRIGERADOR 1", max_chars=50)
    temperatura = st.number_input("🌡️ Temperatura °C", step=0.1)
    operador = st.selectbox("👤 Operador", [
        "Anibal Saavedra", "Stefanie Maureira", "Nycole Farias", "Juan Ramos",
        "Maria Vera", "Pamela Montenegro", "Keyla Orrego", "Felipe Fernandez",
        "Paula Gutierrez", "Paola Araya", "Maria Rodriguez"
    ])
    fecha_manual = st.date_input("📅 Fecha de Medición (opcional)", value=None)
    hora_manual = st.time_input("🕒 Hora de Medición (opcional)", value=datetime.now().time())

    submit = st.form_submit_button("✅ Guardar Registro")

    if submit:
        if equipo and operador:
            if fecha_manual:
                fecha_hora = datetime.combine(fecha_manual, hora_manual)
            else:
                fecha_hora = datetime.now()

            nueva_fila = {
                "Nombre del Equipo": equipo.upper(),
                "Fecha y Hora de Medición": fecha_hora.strftime("%Y-%m-%d %H:%M:%S"),
                "Temperatura (°C)": temperatura,
                "Operador": operador
            }

            df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)
            st.success("✅ Registro guardado correctamente.")
        else:
            st.warning("⚠️ Debes completar todos los campos.")

# Mostrar registros
st.markdown("### 📋 Registros Anteriores")
st.dataframe(df, use_container_width=True)

# Descargar Excel desde memoria
def to_excel_memory(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

excel_bytes = to_excel_memory(df)

st.download_button(
    label="📥 Descargar Registros",
    data=excel_bytes,
    file_name="registro_temperaturas.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Footer
st.markdown("---")
st.markdown("👨‍🔬 **Desarrollado por**: Anibal Saavedra")
st.markdown("📧 **Contacto**: anibalsaavedra@crb.clinicasdelcobre.cl")
st.markdown("🔗 **Licencia**: [MIT](https://opensource.org/licenses/MIT)")
st.markdown("📅 **Última actualización**: 2025-07-27")
