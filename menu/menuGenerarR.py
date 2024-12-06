from logic.archivo import cargar_datos
from logic.calculos import filtrar_gastos_por_fecha
from datetime import datetime, timedelta

def designFour():
    print("\n=============================================")
    print("           Generar Reporte de Gastos")
    print("=============================================")
    gastos = cargar_datos()
    fecha_actual = datetime.now().date()  

    print("Seleccione el tipo de reporte:")
    print("1. Reporte diario")
    print("2. Reporte semanal")
    print("3. Reporte mensual")
    print("4. Regresar al menú principal")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        reporte = filtrar_gastos_por_fecha(gastos, fecha_actual, fecha_actual)
        print("\nReporte de gastos de hoy:")
        for gasto in reporte:
            print(f"{gasto['fecha']} - {gasto['categoria']} - ${gasto['monto']} - {gasto['descripcion']}")
    elif opcion == '2':
        fecha_inicio = fecha_actual - timedelta(days=7)
        reporte = filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_actual)
        print("\nReporte de gastos de la última semana:")
        for gasto in reporte:
            print(f"{gasto['fecha']} - {gasto['categoria']} - ${gasto['monto']} - {gasto['descripcion']}")
    elif opcion == '3':
        fecha_inicio = fecha_actual.replace(day=1)
        reporte = filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_actual)
        print("\nReporte de gastos del mes:")
        for gasto in reporte:
            print(f"{gasto['fecha']} - {gasto['categoria']} - ${gasto['monto']} - {gasto['descripcion']}")
    elif opcion == '4':
        return
    else:
        print("Opción no válida.")
    
    
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