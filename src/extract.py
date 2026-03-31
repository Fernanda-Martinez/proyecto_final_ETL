import requests
import pandas as pd
import openpyxl
from pathlib import Path

# URL de la API para obtener los datos de mortalidad por tránsito en Colombia
API_URL = "https://www.datos.gov.co/resource/2bk8-65js.json"

# Ruta para guardar los datos extraídos en formato excel
BASE_PATH = Path().absolute()
RAW_PATH = BASE_PATH / "data" / "raw" / "datos_mortalidad_transito_raw.xlsx"


def extract_data():

    print("Iniciando la extracción de datos...")

    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception("Error al consumir la API")
    
    print("Datos extraídos correctamente")

    data = response.json()

    df = pd.DataFrame(data)

    print(f"Total de registros extraídos: {len(df)}")

    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_excel(RAW_PATH, index=False)

    print("Datos guardados en la carpeta data/raw")

    return df