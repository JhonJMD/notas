import os
def regAlumnos() -> dict:
    codigo = input("Ingrese el codigo del Estudiante: ")
    nombre = input("Ingrese el nombre del Estudiante: ")
    edad = input("Ingrese la edad del Estudiante: ")
    alumno = {
        "codigo" : codigo,
        "nombre" : nombre,
        "edad" : edad,
        "notas" :{
            "parciales" : [],
            "quices" : [],
            "trabajos" : []
        }
    }
    return {codigo: alumno}
def buscarAlumno(codAlumno : str,alumnos : dict):
    data = alumnos.get(codAlumno,-1)
    if (type(data) == dict):
        for llave,valor in data.items():
            print(f"{llave} : {valor}")
        os.system("pause")
    else:
        print(f"No se encontro el Estudiante con el codigo {codAlumno}")
        os.system("pause")