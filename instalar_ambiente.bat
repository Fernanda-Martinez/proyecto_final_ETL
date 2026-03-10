echo Creando entorno virtual...

python -m venv venv

echo Activando entorno...

call venv\Scripts\activate

echo Instalando librerias...

pip install --upgrade pip
pip install -r requirements.txt

echo Entorno listo
pause