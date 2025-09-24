import pandas as pd

def basic_checks(df: pd.DataFrame) -> list[str]:
    """
    Realiza validaciones mínimas sobre DataFrame canónico.
    Retorna lista de errores encontrados.
    - Columnas canónicas presentes.
    - amount numérico y >= 0.
    - date convertible a datetime.
    """
    errors: list[str] = []

    required_cols = {"date", "partner", "amount"}
    missing = required_cols - set(df.columns)
    if missing:
        errors.append(f"Faltan columnas: {', '.join(missing)}")

    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append("amount no es numérico")
        elif (df["amount"] < 0).any():
            errors.append("amount contiene valores negativos")

    if "date" in df.columns:
        try:
            pd.to_datetime(df["date"])
        except Exception:
            errors.append("date no es convertible a datetime")

    return errors
