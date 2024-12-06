from datetime import datetime

def filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_fin):
    
    fecha_inicio = fecha_inicio.date()
    fecha_fin = fecha_fin.date()
    return [g for g in gastos if fecha_inicio <= datetime.strptime(g['fecha'], '%Y-%m-%d').date() <= fecha_fin]


def calcular_total_periodo(gastos, fecha_inicio, fecha_fin):
    # Asegurar que los límites del rango sean de tipo date
    if isinstance(fecha_inicio, datetime):
        fecha_inicio = fecha_inicio.date()
    if isinstance(fecha_fin, datetime):
        fecha_fin = fecha_fin.date()
        
    return sum(
        g['monto'] 
        for g in gastos 
        if fecha_inicio <= datetime.strptime(g['fecha'], '%Y-%m-%d').date() <= fecha_fin
    )
