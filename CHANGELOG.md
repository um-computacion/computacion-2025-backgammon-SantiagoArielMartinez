# Changelog
Todas las modificaciones importantes de este proyecto serán documentadas en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),  
y este proyecto sigue [Semantic Versioning](https://semver.org/lang/es/).

---

## [Unreleased]

---

## [0.3.0] - 2025-10-09
### Added
- Método `puede_mover` en clase BackgammonGame para validar si un jugador puede realizar movimientos (commit 871c066)
- Método `usar_dados` en clase BackgammonGame para gestionar el uso de valores de dados (commit 144668e)
- Método `estado_juego` en clase BackgammonGame que retorna el estado completo del juego (commit c2cbc96)
- Test `test_hay_almacen` para verificar fichas en almacenamiento (commit c2cbc96)

---

## [0.2.1] - 2025-10-01
### Added
- Método adicional en clase Dice (commit 0a998dd)
- Método `mover_ficha` en clase BackgammonGame (commit 92a6b7b)

---

## [0.2.0] - 2025-09-28
### Added
- Método en clase Dice para gestión de dados (commits 913e337, 4842cd7)
- Método `cambiar_turno` en clase BackgammonGame (commit 75e5bc8)

---

## [0.1.2] - 2025-09-27
### Added
- Método de turno en clase BackgammonGame (commit 788ea56)
- Método `bear_off` en clase Tablero para acción de sacar fichas (commit 0670ce6)
- Método adicional en clase Tablero (commit 46e3fa2)

---

## [0.1.0] - 2025-09-23
### Added
- Método `verificar_ganador` en clase Tablero (commit 8656bd2)

---

## [0.0.9] - 2025-09-16
### Added
- Clase Checker con sus tests
- Implementación completa de clase BackgammonGame

---

## [0.0.8] - 2025-09-15
### Added
- Método `comer_checker` en clase Tablero para capturar fichas enemigas
- Método `sacar_checker_comida` en clase Tablero para reingresar fichas capturadas

---

## [0.0.7] - 2025-09-14
### Added
- Método `mover_con_dado` en clase Tablero
- Método para ingresar fichas desde fuera del tablero (almacenamiento)

---

## [0.0.6] - 2025-09-13
### Added
- Método `almacenamiento` en clase Tablero
- Clase BackgammonGame inicial
- Archivo `.gitignore`
- Configuración de coverage

### Fixed
- Correcciones en merge de ramas

---

## [0.0.5] - 2025-09-10
### Added
- Método de almacenamiento a la clase Tablero

---

## [0.0.4] - 2025-09-01 / 2025-09-09
### Added
- Documentación de CHANGELOG
- Documentación de prompts utilizados

### Fixed
- Corrección general del código

---

## [0.0.3] - 2025-08-30
### Added
- Método `movimiento_valido` en clase Tablero para validar posiciones

---

## [0.0.2] - 2025-08-29
### Added
- Creación del almacenamiento de fichas en clase Tablero

---

## [0.0.5] - 2025-08-27
### Added
- Método `sacar_checker` en clase Tablero (commit e6a031e)

---

## [0.0.6] - 2025-08-28
### Added
- Método `mover_checker` en clase Tablero (commit 09fda25)

---

## [0.0.7] - 2025-08-29
### Added
- Creación del almacenamiento de fichas en clase Tablero (commit 972ec78)

---

## [0.0.8] - 2025-08-30
### Added
- Método `movimiento_valido` en clase Tablero para validar posiciones (commit aa26b58)

---

## [0.0.9] - 2025-09-01
### Added
- Documentación de CHANGELOG y prompts utilizados (commit 3ee6d87)

---

## [0.0.10] - 2025-09-09
### Fixed
- Corrección general del código (commit 911b243)

---

## [0.0.11] - 2025-09-10
### Added
- Método de almacenamiento a la clase Tablero (commit 3203ccd)

---

## [0.0.12] - 2025-09-13
### Added
- Configuración de coverage (commit 1660d32)
- Clase Checker con sus tests (commit 9ccd4c8)
- Clase BackgammonGame inicial (commit ab49c18)
- Archivo `.gitignore` (commit 8be80e7)

### Fixed
- Corrección de merge de ramas (commit 1441c80)

---

## [0.0.13] - 2025-09-14
### Added
- Método `mover_con_dado` en clase Tablero (commit 485a033)
- Método para ingresar fichas desde fuera del tablero (commit bf41955)

---

## [0.0.14] - 2025-09-15
### Added
- Método `comer_checker` en clase Tablero para capturar fichas enemigas (commit 0f5f9ba)
- Método `sacar_checker_comida` en clase Tablero para reingresar fichas capturadas (commit 8dc40ec)

---

## [0.0.15] - 2025-09-16
### Added
- Clase Checker completa (commit 6face77)
- Implementación completa de clase BackgammonGame (commit 57785a7)

---

## [0.0.0] - 2025-08-22
### Added
- Configuración inicial de GitHub Classroom (commits e7c49f1, b5ab2cf)
- Creación de archivos del proyecto (commit 080e642)

---

## [0.0.1] - 2025-08-23
### Added
- Creación de clase Jugador (commit ca78229)

---

## [0.0.2] - 2025-08-24
### Added
- Creación del tablero (commit 077aa8d)

---

## [0.0.3] - 2025-08-25
### Added
- Creación del primer dado (commit 666d555)

---2025-09-28 b7f0633 Merge pull request #53 from um-computacion/52-metodo-en-la-clase-dice
2025-09-28 4842cd7 Agrego metodo en la clase dice
2025-09-28 3d7d5bd Merge pull request #55 from um-computacion/54-metodo-en-la-clase-dice
2025-10-01 0a998dd Agrego metodo en la clase dice
2025-10-01 ef00a39 Merge pull request #57 from um-computacion/56-metodo-en-clase-dice
2025-10-01 92a6b7b Agrego metodo en lase backgammon , mover ficha
2025-10-01 0a5688e Merge pull request #59 from um-computacion/58-metodo-en-la-clase-backgammon
2025-10-09 871c066 Metodo puede mover
2025-10-09 90f7788 Merge pull request #61 from um-computacion/60-metodo-backgammongame
2025-10-09 144668e Metodo usar dados en la clase backgammon
2025-10-09 2c1abce Merge pull request #63 from um-computacion/62-metodo-backgammongame
2025-10-09 c2cbc96 Metoodos en la clase backgammon , estado del juego y prueba del almacen

## [0.0.4] - 2025-08-26
### Added
- Creación de jugador en backgammon (commit a3c673e)
### Fixed
- Corrección de código y carpetas (commit a3c673e)

---

[Unreleased]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/um-computacion/computacion-2025-backgammon-SantiagoArielMartinez/compare/v0.1.0...v0.2.0
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


