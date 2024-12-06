from logic.archivo import cargar_datos

def designTwo():
    print("\n=============================================")
    print("                Listar Gastos")
    print("=============================================")
    gastos = cargar_datos()
    
    if not gastos:
        print("No hay gastos registrados.")
        return
    
    for gasto in gastos:
        print(f"{gasto['fecha']} - {gasto['categoria']} - ${gasto['monto']} - {gasto['descripcion']}")
    
    
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
