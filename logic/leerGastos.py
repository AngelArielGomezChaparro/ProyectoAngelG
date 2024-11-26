import json
import os   
def leerGastos(archivo):  
    """Lee y devuelve los datos del archivo JSON si existe, o una lista vacía si no."""  
    if os.path.exists(archivo):  
        with open(archivo, "r") as file:  
            return json.load(file)  
    return []   