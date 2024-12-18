from logic.calculos import calcular_total_periodo
from logic.archivo import cargar_datos
from datetime import datetime, timedelta

def designThree():
    print("\n=============================================")
    print("          Calcular Total de Gastos")
    print("=============================================")
    gastos = cargar_datos()
    fecha_actual = datetime.now().date()
    
    print("Seleccione el periodo de cálculo:")
    print("1. Calcular total diario")
    print("2. Calcular total semanal")
    print("3. Calcular total mensual")
    print("4. Regresar al menú principal")
    
    opcion = input("Seleccione una opción: ")

    total = None  
    if opcion == '1':
        total = calcular_total_periodo(gastos, fecha_actual, fecha_actual)
        print(f"\nTotal de gastos de hoy: ${total:.2f}")
    elif opcion == '2':
        fecha_inicio = fecha_actual - timedelta(days=7)
        total = calcular_total_periodo(gastos, fecha_inicio, fecha_actual)
        print(f"\nTotal de gastos de la última semana: ${total:.2f}")
    elif opcion == '3':
        fecha_inicio = fecha_actual.replace(day=1)
        total = calcular_total_periodo(gastos, fecha_inicio, fecha_actual)
        print(f"\nTotal de gastos del mes: ${total:.2f}")
    elif opcion == '4':
        return
    else:
        print("\nOpción no válida.")
        return

    
    if total is not None:
        print("\n=============================================")
        print("Seleccione una opción:")
        print("1. Volver al menú principal")
        print("2. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            return
        elif opcion == '2':
            from menu.menuSalir import designFive
            if designFive() == 0:
                print("Saliendo del programa...")
                exit()
        else:
            print("Opción no válida.")
