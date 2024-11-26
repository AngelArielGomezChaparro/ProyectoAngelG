#Main
from menu.mainMenu import designMainMenu 
from menu.menuRegistrarG import designOne
from menu.menuListarG import designTwo
from menu.menuCalcularG import designThree
from menu.menuGenerarR import designFour
from menu.menuSalir import designFive

while True:
    try:
        
        option = designMainMenu()

        if option == 1:
            designOne()
        elif option == 2:
            designTwo()
        elif option == 3:
            designThree()
        elif option == 4:
            designFour()
        elif option == 5:
         if designFive() == 0:
                print("Saliendo del programa...")
                break
        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")
    except ValueError:
        print("Por favor, ingrese un número.")
