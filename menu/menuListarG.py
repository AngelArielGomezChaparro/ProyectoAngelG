#Menu opcion 2
#menuListarG.py
def designTwo():
    print("""
        =============================================
                        Listar Gastos
        =============================================
        Seleccione una opción para filtrar los gastos:

        1. Ver todos los gastos
        2. Filtrar por categoría
        3. Filtrar por rango de fechas
        4. Regresar al menú principal
        =============================================
        """)
    Option1 = int(input("        Por favor, elige una opción (1-4): "))
    return Option1