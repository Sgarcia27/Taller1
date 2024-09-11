from Crud import ICrud
import time
from Curs import Curso
from Utilidades import limpiarPantalla, gotoxy, dibujarCabeza, Validar, BLUE, RESET, GREEN, RED
from clsJson import JsonFile

class menucu(ICrud):
    @staticmethod
    def create():
        limpiarPantalla()
        dibujarCabeza('Registrar curso')
        Descripcion = Validar.letras(f"{BLUE}Ingrese la Descripcion del curso:{RESET}  ", 1, 5)
        while True:
            gotoxy(1, 12)
            option = input('¿Está seguro de crear el curso? (s/n): ')
            if option.lower() == 's':
                cu = Curso(Descripcion)
                json_file = JsonFile('File/cus.json')
                cursos = json_file.read()
                cursos.append(cu.getJson()) 
                json_file.save(cursos)
                gotoxy(50, 15)
                print(f"{GREEN}Curso creado con éxito{RESET}👍")
                break
            elif option.lower() == 'n':
                gotoxy(50, 15)
                print(f"❌{RED}Operación cancelada{RESET}❌")
                break
            else:
                gotoxy(50, 15)
                print(' '*20)
                gotoxy(50, 15)
                print('Opción no válida')
                time.sleep(2)
                gotoxy(50, 15)
                print(' '*20)
        input('Presiona una tecla para continuar....')

    @staticmethod
    def update():
        limpiarPantalla()
        dibujarCabeza('Actualizar curso')
        id = input(f"{BLUE}Ingrese el id del curso: {RESET}")
        json_file = JsonFile('File/cus.json')
        cursos = json_file.read()
        found = False
        for cu in cursos:
            if cu['id'] == id:
                found = True
                print('Curso encontrado')
                print(BLUE, '='*120, RESET)
                gotoxy(50, 7)
                print(GREEN, 'Datos del curso', RESET)
                print(GREEN, 'Descripción: ', BLUE, cu['Descripcion'], RESET)
                print(GREEN, 'Estado: ', BLUE, str(cu['activo']))
                print(BLUE, '='*120, RESET)
                Descripcion = Validar.letras(f"{BLUE}Ingrese la nueva descripción del curso: {RESET}", 1, 13)
                while True:
                    gotoxy(1, 15)
                    option = input('¿Desea actualizar el estado del curso? (s/n): ')
                    if option.lower() == 's':
                        cu["activo"] = not cu["activo"]
                        break
                    elif option.lower() == 'n':
                        break
                    else:
                        gotoxy(50, 15)
                        print(' '*20)
                        gotoxy(50, 15)
                        print('Opción no válida')
                        time.sleep(2)
                        gotoxy(50, 15)
                        print(' '*20)
                cu['Descripcion'] = Descripcion
                break
        if found:
            gotoxy(1, 16)
            print(f"{GREEN}Actualizado con éxito 👍{RESET}")
            json_file.save(cursos)
        else:
            print(f"❌{RED}Curso no encontrado{RESET}❌")
        input('Presione una tecla para continuar...')

    @staticmethod
    def delete():
        limpiarPantalla()
        dibujarCabeza('Eliminar curso')
        id = input(f"{BLUE}Ingrese el id del curso: {RESET}")
        json_file = JsonFile('File/cus.json')
        cursos = json_file.read()
        update_cursos = []
        found = False
        for cu in cursos:
            if cu['id'] == id:
                found = True
                gotoxy(1, 6)
                print('Curso encontrado')
                print(BLUE, '='*120, RESET)
                gotoxy(50, 8)
                print(GREEN, 'Datos del curso', RESET)
                print(GREEN, 'Descripción: ', BLUE, cu['Descripcion'], RESET)
                print(GREEN, 'Estado: ', BLUE, str(cu['activo']))
                print(BLUE, '='*120, RESET)
        if found:
            while True:
                gotoxy(1, 13)
                decision = input('¿Está seguro de eliminar los datos? (s/n): ')
                if decision.lower() == 's':
                    update_cursos = [curso for curso in cursos if curso['id'] != id]
                    gotoxy(50, 14)
                    print(f"{GREEN}Datos eliminados con éxito 👍{RESET}")
                    json_file.save(update_cursos)
                    break
                elif decision.lower() == 'n':
                    print('Operación cancelada')
                    break
                else:
                    gotoxy(40, 13)
                    print(' '*20)
                    gotoxy(40, 13)
                    print('Opción no válida')
                    gotoxy(40, 13)
                    print(' '*20)
                    time.sleep(2)
        else:
            gotoxy(1, 5)
            print(f"❌{RED}Curso no encontrado{RESET}❌")
            time.sleep(2)
        input('Presiona una tecla para continuar')

    @staticmethod
    def consult():
        limpiarPantalla()
        dibujarCabeza('Consultar curso')
        id = input(f"{BLUE}Ingrese el id del curso: {RESET}")
        json_file = JsonFile('File/cus.json')
        curso_buscando = json_file.find('id', id)
        if curso_buscando:
            cu = curso_buscando[0]
            print(BLUE, '='*120, RESET)
            gotoxy(50, 6)
            print('Estos son los datos encontrados')
            print(BLUE, '='*120, RESET)
            print(GREEN + 'Descripción: ' + BLUE + f"{cu['Descripcion']}")
            print(GREEN + 'Estado: ' + BLUE + f"{cu['activo']}")
            print(GREEN + 'Fecha de creación: ', BLUE, str(cu['fecha_creacion']))
            print(RESET)
        else:
            print(f"❌{RED}Curso no encontrado{RESET}❌")
        input(BLUE + "Presione una tecla para continuar...")
