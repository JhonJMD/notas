import os
import menus as menu
import alumnos as st
import notas as nota

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
            while (rta in "S"):
                os.system("cls")
                alumnos.update(st.regAlumnos())
                rta = input("Desea registrar otro Alumno? S(si) o N(no)").upper()
        elif (opMenu == 2):
            # opNotas = 0
            # alumno = st.buscarAlumno(alumnos)
            # isActiveGrades = True
            # while isActiveGrades:
            #     try:
            #         opNotas = int(menu.menuNotas())
            #     except:
            #         print("Error en el dato de ingreso")
            #         os.system("pause")
            #     else:
            #         if(opNotas in [1,2,3]):
            #             nota.registrarNotas(alumno,opNotas)
            #         elif(opNotas == 4):
            #             isActiveGrades = False
            codigo = input("Ingrese el codigo a buscar: ")
            menu.menuNotas(st.buscar(codigo,alumnos))
        elif (opMenu == 3):
            st.buscarAlumno(alumnos)
            os.system("pause")
        elif (opMenu == 5):
            isActive = False
