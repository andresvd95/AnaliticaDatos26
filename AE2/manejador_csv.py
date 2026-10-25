"""Clase para importar, modificar y guardar archivos CSV."""
import csv


class ManejadorCSV:
    def __init__(self):
        self.ruta_origen = None
        self.encabezados = []
        self.filas = []
        self.registros_importados = 0
        self.modificaciones = []
        self.ruta_guardado = None

    def importar(self, ruta):
        """Lee el CSV con csv.reader; la primera fila son los encabezados."""
        with open(ruta, newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.filas = [fila for fila in lector]
        self.ruta_origen = ruta
        self.registros_importados = len(self.filas)
        return self.filas

    def actualizar_valor(self, indice_fila, columna, nuevo_valor):
        """Cambia un valor y devuelve (antes, despues)."""
        indice_columna = self.encabezados.index(columna)
        antes = self.filas[indice_fila][indice_columna]
        self.filas[indice_fila][indice_columna] = str(nuevo_valor)
        self.modificaciones.append(
            f"actualizar_valor: fila {indice_fila}, columna '{columna}': {antes} -> {nuevo_valor}"
        )
        return antes, str(nuevo_valor)

    def agregar_registro(self, registro):
        """Agrega una fila nueva (diccionario columna -> valor) al final."""
        fila = [str(registro.get(columna, "")) for columna in self.encabezados]
        self.filas.append(fila)
        self.modificaciones.append(f"agregar_registro: nueva fila {fila}")
        return fila

    def eliminar_registro(self, indice_fila):
        """Elimina una fila y la devuelve."""
        fila = self.filas.pop(indice_fila)
        self.modificaciones.append(f"eliminar_registro: fila {indice_fila} eliminada {fila}")
        return fila

    def guardar(self, ruta):
        """Escribe un CSV nuevo con csv.writer, incluyendo encabezados."""
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.filas)
        self.ruta_guardado = ruta
        return ruta

    def informe(self):
        """Resultados reales de la ejecucion para el generador de resumen."""
        return {
            "clase": "ManejadorCSV",
            "metodos": ["importar", "actualizar_valor", "agregar_registro",
                        "eliminar_registro", "guardar"],
            "archivo_importado": self.ruta_origen,
            "registros_importados": self.registros_importados,
            "modificaciones": list(self.modificaciones),
            "registros_finales": len(self.filas),
            "archivo_guardado": self.ruta_guardado,
        }
