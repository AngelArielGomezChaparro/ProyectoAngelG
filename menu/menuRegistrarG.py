#menuRegistrarG.py
#Menu opcion 1

import logic.registrarNuevoGasto
import logic.actualizarGastos    
import logic.leerGastos

def designOne():
    print("""
        =============================================
                    Registrar Nuevo Gasto
        =============================================
        """)

    cantidad = input("\tPor favor, ingrese la cantidad del gasto: ")
    categoria = input("\tPor favor, ingrese la categoría del gasto: ")
    descripcion = input("\tPor favor, ingrese la descripción del gasto: ")
    fecha = input("\tPor favor, ingrese la fecha del gasto (YYYY-MM-DD): ")

    logic.registrarNuevoGasto.agregarGasto(cantidad, categoria, descripcion, fecha)

    logic.actualizarGastos.actualizarGastos()

    logic.leerGastos.leerGastos()

    print("""
        =============================================
                    Nuevo Gasto Registrado
        =============================================
        """)

    input("\tPresione Enter para continuar...")


    return 0
    
