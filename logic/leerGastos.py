import json
import os   



archivoGastos = os.path.join(os.path.dirname(__file__), "../dataBase/RegistrarNuevoG.json")

def leerGastos():
    """Carga los gastos desde el archivo JSON. Si el archivo no existe, retorna una lista vacía."""
    if not os.path.exists(archivoGastos):
        return []
    with open(archivoGastos, "r") as archivo:
        return json.load(archivo)
 