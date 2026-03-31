from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    """
    Función principal del programa que ejecuta el proceso de extracción de datos.
    """
    extract_data()
    transform_data()
    load_data()

if __name__ == "__main__":
    main()