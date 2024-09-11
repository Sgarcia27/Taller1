from datetime import date
from Asignatura import  Asignatura
from Profesor import Teacher
from Curs import Curso

class DetalleMatricula:
    def __init__(self, id,asignatura:Asignatura,curso:Curso,profesor:Teacher ):
        self.id = id  # Identificador único para el detalle de la matricula.
        self.asignatura = asignatura  # asignatura que se matricula.
        self.profesor = profesor  # profesor de la asignatura que se matricula.
        self.curso = curso # curso en que se matricula.
