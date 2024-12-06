def designMainMenu():
    print("\n=============================================")
    print("         Simulador de Gasto Diario")
    print("=============================================")
    print("Seleccione una opción:")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")
    try:
        opcion = int(input("Ingrese su opción: "))
        return opcion
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 0  
