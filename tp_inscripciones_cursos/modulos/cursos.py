from modulos.utilidades import (
    buscar_estudiante_por_dni,
    buscar_curso_por_id
)

def inscribir_estudiante(lista_estudiantes, lista_cursos):
    print("\n--- INSCRIBIR ESTUDIANTE A UN CURSO ---")
    
    # 1. Pedir DNI y verificar si el estudiante existe
    dni = input("Ingrese el DNI del estudiante: ")
            
    estudiante_encontrado = buscar_estudiante_por_dni(lista_estudiantes, dni)

    if estudiante_encontrado is None:
        print("Error: El estudiante no está registrado. Primero use la opción 1.")
        return

    # 2. Mostrar los cursos disponibles
    print("\nCursos Disponibles:")
    for curso in lista_cursos:
        lugares_libres = curso["cupo_max"] - len(curso["inscriptos"])
        print(f"ID: {curso['id']} | {curso['nombre']} (Cupo Máx: {curso['cupo_max']} - Libres: {lugares_libres})")
    
    id_curso = input("\nIngrese el ID del curso al que desea inscribirse: ")

    # 3. Buscar el curso elegido

    curso_encontrado = buscar_curso_por_id(lista_cursos, id_curso)

    if curso_encontrado is None:
        print("Error: El ID del curso no es válido.")
        return

    # 4. Control de Cupos y Lista de Espera
    if dni in curso_encontrado["inscriptos"] or dni in curso_encontrado["lista_espera"]:
        print("El estudiante ya se encuentra registrado o en lista de espera para este curso.")
        return

    # Si hay lugar, entra directo
    if len(curso_encontrado["inscriptos"]) < curso_encontrado["cupo_max"]:
        curso_encontrado["inscriptos"].append(dni)
        print(f"¡Éxito! {estudiante_encontrado['nombre']} ha sido inscripto en {curso_encontrado['nombre']}.")
    else:
        # Si NO hay lugar, va a lista de espera
        curso_encontrado["lista_espera"].append(dni)
        print(f"¡CUPO LLENO! {estudiante_encontrado['nombre']} fue derivado a la LISTA DE ESPERA de {curso_encontrado['nombre']}.")

def gestionar_lista_espera(curso, lista_estudiantes):
    
    while len(curso["inscriptos"]) < curso["cupo_max"] and curso["lista_espera"]:
        dni = curso["lista_espera"].pop(0)
        curso["inscriptos"].append(dni)
        estudiante = buscar_estudiante_por_dni(lista_estudiantes, dni)

        if estudiante is not None:
            print(
                f"\n{estudiante['nombre']} fue inscripto automaticamente "
                f"desde la lista de espera al curso {curso['nombre']}"
                )

def dar_de_baja_curso(lista_estudiantes, lista_cursos):
    
    print("\n --- DAR DE BAJA DE UN CURSO ---")

    dni = input("Ingrese el DNI del estudiante: ")
    estudiante = buscar_estudiante_por_dni(lista_estudiantes, dni)

    if estudiante is None:
        print("El estudiante no esta registrado")
        return

    cursos_inscripto = []

    for curso in lista_cursos:
        if dni in curso["inscriptos"]:
            cursos_inscripto.append(curso)

    if not cursos_inscripto:
        print("El estudiante no esta inscripto en ningun curso")
        return

    print("\n Cursos en los que esta inscripto: ")

    for curso in cursos_inscripto:
        print(f"ID: {curso['id']} | {curso['nombre']}")

    id_curso = input("\n Ingrese el ID del curso: ")

    curso_baja = None

    curso_baja = buscar_curso_por_id(cursos_inscripto, id_curso)

    if curso_baja == None:
        print("El estudiante no esta inscripto en ese curso")
        return

    curso_baja["inscriptos"].remove(dni)

    print(f"\n {estudiante['nombre']} fue dado de baja de {curso_baja['nombre']}")

    gestionar_lista_espera(curso_baja, lista_estudiantes)
