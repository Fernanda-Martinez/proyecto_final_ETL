from sqlalchemy import create_engine, text
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

BASE_PATH = Path().absolute()
PROCESSED_PATH = BASE_PATH / "data" / "processed"

DATASET = PROCESSED_PATH / "mortalidad_transito_clean.xlsx"
KPI_MUNICIPIOS = PROCESSED_PATH / "kpi_municipios.xlsx"
KPI_ANUAL = PROCESSED_PATH / "kpi_anual.xlsx"
KPI_TENDENCIA = PROCESSED_PATH / "kpi_tendencia.xlsx"
KPI_CONCENTRACION = PROCESSED_PATH / "kpi_concentracion.xlsx"


def load_data():

    print("Iniciando carga...")

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # Crear base de datos si no existe
    engine_server = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/"
    )

    with engine_server.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Base de datos '{db_name}' verificada/creada")

    # Conectar a la base de datos 
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    )

    print("Conectado a la base de datos")

    # Cargar dataset principal
    df = pd.read_excel(DATASET)

    df.to_sql("mortalidad_transito", engine, if_exists="replace", index=False)

    print("Tabla mortalidad_transito cargada")
    # Cargar KPIs
    pd.read_excel(KPI_MUNICIPIOS).to_sql(
        "kpi_municipios", engine, if_exists="replace", index=False
    )

    pd.read_excel(KPI_ANUAL).to_sql(
        "kpi_anual", engine, if_exists="replace", index=False
    )

    pd.read_excel(KPI_TENDENCIA).to_sql(
        "kpi_tendencia", engine, if_exists="replace", index=False
    )

    pd.read_excel(KPI_CONCENTRACION).to_sql(
        "kpi_concentracion", engine, if_exists="replace", index=False
    )

    print("KPIs cargados correctamente")

    print("\nCarga finalizada")
