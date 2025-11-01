# Changelog
Todas las modificaciones importantes de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),  
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

---

## [Unreleased]

### Por Agregar
- Mejoras en interfaz Pygame
- Integración CI/CD adicional
- Documentación de API

---

## [1.1.0] - 2025-11-01

### Added
- **Documentación Completa del Proyecto** (PR #91, #90)
  - JUSTIFICACION.md con análisis SOLID completo
  - Diagramas UML (clases)
  - Documentación de decisiones de diseño
  - Justificación de clases, atributos y excepciones
  - Estrategias de testing documentadas
- **Actualización Automática de Reportes** (PR #89, #86)
  - Sistema de actualización automática de coverage y pylint
  - Integración de reportes en CI/CD

### Fixed
- **Correcciones Generales del Proyecto** (PR #88, #87)
  - Mejoras en estructura de archivos
  - Optimización de imports y dependencias
  - Corrección de bugs menores

---

## [1.0.0] - 2025-10-31

### Added
- **Docker**: Containerización completa del proyecto (PR #85, #84)
  - Dockerfile con Python 3.12-slim y SDL2 para Pygame
  - docker-compose.yml para orquestación de 3 servicios
  - Script helper \`docker-run.sh\` con menú interactivo
  - Documentación completa: README-DOCKER.md y DOCKER-QUICK-START.md
  - Archivo .dockerignore para optimizar builds
  - Soporte para ejecución de tests, CLI y Pygame en contenedores

### Changed
- Simplificación de requirements.txt (3 paquetes: coverage, pylint, pygame)
- Mejora de estructura de documentación
- Actualización de instrucciones de instalación y ejecución

---

## [0.9.0] - 2025-10-25

### Added
- **Interfaz Pygame**: Interfaz gráfica completa (PR #83, #82)
  - Renderizado visual del tablero con gráficos
  - Sistema de click handling para movimientos con mouse
  - Visualización de dados y turnos en pantalla
  - Indicadores visuales para jugador actual
  - Animaciones de movimiento
  - Ejecutable con \`python -m pygame_ui.pygame_ui\`

### Changed
- Separación completa entre CLI y Pygame en módulos independientes
- Actualización de README con instrucciones de interfaz gráfica

---

## [0.8.0] - 2025-10-20

### Added
- **Interfaz CLI Completa**: Sistema de línea de comandos funcional (PRs #73-79)
  - Visualización ASCII del tablero completo (24 posiciones) (PR #73, #72)
  - Menú interactivo de turnos y acciones (PR #75, #74)
  - Sistema de input validado con manejo de errores (PR #77, #76)
  - Confirmación de acciones del usuario (PR #79, #78)
  - Mensajes claros y ayuda contextual

### Fixed
- Corrección de tests relacionados con CLI (PR #81, #80)
- Mejora en validación de movimientos en interfaz

---

## [0.7.0] - 2025-10-15

### Added
- Método \`win\` para detectar victoria en BackgammonGame (PR #71, #70)
- Método \`verificar_turno_finalizado\` para validar fin de turno
- Método para gestionar fichas en almacén (PR #69, #68)
- Método \`reingresar_ficha\` en BackgammonGame (PR #67, #66)
- Método adicional en BackgammonGame (PR #65, #64)

### Changed
- Lógica de victoria completamente implementada
- Sistema de turnos más robusto
- Mejora en gestión de fichas capturadas

---

## [0.6.0] - 2025-10-09

### Added
- Método \`puede_mover\` en clase BackgammonGame (PR #61, #60)
  - Validar si un jugador puede realizar movimientos
  - Verificación de dados disponibles
- Método \`usar_dados\` en clase BackgammonGame (PR #63, #62)
  - Gestión del uso de valores de dados
  - Control de dados consumidos
- Método \`estado_juego\` en clase BackgammonGame (PR #63, #62)
  - Retorna el estado completo del juego
  - Incluye tablero, turno, dados y almacén

---

## [0.5.0] - 2025-10-01

### Added
- Método adicional en clase Dice (PR #57, #56)
  - Mejora en gestión de valores de dados
- Método \`mover_ficha\` en clase BackgammonGame (PR #59, #58)
  - Coordinación completa de movimiento de fichas
  - Validación de turnos y dados

---

## [0.4.0] - 2025-09-28

### Added
- Método en clase Dice para gestión de dados (PR #53, #52, #55, #54)
  - Lanzamiento de dados con detección de dobles
  - Gestión de valores disponibles
- Método \`cambiar_turno\` en clase BackgammonGame (PR #51, #50)
  - Alternancia automática entre jugadores
  - Validación de turnos

---

## [0.3.0] - 2025-09-23

### Added
- Método de turno en clase BackgammonGame (PR #49, #48)
  - Gestión del turno actual
  - Consulta de jugador activo
- Método \`bear_off\` en clase Tablero (PR #47, #46)
  - Implementación de acción de sacar fichas del tablero
  - Validación de bear off permitido
- Método adicional en clase Tablero (PR #45, #44)
  - Mejoras en validaciones de tablero

---

## [0.2.0] - 2025-09-16

### Added
- Método \`verificar_ganador\` en clase Tablero (PR #43, #42)
  - Detección de condición de victoria
  - Verificación de 15 fichas en banco
- Clase BackgammonGame completa (PR #41, #40)
  - Coordinador principal del juego
  - Integración de todos los componentes
- Clase Checker con sus tests (PR #39, #38, #26, #25)
  - Representación de fichas individuales
  - Métodos para posición y estado

---

## [0.1.5] - 2025-09-15

### Added
- Método \`sacar_checker_comida\` en clase Tablero (PR #37, #36)
  - Reingresar fichas capturadas desde el almacén
  - Validación de posiciones de entrada
- Método \`comer_checker\` en clase Tablero (PR #35, #34)
  - Capturar fichas enemigas solitarias
  - Gestión de almacén de fichas

---

## [0.1.4] - 2025-09-14

### Added
- Método para añadir desde el almacén (PR #33, #32)
  - Gestión de fichas capturadas
  - Sistema de reingreso al tablero
- Método \`mover_con_dado\` en clase Tablero (PR #31, #30)
  - Movimiento de fichas con validación de dados
  - Integración con sistema de dados

---

## [0.1.3] - 2025-09-13

### Added
- Método \`almacenamiento\` en clase Tablero (PR #27, #24)
  - Sistema de almacenamiento de fichas capturadas
  - Tracking de fichas fuera del tablero
- Clase BackgammonGame inicial (PR #29, #28)
  - Estructura base del coordinador del juego
  - Inicialización de componentes

---

## [0.1.2] - 2025-09-10

### Added
- Configuración de coverage para testing (PR #27, #24)
  - Setup de coverage.py
  - Configuración de reportes

---

## [0.1.1] - 2025-09-01

### Added
- Documentación de CHANGELOG (PR #21, #20)
  - Estructura de changelog
  - Documentación de prompts utilizados

### Fixed
- Corrección general del código (PR #23, #22)
  - Refactoring de código duplicado
  - Mejoras en estructura de archivos

---

## [0.1.0] - 2025-08-30

### Added
- Método \`movimiento_valido\` en clase Tablero (PR #19, #18)
  - Validación completa de movimientos
  - Verificación de reglas del Backgammon
  - Control de bloqueos y capturas

---

## [0.0.9] - 2025-08-29

### Added
- Método dentro del tablero para almacenar fichas (PR #17, #16)
  - Sistema de almacén implementado
  - Estructura de datos para fichas capturadas

---

## [0.0.8] - 2025-08-28

### Added
- Método \`mover_checker\` en clase Tablero (PR #15, #14)
  - Movimiento físico de fichas en el tablero
  - Actualización de posiciones

---

## [0.0.7] - 2025-08-27

### Added
- Método \`sacar_checker\` en clase Tablero (PR #13, #12)
  - Extracción de fichas de posiciones
  - Validación de posiciones válidas

---

## [0.0.6] - 2025-08-26

### Added
- Corrección de código y nuevo código (PR #11, #10)
  - Refactoring inicial
  - Mejoras en estructura

---

## [0.0.5] - 2025-08-25

### Added
- Creación del primer dado (PR #9, #8)
  - Clase Dados implementada
  - Método tirar_dado() con random
  - Gestión de valores de dados

---

## [0.0.4] - 2025-08-24

### Added
- Creación del tablero (PR #7, #6)
  - Clase Tablero con 24 posiciones
  - Método tablero_inicial()
  - Estructura de datos del tablero

---

## [0.0.3] - 2025-08-23

### Added
- Creación de clase Jugador (PR #5, #4)
  - Atributos: nombre, color
  - Properties con getters y setters
  - Validación de datos

---

## [0.0.2] - 2025-08-22

### Added
- Armado del proyecto inicial (PR #3, #2)
  - Estructura de carpetas
  - Configuración de GitHub Classroom
  - README inicial

---

## [0.0.1] - 2025-08-22

### Added
- Configuración inicial del repositorio
  - Setup de GitHub Classroom
  - Estructura base del proyecto
  - Archivos de configuración

---

## [0.0.0] - 2025-08-22

### Added
- Inicialización del proyecto
  - Primer commit
  - Setup de repositorio

---

[Unreleased]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.9.0...v1.0.0
[0.9.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.5...v0.2.0
[0.1.5]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.9...v0.1.0
[0.0.9]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.8...v0.0.9
[0.0.8]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.0.0...v0.0.1
[0.0.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/releases/tag/v0.0.0
