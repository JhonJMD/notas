import os
import menus as menu
import alumnos as st

alumnos = {}
isActive = True
opMenu = 0 
while (isActive):
    os.system("cls")
    try:
        opMenu = int(menu.menuPrincipal())
    except:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if(opMenu == 1):
            rta = ("S")
            while (rta in ["S","s"]):
                os.system("cls")
                alumnos.update(st.regAlumnos())
                rta = input("Desea registrar otro Alumno? S(si) o N(no)").upper()
        elif (opMenu == 2):
            opNotas = 0
            isActiveGrades = True
            while isActiveGrades:
                try:
                    opNotas = int(menu.menuNotas())
                except:
                    print("Error en el dato de ingreso")
                    os.system("pause")
                else:
                    if(opNotas == 1):
                        pass
                    elif(opNotas == 4):
                        isActiveGrades = False
        elif (opMenu == 3):
            codAlumno = input("Ingrese el codigo a buscar: ")
            st.buscarAlumno(codAlumno,alumnos)
            os.system("pause")
        elif (opMenu == 5):
            isActive = False
