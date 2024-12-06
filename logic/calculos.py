from datetime import datetime, timedelta


def calcular_total_periodo(gastos, fecha_inicio, fecha_fin):
    return sum(g['monto'] for g in gastos if fecha_inicio <= datetime.strptime(g['fecha'], '%Y-%m-%d').date() <= fecha_fin)


def filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_fin):
    return [g for g in gastos if fecha_inicio <= datetime.strptime(g['fecha'], '%Y-%m-%d').date() <= fecha_fin]
