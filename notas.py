import os
import alumnos as st
def addGrades(alumno : dict,categoria):
    rta = "S"
    while (rta in "S"):
        dataNota = alumno.get("notas")
        evaluacion = dataNota.get(categoria)
        nota = float(input(f"Ingrese la nota de {alumno.get("nombre").upper()}: "))
        evaluacion.append(nota)
        rta = input("Desea registrar otro Alumno? S(si) o N(no)").upper()

def registrarNotas(alumno : dict,opNotas : int):
    tipNota = ""
    rta = "S"
    print(alumno)
    while (rta in "S"):
        if (opNotas == 1):
            tipNota = "parciales"
        elif (opNotas == 2):
            tipNota = "quices"
        elif (opNotas == 3):
            tipNota = "trabajos"
        nota = float(input(f"Ingrese la nota {(len(alumno.get("notas").get(tipNota)))+1} de {tipNota}: "))
        alumno.get("notas").get(tipNota).append(nota)
        print(alumno)
        rta = input("Desea registrar otro Alumno? S(si) o N(no)").upper()