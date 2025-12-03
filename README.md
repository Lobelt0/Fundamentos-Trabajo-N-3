# Proyecto Inmobiliario con ML + MySQL

## Estructura
- data/: CSV principal con abreviaciones
- db/: script SQL para comunas
- scripts/: inserción, join, carga de CSV
- models/: modelo Random Forest
- main/: Código principal con todas las funciones en el mismo archivo.

## Flujo
1. dataset_con_codigos.csv: ML
2. dataset_con_nombres.csv: CSV Generado para modificar la Columna "Nombre".
3. insertar_comunas.py: llena la tabla comuna
4. unir_comunas.py: devuelve nombre real de comuna
5. random_forest_comunas.py: entrena el modelo


# EN EL CMD:

cd "Dirección de la carpeta/Ruta de acceso"

# Entorno Virtual

python -m venv venv

#   Windows

venv\Scripts\activate

#   Instalar dependencias

pip install -r requerimientos.txt