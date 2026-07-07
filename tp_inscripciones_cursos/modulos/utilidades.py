import os

def buscar_estudiante_por_dni(lista_estudiantes, dni):
	for estudiante in lista_estudiantes:
		if estudiante["dni"] == dni:
			return estudiante
	return None

def buscar_curso_por_id(lista_cursos, id_curso):
	for curso in lista_cursos:
		if curso["id"] == id_curso:
			return curso
	return None

def limpiar_pantalla():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
