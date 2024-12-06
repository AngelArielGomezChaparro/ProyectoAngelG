def designFive():
    print("\n=============================================")
    print("               Salir")
    print("=============================================")
    confirmacion = input("¿Estás seguro de que quieres salir? (S para salir, C para cancelar): ").upper()
    if confirmacion == 'S':
        print("Saliendo del programa...")
        return 0  
    elif confirmacion == 'C':
        print("Operación cancelada.")
        return 1  
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        return 1
