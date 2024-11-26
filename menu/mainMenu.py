#mainMenu.py
#Menu principal
import os

def designMainMenu():
    print("""
    =============================================
             Simulador de Gasto Diario
    =============================================
              Seleccione una opción:
    Seleccione una opción:

        1. Registrar nuevo gasto
        2. Listar gastos
        3. Calcular total de gastos
        4. Generar reporte de gastos
        5. Salir
    =============================================
        """)
        
        #try:
   
    opcion1 = int(input("Por favor, elige una opción (1-5): "))
    return opcion1
   
        #except ValueError:
            #print("Por favor, ingrese un número válido.")