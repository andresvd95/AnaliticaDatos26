# AE2: manejo de archivos CSV, JSON y TXT

Tres clases independientes, coordinadas desde un notebook de Jupyter:

| Archivo | Clase | Función |
|---|---|---|
| `manejador_csv.py` | `ManejadorCSV` | Importa con `csv.reader`, modifica y guarda con `csv.writer` |
| `manejador_json.py` | `ManejadorJSON` | Importa con `json.load`, modifica y guarda con `json.dump` |
| `generador_resumen_txt.py` | `GeneradorResumenTXT` | Genera `resultados/resumen.txt` con los resultados reales |

## Datos de origen (Hugging Face, dataset `BIT/titanic-dataset`)

- CSV: https://huggingface.co/datasets/BIT/titanic-dataset/resolve/main/titanic.csv
- JSON (primeras 100 filas, split `train`): https://datasets-server.huggingface.co/rows?dataset=BIT%2Ftitanic-dataset&config=default&split=train&offset=0&length=100

El dataset publica solo un CSV; el JSON es la respuesta del servicio de filas de Hugging Face para el mismo dataset. Los originales se conservan sin cambios en `datos/originales/`.

## Modificaciones (en cada formato)

Actualizar `age` del primer registro (22.0 → 23.0), agregar un registro nuevo y eliminar el segundo registro.

## Estructura

```text
AE2/
  manejador_csv.py  manejador_json.py  generador_resumen_txt.py
  AE2_manejo_archivos.ipynb   (ejecutado, con resultados)
  datos/originales/   titanic.csv, titanic_filas.json
  datos/modificados/  titanic_modificado.csv, titanic_filas_modificado.json
  resultados/resumen.txt
```

## Ejecución

```bash
cd AE2
python -m pip install notebook
jupyter nbconvert --to notebook --execute --inplace AE2_manejo_archivos.ipynb
```

Solo usa la biblioteca estándar de Python (`csv`, `json`, `datetime`) y rutas relativas, por lo que el notebook debe ejecutarse desde la carpeta `AE2`.
