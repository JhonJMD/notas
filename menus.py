import os
import notas as nota
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Buscar Alumno\n4. Notas Finales\n5. Salir\n"
subMenuNotas = "1. Parciales\n2. Quices\n3. Trabajos\n4. Regresar al menu principal\n"
hasError = True
def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError == True):
        try: 
            return int(input(":)"))
        except ValueError:
            print("Error en el dato de ingreso")
            os.system("pause")
            hasError = True
# def menuNotas() -> int:
#     os.system("cls")
#     header = """
#     *********************
#     *MENU REGISTRO NOTAS*
#     *********************
#     """
#     print(header)
#     global hasError
#     hasError = True
#     print(subMenuNotas)
#     while (hasError == True):
#         try: 
#             return int(input(":)"))
#         except ValueError:
#             print("Error en el dato de ingreso")
#             os.system("pause")
#             hasError = True
def menuNotas(alumnos : dict):
    os.system("cls")
    header = """
    *********************
    *MENU REGISTRO NOTAS*
    *********************
    """
    isActiveMenu = True
    while (isActiveMenu):
        print(header)
        try: 
            print(subMenuNotas)
            opMenu = int(input(":)"))
        except ValueError:
            print("Opcion invalida....Recuerde que son enteros")
            os.system("pause")
        else:
            if (opMenu == 1):
                nota.addGrades(alumnos,"parciales")
            elif (opMenu == 2):
                nota.addGrades(alumnos,"quices")
            elif (opMenu == 3):
                nota.addGrades(alumnos,"trabajos")
            elif (opMenu == 4):
                isActiveMenu = False
            else:
                print("La opcion ingresada es invalida...")
                os.system("pause")