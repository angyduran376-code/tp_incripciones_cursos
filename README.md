# Sistema de Inscripción a Cursos (Python CLI) 📚

Este es el **Trabajo Final Integrador** desarrollado para la asignatura. Consiste en una aplicación de consola (CLI) escrita en Python que permite gestionar el registro de estudiantes, la inscripción a talleres o cursos con control estricto de cupos, la asignación automática a listas de espera y la generación de estadísticas del sistema.

---

## 👥 Integrantes del Equipo
*  [Nombre y Apellido] - [@usuario_github]
*  [Nombre y Apellido] - [@usuario_github]
*  [Nombre y Apellido] - [@usuario_github]
*  [Nombre y Apellido] - [@usuario_github]
*  [Nombre y Apellido] - [@usuario_github]
  

---

## 🚀 Funcionalidades Principales

* **Registro de Estudiantes:** Alta de alumnos con validación de DNI numérico y control de duplicados en el sistema.
* **Inscripción Eficiente:** Permite asociar estudiantes a cursos mediante ID únicos.
* **Control de Cupos Automático:** El sistema verifica las vacantes en tiempo real.
* **Lista de Espera:** Si un curso alcanza su capacidad máxima (`cupo_max`), los nuevos postulantes son derivados automáticamente a una lista de espera.
* **Módulo de Estadísticas:** Reportes detallados en consola que muestran el total de estudiantes, cursos con mayor demanda y el listado de personas inscritas o esperando lugar (con cruce de datos DNI-Nombre).

---

## 🛠️ Requisitos Técnicos Implementados

El proyecto fue diseñado aplicando las buenas prácticas solicitadas por la cátedra:
* **Modularización:** Separación de la interfaz de usuario y la lógica de negocio.
* **Estructuras de Control:** Uso dinámico de bucles (`while`, `for`) y condicionales (`if`, `elif`, `else`).
* **Estructuras de Datos:** Manejo de datos complejos mediante listas de diccionarios y colecciones anidadas.
* **Manejo de Errores:** Validaciones nativas (como `.isdigit()`) y mensajes claros para evitar interrupciones críticas en la ejecución.

---

## 📂 Estructura del Proyecto

```text
├── tp_inscripciones_cursos/   # Carpeta principal del proyecto
│   ├── main.py                # Punto de entrada de la aplicación (Menú principal)
│   └── modulos/
│       └── funciones.py       # Módulo con la lógica de negocio y validaciones
└── README.md                  # Este archivo de documentación
