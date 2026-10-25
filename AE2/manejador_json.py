"""Clase para importar, modificar y guardar archivos JSON."""
import json


class ManejadorJSON:
    def __init__(self):
        self.ruta_origen = None
        self.datos = None
        self.registros_importados = 0
        self.modificaciones = []
        self.ruta_guardado = None

    def importar(self, ruta):
        """Lee el JSON con json.load. Los registros estan en la clave 'rows'."""
        with open(ruta, encoding="utf-8") as archivo:
            self.datos = json.load(archivo)
        self.ruta_origen = ruta
        self.registros_importados = len(self.datos["rows"])
        return self.datos

    def actualizar_valor(self, indice, campo, nuevo_valor):
        """Cambia un campo de un registro y devuelve (antes, despues)."""
        registro = self.datos["rows"][indice]["row"]
        antes = registro[campo]
        registro[campo] = nuevo_valor
        self.modificaciones.append(
            f"actualizar_valor: registro {indice}, campo '{campo}': {antes} -> {nuevo_valor}"
        )
        return antes, nuevo_valor

    def agregar_registro(self, registro):
        """Agrega un registro nuevo al final de 'rows'."""
        nuevo = {"row_idx": len(self.datos["rows"]), "row": registro, "truncated_cells": []}
        self.datos["rows"].append(nuevo)
        self.modificaciones.append(f"agregar_registro: nuevo registro row_idx={nuevo['row_idx']}")
        return nuevo

    def eliminar_registro(self, indice):
        """Elimina un registro por posicion y lo devuelve."""
        eliminado = self.datos["rows"].pop(indice)
        self.modificaciones.append(
            f"eliminar_registro: registro {indice} eliminado (row_idx={eliminado['row_idx']})"
        )
        return eliminado

    def guardar(self, ruta):
        """Escribe un JSON nuevo con json.dump."""
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=2)
        self.ruta_guardado = ruta
        return ruta

    def informe(self):
        """Resultados reales de la ejecucion para el generador de resumen."""
        return {
            "clase": "ManejadorJSON",
            "metodos": ["importar", "actualizar_valor", "agregar_registro",
                        "eliminar_registro", "guardar"],
            "archivo_importado": self.ruta_origen,
            "registros_importados": self.registros_importados,
            "modificaciones": list(self.modificaciones),
            "registros_finales": len(self.datos["rows"]),
            "archivo_guardado": self.ruta_guardado,
        }
