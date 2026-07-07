from modulos.utilidades import buscar_estudiante_por_dni

def mostrar_estadisticas(lista_estudiantes, lista_cursos):
    print("\n=============================================")
    print("      ESTADÍSTICAS GENERALES DEL SISTEMA     ")
    print("=============================================")
    
    print(f"\nTotal de estudiantes en el sistema: {len(lista_estudiantes)}")
    if lista_estudiantes:
        for e in lista_estudiantes:
            print(f" - DNI: {estudiante['dni']} | Nombre: {estudiante['nombre']}")
    else:
        print(" - No hay estudiantes registrados todavía.")

    print("\n--- ESTADO DE LOS CURSOS Y DEMANDA ---")
    for curso in lista_cursos:
        print(f"\n> Curso: {curso['nombre']} (ID: {curso['id']})")
        print(f"  Cupo Máximo: {curso['cupo_max']}")
        
        print(f"  Inscriptos ({len(curso['inscriptos'])}):")
        if curso["inscriptos"]:
            for dni in curso["inscriptos"]:
                estudiante = buscar_estudiante_por_dni(lista_estudiantes, dni)

                if estudiante is not None:
                    print(f"    * DNI: {dni} - {estudiante['nombre']}")
        else:
            print("    * Sin inscriptos aún.")
            
        print(f"  En Lista de Espera ({len(curso['lista_espera'])}):")
        if curso["lista_espera"]:
            for dni in curso["lista_espera"]:
                estudiante = buscar_estudiante_por_dni(lista_estudiantes, dni)

                if estudiante is not None:
                    print(f"    * DNI: {dni} - {estudiante['nombre']} (ESPERANDO)")
        else:
            print("    * Sin alumnos en espera.")
    print("\n=============================================")
