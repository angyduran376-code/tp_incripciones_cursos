def registrar_estudiante(lista_estudiantes):
    print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")
    
    # Validación de DNI numérico
    while True:
        dni = input("Ingrese el DNI del estudiante: ")
        if dni.isdigit():
            break
        print("Error: El DNI debe contener solo números. Intente de nuevo.")
    
    # Validación de Duplicados
    for estudiante in lista_estudiantes:
        if estudiante["dni"] == dni:
            print(f"Error: Ya existe un estudiante registrado con el DNI {dni}.")
            return

    nombre = input("Ingrese el nombre completo: ")
    
    # Guardamos en la lista
    nuevo = {"dni": dni, "nombre": nombre}
    lista_estudiantes.append(nuevo)
    print(f"\n¡Éxito! {nombre} fue registrado correctamente.")


def inscribir_estudiante(lista_estudiantes, lista_cursos):
    print("\n--- INSCRIBIR ESTUDIANTE A UN CURSO ---")
    
    # 1. Pedir DNI y verificar si el estudiante existe
    dni = input("Ingrese el DNI del estudiante: ")
    estudiante_encontrado = None
    
    for estudiante in lista_estudiantes:
        if estudiante["dni"] == dni:
            estudiante_encontrado = estudiante
            break
            
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
    curso_encontrado = None
    for curso in lista_cursos:
        if curso["id"] == id_curso:
            curso_encontrado = curso
            break
            
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


def mostrar_estadisticas(lista_estudiantes, lista_cursos):
    print("\n=============================================")
    print("      ESTADÍSTICAS GENERALES DEL SISTEMA     ")
    print("=============================================")
    
    print(f"\nTotal de estudiantes en el sistema: {len(lista_estudiantes)}")
    if lista_estudiantes:
        for e in lista_estudiantes:
            print(f" - DNI: {e['dni']} | Nombre: {e['nombre']}")
    else:
        print(" - No hay estudiantes registrados todavía.")

    print("\n--- ESTADO DE LOS CURSOS Y DEMANDA ---")
    for curso in lista_cursos:
        print(f"\n> Curso: {curso['nombre']} (ID: {curso['id']})")
        print(f"  Cupo Máximo: {curso['cupo_max']}")
        
        print(f"  Inscriptos ({len(curso['inscriptos'])}):")
        if curso["inscriptos"]:
            for dni in curso["inscriptos"]:
                for e in lista_estudiantes:
                    if e["dni"] == dni:
                        print(f"    * DNI: {dni} - {e['nombre']}")
        else:
            print("    * Sin inscriptos aún.")
            
        print(f"  En Lista de Espera ({len(curso['lista_espera'])}):")
        if curso["lista_espera"]:
            for dni in curso["lista_espera"]:
                for e in lista_estudiantes:
                    if e["dni"] == dni:
                        print(f"    * DNI: {dni} - {e['nombre']} (ESPERANDO)")
        else:
            print("    * Sin alumnos en espera.")
    print("\n=============================================")