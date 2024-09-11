from datetime import date
from Periodo import Periodo
from Estudiante import Student

class Maticula :
    next_id = 0
    def __init__(self, id, periodo:Periodo, estudiante:Student, active:True):
        Maticula.next_id += 1
        self.id = Maticula.next_id  
        self.periodo = periodo  # Periodo en el que se matricula.
        self.estudiante = estudiante  # Estudiante al que se le asigna la matricula.
        self.detalleMatricula = []  # Lista para almacenar los detalles de las asignaturas del estudiante para la matricula.
        self.fecha_creacion = date.today()  # Fecha de creación del registro, se asigna la fecha actual.
        self.active = active  # Estado de actividad de la nota (True o False).
    
    @property
    def id(self):
        return self.id
    
    def __str__(self) :
        return f"id:{self.id} , Periodo:{self.periodo.getJson()} ,Estudiante:{self.estudiante.getJson()} ,Fecha de Creacion:{self.fecha_creacion} ,Active:{self.active}"
    
    def getJson(self):
        return{
            "id":self.id,
            "periodo":self.periodo.getJson(),
            "Estudainte":self.estudiante.getJson(),
            "Fecha de creacion":self.fecha_creacion,
            "activo":self.active
        }
        
    def addMatricula(self):
        pass  # Método placeholder para añadir detalles de las asignaturas de matricula.

