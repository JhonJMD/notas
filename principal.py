import os
import menus as menu

alumonos = {}
isActive = True
opMenu = 0 
while (isActive):
    os.system("cls")
    try:
        opMenu = menu.menuPrincipal()
    except:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if(opMenu == 4):
            isActive = False
