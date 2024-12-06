from logic.archivo import cargar_datos
from tabulate import tabulate

def designTwo():
    print("\n=============================================")
    print("                Listar Gastos")
    print("=============================================")
    gastos = cargar_datos()
    
    if not gastos:
        print("No hay gastos registrados.")
        return

    
    tabla = [[gasto['fecha'], gasto['categoria'], f"${gasto['monto']:.2f}", gasto['descripcion']] for gasto in gastos]
    print(tabulate(tabla, headers=["Fecha", "Categoría", "Monto", "Descripción"], tablefmt="grid"))
    
    
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
