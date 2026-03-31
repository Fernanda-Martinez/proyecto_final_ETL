# Proyecto ETL - Mortalidad por Accidentes de Tránsito en Caldas

## Descripción

Este proyecto implementa un proceso ETL (Extract, Transform, Load) para el análisis de la mortalidad por accidentes de tránsito en el departamento de Caldas, Colombia, utilizando datos abiertos del DANE.

El pipeline permite transformar datos crudos en información estructurada y generar indicadores clave para la toma de decisiones en el ámbito de la seguridad vial.

## Objetivo

Convertir datos abiertos en un activo de información mediante:

- Limpieza y transformación de datos
- Generación de KPIs
- Almacenamiento en base de datos
- Preparación para visualización

## Arquitectura del Proyecto

PROYECTO_FINAL_ETL/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── src/

│   ├── extract.py

│   ├── transform.py

│   ├── load.py

│   └── main.py

│

├── requirements.txt

├── .env

├── .gitignore

├── README.md


## Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- SQLAlchemy
- MySQL

## Proceso ETL

### 1. Extract

Obtención de datos desde API pública de datos abiertos:

- Fuente: datos.gov.co
- Formato: JSON

### 2. Transform

- Limpieza de datos
- Normalización de columnas
- Filtrado de los últimos 5 años
- Cálculo de tasa de mortalidad (por cada 100,000 habitantes)
- Generación de KPIs:
  - Ranking de municipios
  - Evolución anual
  - Tendencias
  - Variación porcentual
  - Concentración de casos

### 3. Load

- Creación automática de la base de datos
- Carga de tablas en MySQL:
  - mortalidad_transito
  - kpi_municipios
  - kpi_anual
  - kpi_tendencia
  - kpi_concentracion

## Instalación

1. Clonar repositorio
2. Ejecutar el archivo .bat
3. Configurar el archivo .env
