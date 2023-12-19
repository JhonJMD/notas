import os
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
def menuNotas() -> int:
    os.system("cls")
    global hasError
    hasError = True
    print(subMenuNotas)
    while (hasError == True):
        try: 
            return int(input(":)"))
        except ValueError:
            print("Error en el dato de ingreso")
            os.system("pause")
            hasError = True