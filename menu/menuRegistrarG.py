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

    cantidad = input("Por favor, ingrese la cantidad del gasto: ")
    categoria = input("Por favor, ingrese la categoría del gasto: ")
    descripcion = input("Por favor, ingrese la descripción del gasto: ")
    fecha = input("Por favor, ingrese la fecha del gasto (YYYY-MM-DD): ")

    logic.registrarNuevoGasto.agregarGasto(cantidad, categoria, descripcion, fecha)

    logic.actualizarGastos.actualizarGastos()

    logic.leerGastos.leerGastos()

    print("""
        =============================================
                    Nuevo Gasto Registrado
        =============================================
        """)

    input("Presione Enter para continuar...")


    return 0
    
