#menuRegistrarG.py
#Menu opcion 1

def designOne():
    print("""
        =============================================
                    Registrar Nuevo Gasto
        =============================================
        Ingrese la información del gasto:    
        """)
    
        
   
    monto = input("        - Monto de gasto: ")
    categoria = input("        - Categoría (ej. comida, transporte, entretenimiento, otros): ")
    descripcion = input("        - Descripción (opcional): ")
    print (" ")
    guardar_o_cancelar = input("        Ingrese 'S' para guardar o 'C' para cancelar: ")
    print("""        
        ===============================================
          """)