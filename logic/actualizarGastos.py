import json
import os


archivoGastos = "registrarNuevoG.json" 



def leerGastos(archivo):
    """Lee y devuelve los datos del archivo JSON si existe, o una lista vacía si no."""
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            return json.load(file)
    return []



def guardarGastos(archivo, datos):
    """Guarda los datos en el archivo JSON."""
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)




def actualizarGastos():
    """Agrega la clave 'fecha' a los gastos si no existe."""
    gastos = leerGastos(archivoGastos)  
    if not gastos:
        print(" No hay datos para actualizar o el archivo no existe.")
        return
    
    
    for gasto in gastos:
        if "fecha" not in gasto: 
            gasto["fecha"] = "Sin fecha"
    
    guardarGastos(archivoGastos, gastos)  
    print(" Archivo actualizado correctamente.")


actualizarGastos()

