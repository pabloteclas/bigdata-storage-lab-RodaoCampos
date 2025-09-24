import pandas as pd
from datetime import datetime, timezone

def tag_lineage(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Añade metadatos de linaje:
    - source_file: nombre del archivo origen.
    - ingested_at: timestamp UTC ISO8601.
    """
    df = df.copy()
    df["source_file"] = source_name
    df["ingested_at"] = datetime.now(timezone.utc).isoformat()
    return df


def concat_bronze(frames: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatena múltiples DataFrames de Bronze asegurando esquema.
    Columnas finales: date, partner, amount, source_file, ingested_at
    """
    bronze = pd.concat(frames, ignore_index=True)
    return bronze[["date", "partner", "amount", "source_file", "ingested_at"]]
