import pandas as pd
import numpy as np
from pathlib import Path

BASE_PATH = Path().absolute()

RAW_PATH = BASE_PATH / "data" / "raw" / "datos_mortalidad_transito_raw.xlsx"
PROCESSED_PATH = BASE_PATH / "data" / "processed"

DATASET_FINAL = PROCESSED_PATH / "mortalidad_transito_clean.xlsx"
KPI_MUNICIPIOS_PATH = PROCESSED_PATH / "kpi_municipios.xlsx"
KPI_ANUAL_PATH = PROCESSED_PATH / "kpi_anual.xlsx"
KPI_TENDENCIA_PATH = PROCESSED_PATH / "kpi_tendencia.xlsx"
KPI_CONCENTRACION_PATH = PROCESSED_PATH / "kpi_concentracion.xlsx"


def transform_data():

    print("Iniciando transformación...")

    # 1. Cargar datos
    df = pd.read_excel(RAW_PATH)

    print(f"Registros iniciales: {len(df)}")

    # 2. Normalizar columnas
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("ñ", "n")
    )

    print("Columnas disponibles:")
    print(df.columns)

    # 3. Seleccionar columnas clave
    columnas = ["municipio", "anno", "numerador", "denominador"]

    df = df[columnas]

    # 4. Renombrar columnas
    df = df.rename(columns={
        "anno": "anio",
        "numerador": "fallecidos",
        "denominador": "poblacion"
    })

    # 5. Limpieza
    df = df.drop_duplicates()

    df["anio"] = pd.to_numeric(df["anio"], errors="coerce")
    df["fallecidos"] = pd.to_numeric(df["fallecidos"], errors="coerce")
    df["poblacion"] = pd.to_numeric(df["poblacion"], errors="coerce")

    # eliminar nulos críticos
    df = df.dropna(subset=["municipio", "anio", "fallecidos", "poblacion"])

    # eliminar valores inválidos
    df = df[df["poblacion"] > 0]

    print(f"Registros después de limpieza: {len(df)}")

    # 6. Filtro dinámico: últimos 5 años
    anio_max = df["anio"].max()
    anio_min = anio_max - 4

    df = df[df["anio"] >= anio_min]

    print(f"Filtrando datos desde {anio_min} hasta {anio_max}")
    print(f"Registros después del filtro: {len(df)}")

    # 7. KPIs
    # Calcular tasa de mortalidad por cada 100.000 habitantes
    df["tasa_mortalidad"] = (df["fallecidos"] / df["poblacion"]) * 100000

    # eliminar posibles infinitos
    df = df.replace([np.inf, -np.inf], np.nan)

    # KPI 1: Municipios con mayor mortalidad
    kpi_municipios = (
        df.groupby("municipio")[["fallecidos", "tasa_mortalidad"]]
        .sum()
        .reset_index()
        .sort_values(by="fallecidos", ascending=False)
    )

    # KPI 2: Evolución anual
    kpi_anual = (
        df.groupby("anio")[["fallecidos", "tasa_mortalidad"]]
        .sum()
        .reset_index()
    )

    kpi_anual["variacion_%"] = kpi_anual["fallecidos"].pct_change() * 100
    kpi_anual["variacion_%"] = kpi_anual["variacion_%"].replace([np.inf, -np.inf], np.nan)
    kpi_anual["variacion_%"] = kpi_anual["variacion_%"].round(2)

    # KPI 3: Tendencia por municipio
    kpi_tendencia = (
        df.groupby(["municipio", "anio"])[["fallecidos", "tasa_mortalidad"]]
        .sum()
        .reset_index()
    )

    kpi_tendencia["variacion"] = (
        kpi_tendencia
        .sort_values(["municipio", "anio"])
        .groupby("municipio")["fallecidos"]
        .pct_change()
    )

    kpi_tendencia["variacion"] = kpi_tendencia["variacion"].replace([np.inf, -np.inf], np.nan)
    kpi_tendencia["variacion"] = kpi_tendencia["variacion"].round(4)

    # KPI 4: Concentración histórica
    total = df["fallecidos"].sum()

    kpi_concentracion = (
        df.groupby("municipio")["fallecidos"]
        .sum()
        .reset_index()
    )

    kpi_concentracion["porcentaje"] = (
        kpi_concentracion["fallecidos"] / total * 100
    )

    # 8. Guardar resultados
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    # dataset limpio
    df.to_excel(DATASET_FINAL, index=False)

    # KPIs
    kpi_municipios.to_excel(KPI_MUNICIPIOS_PATH, index=False)
    kpi_anual.to_excel(KPI_ANUAL_PATH, index=False)
    kpi_tendencia.to_excel(KPI_TENDENCIA_PATH, index=False)
    kpi_concentracion.to_excel(KPI_CONCENTRACION_PATH, index=False)

    print("\nArchivos generados en data/processed:")
    print("- mortalidad_transito_clean.xlsx")
    print("- kpi_municipios.xlsx")
    print("- kpi_anual.xlsx")
    print("- kpi_tendencia.xlsx")
    print("- kpi_concentracion.xlsx")

    return df