from datetime import datetime
from clsJson import JsonFile

class Curso:
    next = 0
    
    def __init__(self, Descripcion=None):
        json_file = JsonFile('File/id.json')
        id_Curso = json_file.read()
        
        if 'id_Curso' not in id_Curso:
            id_Curso['id_Curso'] = 0
        
        Curso.next = id_Curso['id_Curso']
        Curso.next += 1
        
        self.Descripcion = Descripcion
        self.__id = ('E0' if id_Curso['id_Curso'] < 10 else 'E') + str(Curso.next)
        self.activo = True 
        self.fecha_creacion = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        
        id_Curso['id_Curso'] = Curso.next
        json_file.save(id_Curso)
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self):
        return f"Curso: {self.Descripcion}"
    
    def getJson(self):
        return {"id": self.id, "Descripcion": self.Descripcion, "activo": self.activo, "fecha_creacion": self.fecha_creacion}
