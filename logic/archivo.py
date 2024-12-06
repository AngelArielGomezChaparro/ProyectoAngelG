import json

FILE_PATH = 'database/gastos.json'


def cargar_datos():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  


def guardar_datos(gastos):
    try:
        with open(FILE_PATH, 'w') as file:
            json.dump(gastos, file, indent=4)
    except IOError:
        print("Error al guardar los datos en el archivo.")
        

def actualizar_dato(indice, nuevo_gasto):
    gastos = cargar_datos()
    if 0 <= indice < len(gastos):
        gastos[indice] = nuevo_gasto
        guardar_datos(gastos)
        return True
    return False
