from logic.archivo import cargar_datos
from datetime import datetime
from tabulate import tabulate

def designTwo():
    print("\n=============================================")
    print("                Listar Gastos")
    print("=============================================")
    gastos = cargar_datos()

    if not gastos:
        print("No hay gastos registrados.")
        return

    print("\nSeleccione una opción para filtrar los gastos:")
    print("1. Ver todos los gastos")
    print("2. Filtrar por categoría")
    print("3. Filtrar por rango de fechas")
    print("4. Regresar al menú principal")
    print("=============================================")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
       
        print("\nTodos los gastos:")
        mostrar_gastos(gastos)

    elif opcion == '2':
        
        categoria = input("Ingrese la categoría para filtrar (ej. comida, transporte, entretenimiento, otros): ").strip()
        gastos_filtrados = [g for g in gastos if g['categoria'].lower() == categoria.lower()]
        if gastos_filtrados:
            print(f"\nGastos en la categoría '{categoria}':")
            mostrar_gastos(gastos_filtrados)
        else:
            print(f"No se encontraron gastos en la categoría '{categoria}'.")

    elif opcion == '3':
        
        try:
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ").strip()
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()

            gastos_filtrados = [g for g in gastos if fecha_inicio <= datetime.strptime(g['fecha'], '%Y-%m-%d').date() <= fecha_fin]
            if gastos_filtrados:
                print(f"\nGastos desde {fecha_inicio} hasta {fecha_fin}:")
                mostrar_gastos(gastos_filtrados)
            else:
                print(f"No se encontraron gastos en el rango de fechas especificado.")
        except ValueError:
            print("Fechas inválidas. Por favor, use el formato YYYY-MM-DD.")

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
        if designFive() == 0:
            print("Saliendo del programa...")
            exit()
    else:
        print("Opción no válida.")

def mostrar_gastos(gastos):
    """Muestra los gastos en formato tabular usando tabulate."""
    tabla = [[g['fecha'], g['categoria'], g['monto'], g['descripcion']] for g in gastos]
    print(tabulate(tabla, headers=["Fecha", "Categoría", "Monto", "Descripción"], tablefmt="grid"))
