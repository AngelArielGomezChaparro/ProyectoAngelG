from logic.archivo import cargar_datos
from logic.calculos import filtrar_gastos_por_fecha
from datetime import datetime, timedelta
from tabulate import tabulate

def designFour():
    print("\n=============================================")
    print("           Generar Reporte de Gastos")
    print("=============================================")
    gastos = cargar_datos()
    fecha_actual = datetime.now()

    print("Seleccione el tipo de reporte:")
    print("1. Reporte diario")
    print("2. Reporte semanal")
    print("3. Reporte mensual")
    print("4. Regresar al menú principal")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        reporte = filtrar_gastos_por_fecha(gastos, fecha_actual, fecha_actual)
        print("\nReporte de gastos de hoy:")
    elif opcion == '2':
        fecha_inicio = fecha_actual - timedelta(days=7)
        reporte = filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_actual)
        print("\nReporte de gastos de la última semana:")
    elif opcion == '3':
        fecha_inicio = fecha_actual.replace(day=1)
        reporte = filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_actual)
        print("\nReporte de gastos del mes:")
    elif opcion == '4':
        return
    else:
        print("Opción no válida.")
        return
    
    
    if reporte:
        tabla = [[g['fecha'], g['categoria'], f"${g['monto']:.2f}", g['descripcion']] for g in reporte]
        print(tabulate(tabla, headers=["Fecha", "Categoría", "Monto", "Descripción"], tablefmt="grid"))
    else:
        print("No hay gastos registrados en este periodo.")
    
    
    print("\n=============================================")
    print("Seleccione una opción:")
    print("1. Volver al menú principal")
    print("2. Salir")
    opcion = input("Ingrese su opción: ")
    if opcion == '1':
        return
    elif opcion == '2':
        from menu.menuSalir import designFive
        designFive()
    else:
        print("Opción no válida.")
