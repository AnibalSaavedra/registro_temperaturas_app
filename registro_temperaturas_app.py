import streamlit as st
import pandas as pd
from datetime import datetime
import os
from io import BytesIO

st.set_page_config(page_title="Registro de Temperaturas", page_icon="🌡️", layout="centered")

st.title("🌡️ Registro de Temperaturas de Equipos de Laboratorio")

# Ruta del archivo Excel
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
    submit = st.form_submit_button("✅ Guardar Registro")

    if submit:
        if equipo and operador:
            nueva_fila = {
                "Nombre del Equipo": equipo.upper(),
                "Fecha y Hora de Medición": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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

# Guardar Excel en memoria para descarga
def to_excel_memory(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    processed_data = output.getvalue()
    return processed_data

excel_bytes = to_excel_memory(df)

# Botón de descarga
st.download_button(
    label="📥 Descargar Registros",
    data=excel_bytes,
    file_name="registro_temperaturas.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Footer
st.markdown("---")
st.markdown("👨‍🔬 **Desarrollado por**: Anibal Saavedra | 🌐 **GitHub**: [anibalsaavedra](https://github.com/anibalsaavedra)")
st.markdown("📧 **Contacto**: anibalsaavedra@example.com")
# Fin del script
st.markdown("🔗 **Licencia**: [MIT](https://opensource.org/licenses/MIT)")
# Fin del script
st.markdown("📅 **Última actualización**: 2023-10-01")
st.markdown("🔗 **Documentación**: [Documentación del Proyecto](https://github.com/anibalsaavedra/temperaturas_app)")   
# Fin del script