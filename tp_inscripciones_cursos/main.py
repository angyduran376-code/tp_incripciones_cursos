from modulos.funciones import registrar_estudiante, inscribir_estudiante, mostrar_estadisticas

def menu_principal():
    estudiantes = []
    
    cursos = [
        {"id": "1", "nombre": "Python Basico", "cupo_max": 2, "inscriptos": [], "lista_espera": []},
        {"id": "2", "nombre": "Disenio Web", "cupo_max": 2, "inscriptos": [], "lista_espera": []},
        {"id": "3", "nombre": "Bases de Datos", "cupo_max": 5, "inscriptos": [], "lista_espera": []}
    ]
    
    while True:
        print("\n=== SISTEMA DE INSCRIPCIÓN A CURSOS ===")
        print("1. Registrar Estudiante")
        print("2. Inscribir Estudiante a un Curso")
        print("3. Mostrar Estadisticas del Sistema")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            inscribir_estudiante(estudiantes, cursos)
        elif opcion == "3":
            mostrar_estadisticas(estudiantes, cursos)
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()