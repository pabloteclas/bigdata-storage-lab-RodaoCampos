import streamlit as st
import pandas as pd
from io import BytesIO

# Importar funciones propias
from src.ingest import tag_lineage, concat_bronze
from src.validate import basic_checks
from src.transform import normalize_columns, to_silver

# ---------------------------------------------------------
# Función auxiliar para descarga
def download_df(df: pd.DataFrame, filename: str) -> BytesIO:
    """Convierte un DataFrame en buffer CSV para descarga."""
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    return buffer

# ---------------------------------------------------------
# Interfaz
st.set_page_config(page_title="Big Data Storage Lab", layout="wide")
st.title("📊 Big Data Storage Lab")
st.write("De CSVs heterogéneos a un almacén analítico confiable")

# ---------------------------------------------------------
# Sidebar: configuración de mapping
st.sidebar.header("Configuración de columnas origen")
col_date = st.sidebar.text_input("Columna de fecha en origen", value="date")
col_partner = st.sidebar.text_input("Columna de partner en origen", value="partner")
col_amount = st.sidebar.text_input("Columna de amount en origen", value="amount")

mapping = {
    col_date: "date",
    col_partner: "partner",
    col_amount: "amount",
}

# Subida de archivos
uploaded_files = st.file_uploader(
    "Sube uno o varios archivos CSV",
    type=["csv"],
    accept_multiple_files=True
)

# ---------------------------------------------------------
# Procesamiento
if uploaded_files:
    bronze_frames = []
    for file in uploaded_files:
        # Leer con fallback de encoding
        try:
            df = pd.read_csv(file)
        except UnicodeDecodeError:
            file.seek(0)
            df = pd.read_csv(file, encoding="latin-1")

        # Normalizar y etiquetar linaje
        df = normalize_columns(df, mapping)
        df = tag_lineage(df, source_name=file.name)
        bronze_frames.append(df)

    # Concatenar todos los frames
    bronze = concat_bronze(bronze_frames)

    st.subheader("📂 Bronze Data (unificado)")
    st.dataframe(bronze, use_container_width=True)

    # Validaciones
    errors = basic_checks(bronze)
    if errors:
        st.error("⚠️ Errores encontrados en validaciones básicas:")
        for err in errors:
            st.write(f"- {err}")
    else:
        st.success("✅ Validaciones básicas superadas")

        # Generar Silver
        silver = to_silver(bronze)

        st.subheader("📂 Silver Data (agregado por partner × mes)")
        st.dataframe(silver, use_container_width=True)

        # KPIs simples
        st.subheader("📈 KPIs")
        total_amount = silver["amount"].sum()
        total_partners = silver["partner"].nunique()
        total_months = silver["month"].nunique()

        kpi_cols = st.columns(3)
        kpi_cols[0].metric("Total Amount (EUR)", f"{total_amount:,.2f}")
        kpi_cols[1].metric("Partners únicos", total_partners)
        kpi_cols[2].metric("Meses analizados", total_months)

        # Gráfico
        st.bar_chart(
            silver.groupby("month")["amount"].sum(),
            use_container_width=True
        )

        # Descargas
        st.subheader("⬇️ Descargas")
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "Descargar Bronze CSV",
                data=download_df(bronze, "bronze.csv"),
                file_name="bronze.csv",
                mime="text/csv"
            )
        with col2:
            st.download_button(
                "Descargar Silver CSV",
                data=download_df(silver, "silver.csv"),
                file_name="silver.csv",
                mime="text/csv"
            )
