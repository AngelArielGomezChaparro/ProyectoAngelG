from logic.gastos import registrar_gasto

def designOne():
    print("\n=============================================")
    print("            Registrar Nuevo Gasto")
    print("=============================================")
    try:
        monto = float(input("Ingrese el monto del gasto: "))
        categoria = input("Ingrese la categoría (ej. comida, transporte, entretenimiento, otros): ")
        descripcion = input("Ingrese una descripción (opcional): ")
        registrar_gasto(monto, categoria, descripcion)
        print("\nGasto registrado con éxito.\n")
        
        
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
            print("Opción no válida. Volviendo al menú principal.")
            return  

    except ValueError:
        print("Monto inválido. Por favor, ingrese un número.")