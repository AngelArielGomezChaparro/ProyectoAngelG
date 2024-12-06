from datetime import datetime
from logic.archivo import cargar_datos, guardar_datos


def registrar_gasto(monto, categoria, descripcion=""):
    fecha = datetime.now().date().strftime('%Y-%m-%d')
    gasto = {
        'fecha': fecha,
        'monto': monto,
        'categoria': categoria,
        'descripcion': descripcion
    }
    gastos = cargar_datos()
    gastos.append(gasto)
    guardar_datos(gastos)
    print("\nGasto registrado con éxito.\n")