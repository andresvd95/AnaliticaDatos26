"""Clase que genera resumen.txt con los resultados de ManejadorCSV y ManejadorJSON."""
from datetime import datetime


class GeneradorResumenTXT:
    def __init__(self, url_csv, url_json):
        self.url_csv = url_csv
        self.url_json = url_json
        self.ruta_resumen = None

    def _seccion(self, titulo, url, informe):
        lineas = [
            f"== {titulo} ==",
            f"URL de origen: {url}",
            f"Archivo importado: {informe['archivo_importado']}",
            f"Clase usada: {informe['clase']}",
            f"Metodos usados: {', '.join(informe['metodos'])}",
            f"Registros importados: {informe['registros_importados']}",
            "Modificaciones realizadas:",
        ]
        lineas += [f"  - {m}" for m in informe["modificaciones"]]
        lineas += [
            f"Registros finales: {informe['registros_finales']}",
            f"Archivo nuevo guardado: {informe['archivo_guardado']}",
            "",
        ]
        return lineas

    def generar(self, ruta, informe_csv, informe_json):
        """Escribe el resumen en 'ruta' y devuelve su contenido."""
        total = informe_csv["registros_importados"] + informe_json["registros_importados"]
        lineas = [
            "RESUMEN AE2 - MANEJO DE ARCHIVOS CSV, JSON Y TXT",
            f"Generado: {datetime.now():%Y-%m-%d %H:%M:%S}",
            "Clase generadora: GeneradorResumenTXT (metodo generar)",
            "",
        ]
        lineas += self._seccion("CSV", self.url_csv, informe_csv)
        lineas += self._seccion("JSON", self.url_json, informe_json)
        lineas.append(f"Total de registros importados (CSV + JSON): {total}")
        contenido = "\n".join(lineas) + "\n"
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        self.ruta_resumen = ruta
        return contenido
