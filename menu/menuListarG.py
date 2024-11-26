#Menu opcion 2
#menuListarG.py
import json
import os
from datetime import datetime
from tabulate import tabulate


rutaArchivoGastos = os.path.join(os.path.dirname(__file__), "../dataBase/registrarNuevoG.json")

def cargarastos():
    """
    Carga los gastos desde un archivo JSON. Si el archivo no existe, retorna una lista vacía.
    """
    try:
        with open(rutaArchivoGastos, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(" No se encontró el archivo de gastos.")
        return []
    except json.JSONDecodeError:
        print(" Error al leer el archivo de gastos. Podría estar corrupto.")
        return []

def filtrarGastosPorCategoria(gastos, categoria):
    """
    Filtra los gastos de una lista según una categoría específica (sin importar mayúsculas o minúsculas).
    """
    return list(filter(lambda gasto: gasto.get("categoria", "").lower() == categoria.lower(), gastos))

def filtrarGastosPorFecha(gastos, inicio, fin):
    """
    Filtra los gastos dentro de un rango de fechas proporcionado.
    """
    try:
        fechaInicio = datetime.strptime(inicio, "%Y-%m-%d")
        fechaFin = datetime.strptime(fin, "%Y-%m-%d")
        return [
            gasto for gasto in gastos
            if fechaInicio <= datetime.strptime(gasto.get("fecha", "1900-01-01"), "%Y-%m-%d") <= fechaFin
        ]
    except ValueError:
        print(" Las fechas deben tener el formato YYYY-MM-DD.")
        return []

def generarTablaGastos(gastos):
    """
    Genera una tabla con los datos de los gastos en formato de texto legible.
    """
    if not gastos:
        return " No hay gastos para mostrar."

    filas = []
    for gasto in gastos:
        filas.append([
            gasto.get("fecha", "Sin fecha"),
            gasto.get("categoria", "Sin categoría"),
            gasto.get("cantidad", "Sin cantidad"),
            gasto.get("descripcion", "Sin descripción")
        ])
    
    return tabulate(filas, headers=["Fecha", "Categoría", "Cantidad", "Descripción"], tablefmt="grid")

