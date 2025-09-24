import pandas as pd

def normalize_columns(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """
    Normaliza columnas de un DataFrame a esquema canónico:
    - Renombra según mapping (origen -> {date, partner, amount}).
    - Convierte fechas a datetime (ISO).
    - Limpia columna partner (espacios).
    - Convierte amount a float en EUR (quita €, puntos, comas).
    """
    # Renombrar columnas al esquema canónico
    df = df.rename(columns=mapping)

    # Normalizar fecha
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date

    # Normalizar partner
    if "partner" in df.columns:
        df["partner"] = df["partner"].astype(str).str.strip()

    # Normalizar amount
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace("€", "", regex=False)
            .str.replace(".", "", regex=False)   # eliminar separador de miles europeo
            .str.replace(",", ".", regex=False)  # convertir coma decimal a punto
        )
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df[["date", "partner", "amount"]]


def to_silver(bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega datos de Bronze a Silver:
    - Agrupa por partner y mes.
    - Columna 'month' como primer día del mes (Timestamp).
    - Suma los amounts.
    """
    bronze = bronze.copy()
    bronze["month"] = pd.to_datetime(bronze["date"]).dt.to_period("M")
    silver = (
        bronze.groupby(["partner", "month"], as_index=False)
        .agg({"amount": "sum"})
    )
    # Convertir Period a Timestamp (primer día de mes)
    silver["month"] = silver["month"].dt.to_timestamp()
    return silver
