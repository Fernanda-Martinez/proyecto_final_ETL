# ETL Pipeline – Mortalidad por Accidentes de Tránsito en Caldas

Este repositorio contiene el desarrollo de un pipeline ETL (Extract, Transform, Load) para la integración, limpieza y análisis de datos de mortalidad por accidentes de tránsito en los municipios del departamento de Caldas, Colombia.

El proyecto utiliza datos abiertos provenientes del portal Datos Abiertos Colombia específicamente el dataset oficial basado en registros del DANE sobre mortalidad asociada a siniestros viales.

El objetivo del proyecto es transformar datos abiertos en formato crudo en un activo de información estructurado, permitiendo realizar análisis comparativos entre municipios, identificar tendencias temporales y apoyar procesos de toma de decisiones en el ámbito de la seguridad vial y la salud pública territorial.

El pipeline desarrollado automatiza las siguientes etapas:

* Extracción: Obtención de datos desde fuentes abiertas mediante Python.
* Transformación: Limpieza, validación y estructuración de los datos utilizando Pandas.
* Carga: Almacenamiento de los datos procesados en una base de datos relacional.
* Visualización: Generación de dashboards para el análisis territorial de la mortalidad por accidentes de tránsito.

Este proyecto se desarrolla, aplicando principios de arquitectura de datos y buenas prácticas de ingeniería de datos.

