import json
import os
from datetime import datetime

archivoGastos = os.path.join(os.path.dirname(__file__), "../dataBase/RegistrarNuevoG.json")

def leerGastos():
    """Carga los gastos desde el archivo JSON."""
    if not os.path.exists(archivoGastos):
        return []
    with open(archivoGastos, "r") as archivo:
        return json.load(archivo)

def convertirCantidadNumero(gastos):
    """Convierte la cantidad de cada gasto a número si es necesario."""
    for gasto in gastos:
        if isinstance(gasto.get("cantidad"), str):
            try:
                gasto["cantidad"] = float(gasto["cantidad"])
            except ValueError:
                print(f" No se pudo convertir la cantidad: {gasto['cantidad']}")

def escribirGastos(gastos):
    """Guarda los gastos en el archivo JSON, creando directorios si es necesario."""
    os.makedirs(os.path.dirname(archivoGastos), existOk=True)
    with open(archivoGastos, "w") as archivo:
        json.dump(gastos, archivo, indent=4)

def agregarGasto(cantidad, categoria, descripcion="", fecha=None):
    """Agrega un nuevo gasto al archivo JSON."""
    fechaGasto = fecha or datetime.now().strftime("%Y-%m-%d")
    
   
    if fecha:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            return "\t Error: Formato de fecha inválido. Usa 'YYYY-MM-DD'."
    
    
    nuevoGasto = {
        "cantidad": cantidad,
        "categoria": categoria,
        "descripcion": descripcion if descripcion else "Sin descripción",
        "fecha": fechaGasto
    }
    

    gastos = leerGastos()
    convertirCantidadNumero(gastos)
    gastos.append(nuevoGasto)
    escribirGastos(gastos)
    
    return "\t Gasto registrado con éxito."
