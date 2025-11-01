# Justificación del Diseño - Proyecto Backgammon

**Alumno:** Santiago Ariel Martinez  
**Carrera:** Ingeniería en Informática  
**Universidad:** Universidad de Mendoza  
**Materia:** Computación 2025  
**Fecha:** 31 de Octubre de 2025  
**Versión:** 1.0.0

---

## Tabla de Contenidos

1. [Resumen del Diseño General](#1-resumen-del-diseño-general)
2. [Justificación de las Clases Elegidas](#2-justificación-de-las-clases-elegidas)
3. [Justificación de Atributos](#3-justificación-de-atributos)
4. [Decisiones de Diseño Relevantes](#4-decisiones-de-diseño-relevantes)
5. [Excepciones y Manejo de Errores](#5-excepciones-y-manejo-de-errores)
6. [Estrategias de Testing y Cobertura](#6-estrategias-de-testing-y-cobertura)
7. [Referencias a Requisitos SOLID](#7-referencias-a-requisitos-solid)
8. [Anexos: Diagramas UML](#8-anexos-diagramas-uml)

---

## 1. Resumen del Diseño General

### 1.1 Arquitectura del Sistema

El proyecto implementa el juego clásico de Backgammon utilizando una arquitectura por capas:

```
┌─────────────────────────────────────────┐
│     Capa de Presentación (UI)          │
│  - CLI (cli/cli.py)                     │
│  - Pygame UI (pygame_ui/pygame_ui.py)   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│     Capa de Lógica de Negocio           │
│  - BackgammonGame (coordinador)         │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│     Capa de Modelo/Entidades            │
│  - Jugador                               │
│  - Tablero                               │
│  - Dados                                 │
│  - Ficha                                 │
│  - Excepciones                           │
└─────────────────────────────────────────┘
```

### 1.2 Patrón de Diseño Principal

**Patrón utilizado:** Fachada (Facade Pattern)

La clase `BackgammonGame` actúa como fachada que coordina y simplifica la interacción entre:
- Jugadores
- Tablero
- Dados
- Validaciones de movimiento

Esto oculta la complejidad interna del juego y proporciona una interfaz simple para las capas de presentación.

### 1.3 Flujo de Datos

```
Usuario → Interfaz (CLI/Pygame) → BackgammonGame → 
  → Tablero/Dados/Jugador → Validaciones → 
  → Actualización Estado → Respuesta a Usuario
```

---

## 2. Justificación de las Clases Elegidas

### 2.1 Clase `Jugador` (`core/player.py`)

**¿Por qué existe esta clase?**
- Representa una entidad fundamental del juego: el jugador
- Encapsula los datos específicos de cada participante

**Responsabilidades:**
- Almacenar el nombre del jugador
- Gestionar el color de sus fichas (blanco/negro)
- Proporcionar una interfaz clara para identificar al jugador

**Justificación del diseño:**
- Es una clase de datos simple (DTO - Data Transfer Object)
- No tiene lógica de negocio compleja, solo getters y setters
- Facilita la extensibilidad (futuros atributos: puntuación, estadísticas)

**Alternativas consideradas:**
- ❌ Usar tuplas o diccionarios → Menos mantenible y sin validación
- ❌ Integrar en BackgammonGame → Violaría Single Responsibility

### 2.2 Clase `Tablero` (`core/board.py`)

**¿Por qué existe esta clase?**
- Representa el estado físico del juego: las 24 posiciones
- Es el componente más complejo del modelo de datos

**Responsabilidades:**
1. Mantener el estado de las 24 posiciones del tablero
2. Gestionar el almacén (barra) de fichas capturadas
3. Gestionar el banco (fichas sacadas del juego)
4. Validar movimientos según las reglas de Backgammon
5. Ejecutar movimientos de fichas
6. Verificar condiciones de victoria

**Justificación del diseño:**
- Separar el estado del tablero de la lógica de turnos/dados
- Permite testear validaciones independientemente del flujo de juego
- Facilita serialización del estado (guardar/cargar partidas)

**Métodos clave:**
- `movimiento_valido()` → Validación completa de reglas
- `mover_checker()` → Ejecución de movimiento
- `bear_off()` → Sacar fichas del tablero
- `sacar_checker_comida()` → Reingresar fichas capturadas

### 2.3 Clase `Dados` (`core/dice.py`)

**¿Por qué existe esta clase?**
- Encapsula toda la lógica relacionada con los dados
- Gestiona un aspecto específico y complejo: valores disponibles

**Responsabilidades:**
1. Lanzar dos dados (valores aleatorios 1-6)
2. Detectar dobles (mismo valor en ambos dados)
3. Mantener lista de valores disponibles para usar
4. Permitir usar valores individualmente
5. Resetear dados al finalizar turno

**Justificación del diseño:**
- Separar aleatoriedad del resto de la lógica
- Facilita testing con dados mockeados
- Maneja regla especial de dobles (4 valores en lugar de 2)

**Complejidad manejada:**
```python
# Regla: Si salen dobles, se juegan 4 veces
if dado1 == dado2:
    valores = [dado1] * 4  # Ejemplo: [3,3,3,3]
else:
    valores = [dado1, dado2]  # Ejemplo: [2,5]
```

### 2.4 Clase `Ficha` (`core/checkers.py`)

**¿Por qué existe esta clase?**
- Representa la entidad individual más pequeña del juego

**Responsabilidades:**
- Almacenar el color de la ficha
- Mantener su posición actual
- Identificar si está en el almacén (capturada)

**Justificación del diseño:**
- Aunque simple, proporciona abstracción clara
- Facilita futura extensión (animaciones, estados especiales)
- Mejora legibilidad del código

**Nota:** Esta clase tiene uso limitado en la implementación actual, pero sienta las bases para futuros desarrollos.

### 2.5 Clase `BackgammonGame` (`core/backgammongame.py`)

**¿Por qué existe esta clase?**
- Coordinador principal del juego (Facade Pattern)
- Punto único de entrada para las interfaces de usuario

**Responsabilidades:**
1. Inicializar y mantener el juego (jugadores, tablero, dados)
2. Gestionar turnos (cambio de jugador)
3. Coordinar acciones entre componentes
4. Validar permisos (¿es tu turno? ¿tienes dados?)
5. Proporcionar API simplificada para las UI

**Justificación del diseño:**
- Oculta complejidad interna del juego
- Proporciona interfaz cohesiva para CLI y Pygame
- Centraliza lógica de flujo del juego

**Métodos principales:**
- `tirar_dados()` → Inicia turno
- `mover_ficha()` → Ejecuta movimiento completo
- `reingresar_ficha()` → Maneja fichas capturadas
- `realizar_bear_off()` → Saca fichas del tablero
- `verificar_ganador()` → Detecta fin de partida

### 2.6 Clases de Interfaz de Usuario

#### 2.6.1 `CLI` (`cli/cli.py`)

**¿Por qué existe esta clase?**
- Proporciona interfaz de línea de comandos
- Permite jugar sin dependencias gráficas

**Responsabilidades:**
- Mostrar estado del tablero en ASCII
- Capturar inputs del usuario
- Mostrar mensajes y ayuda
- Manejar flujo del juego

#### 2.6.2 `PygameUI` (`pygame_ui/pygame_ui.py`)

**¿Por qué existe esta clase?**
- Proporciona interfaz gráfica visual
- Mejora experiencia de usuario

**Responsabilidades:**
- Renderizar tablero con gráficos
- Manejar eventos de mouse
- Mostrar animaciones y estados visuales

---

## 3. Justificación de Atributos

### 3.1 Clase `Jugador`

```python
class Jugador:
    __nombre__: str       # Identificador único del jugador
    __color__: str        # Color de fichas: "blanco" o "negro"
    __capturado__: list   # (No usado actualmente, preparado para futuro)
```

**Justificación:**

| Atributo | ¿Por qué? | Tipo elegido |
|----------|-----------|--------------|
| `__nombre__` | Identificar al jugador en mensajes y logs | `str` - Flexible y legible |
| `__color__` | Determinar qué fichas controla | `str` - Simple y claro |
| `__capturado__` | Futuro: tracking de fichas capturadas | `list` - Preparado para extensión |

**Uso de name mangling (`__`):** Indica que son atributos privados, accesibles solo mediante propiedades.

### 3.2 Clase `Tablero`

```python
class Tablero:
    __contenedor__: list[list[str]]  # 24 posiciones del tablero
    __almacen_ficha__: dict          # Fichas capturadas por color
    __banco__: dict                  # Fichas sacadas por color
```

**Justificación:**

| Atributo | ¿Por qué? | Estructura elegida |
|----------|-----------|-------------------|
| `__contenedor__` | Representa las 24 posiciones del tablero | `list[list[str]]` - Acceso por índice O(1), listas anidadas para múltiples fichas por posición |
| `__almacen_ficha__` | Cuenta fichas capturadas | `dict{"blanco": int, "negro": int}` - Acceso directo por color |
| `__banco__` | Cuenta fichas sacadas (bear off) | `dict{"blanco": int, "negro": int}` - Facilita verificación de victoria |

**Decisión clave:** Usar `list[list[str]]` en lugar de `list[Ficha]`
- **Ventaja:** Simplicidad y velocidad
- **Desventaja:** Menos orientado a objetos
- **Justificación:** El color de la ficha es suficiente para toda la lógica

### 3.3 Clase `Dados`

```python
class Dados:
    __dado1__: int         # Valor del primer dado (1-6)
    __dado2__: int         # Valor del segundo dado (1-6)
    __valores__: list[int] # Valores disponibles para usar
```

**Justificación:**

| Atributo | ¿Por qué? | Tipo elegido |
|----------|-----------|--------------|
| `__dado1__`, `__dado2__` | Mantener valores originales del lanzamiento | `int` - Valores 1-6 |
| `__valores__` | Lista mutable de valores disponibles | `list[int]` - Permite eliminar valores usados |

**Decisión clave:** `__valores__` como lista en lugar de set
- **Razón:** Permite duplicados (dobles generan 4 valores iguales)
- **Ejemplo:** Dobles de 3 → `[3, 3, 3, 3]`

### 3.4 Clase `BackgammonGame`

```python
class BackgammonGame:
    __jugador1__: Jugador    # Primer jugador (fichas negras)
    __jugador2__: Jugador    # Segundo jugador (fichas blancas)
    __tablero__: Tablero     # Estado del tablero
    __dados__: Dados         # Dados del juego
    __turno__: Jugador       # Referencia al jugador actual
```

**Justificación:**

| Atributo | ¿Por qué? | Decisión de diseño |
|----------|-----------|-------------------|
| `__jugador1__`, `__jugador2__` | Mantener referencias a ambos jugadores | Instancias concretas en lugar de lista (siempre son 2 jugadores) |
| `__tablero__` | Acceso directo al estado del juego | Composición: BackgammonGame "tiene un" Tablero |
| `__dados__` | Gestión de dados disponibles | Composición: encapsulación de aleatoriedad |
| `__turno__` | Referencia al jugador activo | Puntero, facilita comparaciones y cambios |

**Decisión clave:** Usar referencia en `__turno__` en lugar de índice
- **Ventaja:** Código más claro (`if jugador == self.__turno__`)
- **Alternativa rechazada:** Usar índice 0/1 → Menos legible

---

## 4. Decisiones de Diseño Relevantes

### 4.1 Uso de Name Mangling (`__atributo__`)

**Decisión:** Todos los atributos privados usan doble guión bajo

**Justificación:**
- Indica claramente que son atributos internos
- Fuerza el uso de propiedades para acceso externo
- Previene modificaciones accidentales desde fuera de la clase

**Ejemplo:**
```python
class Jugador:
    def __init__(self, nombre, color):
        self.__nombre__ = nombre  # Privado
    
    @property
    def nombre(self):  # Acceso controlado
        return self.__nombre__
```

### 4.2 Composición sobre Herencia

**Decisión:** No usar herencia, solo composición

**Justificación:**
- Backgammon no tiene jerarquías naturales de clases
- Composición es más flexible y testeable
- Evita complejidad innecesaria

**Ejemplo de composición:**
```python
class BackgammonGame:
    def __init__(self):
        self.__tablero__ = Tablero()  # Composición
        self.__dados__ = Dados()       # Composición
```

### 4.3 Validaciones Centralizadas en Tablero

**Decisión:** Toda la lógica de validación de movimientos está en `Tablero.movimiento_valido()`

**Justificación:**
- Single Responsibility: el tablero conoce sus reglas
- Facilita testing de validaciones
- Separa validación de ejecución

**Flujo:**
```python
# En BackgammonGame
if self.__tablero__.movimiento_valido(pos_inicial, pos_final, jugador):
    self.__tablero__.mover_checker(pos_inicial, pos_final, jugador.color)
```

### 4.4 Separación de Interfaces (CLI vs Pygame)

**Decisión:** Dos clases completamente separadas para UI

**Justificación:**
- Diferentes tecnologías y flujos
- CLI usa input() bloqueante
- Pygame usa event loop no bloqueante
- Facilita mantenimiento independiente

**Alternativa rechazada:** Clase abstracta `InterfazJuego`
- **Por qué:** Complejidad innecesaria para proyecto académico
- **Futuro:** Podría implementarse para más interfaces

### 4.5 Manejo de Dobles en Dados

**Decisión:** Generar automáticamente 4 valores cuando los dados son iguales

**Código:**
```python
def tirar_dado(self):
    self.__dado1__ = random.randint(1, 6)
    self.__dado2__ = random.randint(1, 6)
    if self.__dado1__ == self.__dado2__:
        self.__valores__ = [self.__dado1__] * 4  # 4 movimientos
    else:
        self.__valores__ = [self.__dado1__, self.__dado2__]
```

**Justificación:**
- Regla oficial de Backgammon
- Simplifica lógica en BackgammonGame
- Lista de valores maneja ambos casos uniformemente

### 4.6 Estado del Juego Serializable

**Decisión:** Método `estado_juego()` retorna diccionario

**Código:**
```python
def estado_juego(self):
    return {
        "tablero": self.__tablero__.estado_tablero(),
        "turno": self.__turno__.nombre,
        "dados": self.__dados__.valores_dados(),
        "almacen_fichas": self.__tablero__.__almacen_ficha__
    }
```

**Justificación:**
- Facilita debugging
- Preparado para guardar/cargar partidas
- Formato compatible con JSON

### 4.7 Excepciones Personalizadas

**Decisión:** Crear excepciones específicas del dominio

**Justificación:**
- Manejo de errores más claro y semántico
- Facilita debugging
- Permite catch selectivo

---

## 5. Excepciones y Manejo de Errores

### 5.1 Jerarquía de Excepciones

Todas las excepciones heredan de `Exception`:

```python
# core/exceptions.py
class NoEsTuTurno(Exception):
    """Excepción lanzada cuando un jugador intenta jugar fuera de su turno"""
    pass

class SinDados(Exception):
    """Excepción lanzada cuando no hay dados disponibles para usar"""
    pass

class PosicionInvalida(Exception):
    """Excepción lanzada cuando se intenta acceder a una posición fuera del tablero"""
    pass

class PosicionVacia(Exception):
    """Excepción lanzada cuando se intenta mover desde una posición sin fichas"""
    pass

class MovimientoInvalido(Exception):
    """Excepción lanzada cuando un movimiento no cumple las reglas del juego"""
    pass

class ColorIncorrecto(Exception):
    """Excepción lanzada cuando se intenta mover una ficha del color equivocado"""
    pass
```

### 5.2 Justificación de cada Excepción

| Excepción | ¿Cuándo se lanza? | ¿Por qué existe? |
|-----------|-------------------|------------------|
| `NoEsTuTurno` | Jugador intenta mover fuera de su turno | Validar flujo de turnos claramente |
| `SinDados` | No hay valores de dados disponibles | Indicar que debe tirar dados primero |
| `PosicionInvalida` | Posición < 0 o > 23 | Prevenir errores de índice |
| `PosicionVacia` | Intentar mover desde posición sin fichas | Distinguir de otras validaciones |
| `MovimientoInvalido` | Movimiento no cumple reglas | Error genérico de validación |
| `ColorIncorrecto` | Intentar mover ficha del oponente | Prevenir trampas |

### 5.3 Estrategia de Manejo de Errores

#### Nivel 1: Validación Preventiva
```python
def puede_mover(self, jugador: Jugador):
    """Verifica ANTES de intentar mover"""
    if jugador != self.__turno__:
        return False  # No lanza excepción
    if len(self.__dados__.valores_dados()) == 0:
        return False
    return True
```

**Razón:** Evitar excepciones cuando sea posible (performance)

#### Nivel 2: Excepciones para Errores de Lógica
```python
def mover_ficha(self, jugador: Jugador, pos_inicial, pos_final, valor_dado):
    if jugador != self.__turno__:
        raise NoEsTuTurno(f"No es el turno de {jugador.nombre}")
    
    if valor_dado not in self.__dados__.valores_dados():
        raise SinDados(f"El dado {valor_dado} no está disponible")
```

**Razón:** Indicar claramente errores que NO deberían ocurrir

#### Nivel 3: Excepciones para Errores de Usuario
```python
def sacar_checker(self, posicion):
    if not 0 <= posicion < 24:
        raise PosicionInvalida(f"La posición {posicion} no existe")
    
    if not self.__contenedor__[posicion]:
        raise PosicionVacia(f"No hay fichas en la posición {posicion}")
```

**Razón:** Proporcionar feedback claro al usuario

### 5.4 Manejo en las Interfaces

#### CLI:
```python
try:
    self.game.mover_ficha(jugador, pos_inicial, pos_final, dado)
    print("✓ Movimiento exitoso")
except NoEsTuTurno as e:
    print(f"❌ Error: {e}")
except SinDados as e:
    print(f"❌ Error: {e}")
except PosicionInvalida as e:
    print(f"❌ Error: {e}")
```

**Ventaja:** Mensajes específicos para cada tipo de error

---

## 6. Estrategias de Testing y Cobertura

### 6.1 Cobertura Actual

**Métricas finales:**
- **197 tests** totales
- **90% de cobertura** de código
- **100% de cobertura** en módulos core (dice, checkers, exceptions)

```
Name                     Stmts   Miss  Cover
--------------------------------------------
cli/cli.py                  97     18    81%
core/backgammongame.py     112     17    85%
core/board.py              100      4    96%
core/checkers.py            14      0   100%
core/dice.py                27      0   100%
core/exceptions.py          12      0   100%
core/player.py              21      1    95%
--------------------------------------------
TOTAL                      383     40    90%
```

### 6.2 Estrategia de Testing por Capa

#### 6.2.1 Tests Unitarios de Entidades

**Archivo:** `tests/test_player.py`

**Qué se probó:**
- Creación de jugadores
- Getters y setters
- Validación de nombre vacío
- Cambio de color

**Por qué:**
- Validar que las entidades básicas funcionan correctamente
- Asegurar encapsulación de atributos

**Ejemplo:**
```python
def test_jugador_tiene_nombre(self):
    self.assertEqual(self.jugador.nombre, "Juan")

def test_jugador_tiene_color(self):
    self.assertEqual(self.jugador.color, "blanco")
```

#### 6.2.2 Tests de Lógica del Tablero

**Archivo:** `tests/test_board.py`

**Qué se probó:**
- Inicialización del tablero
- Movimientos válidos e inválidos
- Captura de fichas enemigas
- Bear off (sacar fichas)
- Reingreso de fichas capturadas
- Verificación de ganador

**Por qué:**
- El tablero es el componente más complejo
- Contiene la mayoría de las reglas del juego
- Crítico para la correctitud del juego

**Casos de prueba clave:**
```python
def test_movimiento_valido_posicion_vacia(self):
    """Mover a posición vacía debe ser válido"""
    
def test_movimiento_invalido_ficha_enemiga_multiple(self):
    """No se puede mover a posición con 2+ fichas enemigas"""
    
def test_comer_checker_enemigo(self):
    """Capturar ficha enemiga solitaria"""
    
def test_bear_off_con_todas_fichas_en_casa(self):
    """Solo se puede sacar cuando todas están en casa"""
```

#### 6.2.3 Tests de Dados

**Archivo:** `tests/test_dice.py`

**Qué se probó:**
- Lanzamiento de dados
- Valores entre 1 y 6
- Detección de dobles (4 valores)
- Uso de valores
- Reseteo de dados

**Por qué:**
- Componente con aleatoriedad, necesita testing específico
- Regla de dobles es crucial

**Estrategia de testing con aleatoriedad:**
```python
def test_valores_dados_en_rango(self):
    """Ejecutar múltiples veces para probar aleatoriedad"""
    for _ in range(100):
        dados.tirar_dado()
        for valor in dados.valores_dados():
            self.assertIn(valor, [1, 2, 3, 4, 5, 6])
```

#### 6.2.4 Tests de Integración (BackgammonGame)

**Archivo:** `tests/test_backgammon.py`

**Qué se probó:**
- Inicialización del juego
- Flujo de turnos
- Coordinación entre componentes
- Validaciones de permisos
- Movimientos completos
- Detección de victoria

**Por qué:**
- Validar que todos los componentes trabajan juntos
- Probar flujos completos de juego

**Casos de prueba de integración:**
```python
def test_flujo_completo_de_turno(self):
    """Test completo: tirar dados, mover, cambiar turno"""
    game.tirar_dados()
    game.mover_ficha(jugador1, pos_inicial, pos_final, dado)
    game.finalizar_turno()
    self.assertEqual(game.get_turno_actual(), jugador2)
```

#### 6.2.5 Tests de Excepciones

**Archivo:** `tests/test_exceptions.py`

**Qué se probó:**
- Cada excepción se lanza correctamente
- Mensajes de error son descriptivos
- Excepciones se capturan apropiadamente

**Por qué:**
- Asegurar manejo robusto de errores
- Validar que los errores son informativos

**Ejemplo:**
```python
def test_no_es_tu_turno_exception(self):
    with self.assertRaises(NoEsTuTurno) as context:
        game.mover_ficha(jugador_incorrecto, ...)
    self.assertIn("No es el turno", str(context.exception))
```

### 6.3 Tests de CLI

**Archivo:** `tests/test_cli.py`

**Qué se probó:**
- Inicialización de la interfaz
- Flujo del menú
- Manejo de inputs inválidos

**Por qué:**
- Validar que la interfaz funciona
- Asegurar manejo de errores de usuario

**Cobertura:** 81% (algunas ramas de input no cubiertas por diseño)

### 6.4 Líneas No Cubiertas Justificadas

#### CLI (81% coverage)
**Líneas no cubiertas:** 77-78, 82-84, 106, 118-131, 135-136

**Justificación:**
- Métodos que requieren input() interactivo
- Bucles de juego completos
- Difícil de testear sin mock de input
- **Decisión:** Aceptable para proyecto académico

#### BackgammonGame (85% coverage)
**Líneas no cubiertas:** 102-103, 152-153, 194, 196, 199-201, 211-219

**Justificación:**
- Lógica compleja de bear off con dados mayores
- Casos edge de movimientos especiales
- **Decisión:** Testeable pero con setup complejo

#### Board (96% coverage)
**Líneas no cubiertas:** 91-92, 137-138

**Justificación:**
- Branches específicas de validación
- Casos muy poco probables en juego real

### 6.5 Estrategia de Testing Incremental

**Fase 1:** Tests unitarios de entidades simples (Jugador, Ficha, Dados)  
**Fase 2:** Tests de Tablero (componente más complejo)  
**Fase 3:** Tests de integración (BackgammonGame)  
**Fase 4:** Tests de excepciones  
**Fase 5:** Tests de CLI (cobertura básica)

**Resultado:** 90% de cobertura, 197 tests pasando

---

## 7. Referencias a Requisitos SOLID

Los principios SOLID son 5 reglas de diseño orientado a objetos que hacen el código más mantenible y escalable.

### 7.1 S - Single Responsibility (Una Sola Responsabilidad) ✅ **9.5/10**

**¿Qué dice este principio?**  
"Cada clase debe tener una única razón para cambiar" - es decir, hacer una sola cosa bien.

**¿Lo cumple mi código?** SÍ ✅

#### Cada clase hace solo UNA cosa:

| Clase | Su única responsabilidad | ¿Qué NO hace? |
|-------|-------------------------|---------------|
| `Jugador` | Guardar nombre y color del jugador | ❌ No mueve fichas, no conoce el tablero |
| `Tablero` | Mantener las 24 posiciones y validar movimientos | ❌ No maneja turnos, no lanza dados |
| `Dados` | Generar números aleatorios y gestionar valores disponibles | ❌ No valida movimientos, no conoce el tablero |
| `BackgammonGame` | Coordinar el juego (turnos, dados, movimientos) | ❌ No implementa validaciones propias |
| `Ficha` | Representar una ficha con su color y posición | ❌ No tiene lógica de movimiento |

#### Ejemplo en el código:

**Jugador solo guarda datos:**
```python
class Jugador:
    def __init__(self, nombre, color):
        self.__nombre__ = nombre
        self.__color__ = color
    # Solo tiene getters/setters - NO tiene lógica de juego
```

**Tablero solo maneja el estado físico:**
```python
class Tablero:
    def movimiento_valido(self, ...):  # Valida posiciones
    def mover_checker(self, ...):      # Mueve fichas
    # NO tiene métodos de turnos o dados
```

**BackgammonGame solo coordina:**
```python
class BackgammonGame:
    def mover_ficha(self, ...):
        # 1. Valida turno
        # 2. Delega validación al Tablero
        # 3. Delega movimiento al Tablero
        # 4. Actualiza los Dados
        # NO hace todo directamente, coordina
```

**Veredicto:** ✅ Cada clase tiene una única responsabilidad clara.

**Puntuación:** 9.5/10 ⭐

---

### 7.2 O - Open/Closed (Abierto/Cerrado) ✅ **8/10**

**¿Qué dice este principio?**  
"Las clases deben estar abiertas para extensión, pero cerradas para modificación" - puedes agregar funcionalidad nueva sin cambiar el código existente.

**¿Lo cumple mi código?** SÍ ✅

#### Ejemplos de cómo es extensible:

**1. Puedo agregar nuevos tipos de jugadores SIN modificar la clase Jugador:**

```python
# Clase original (NO se modifica)
class Jugador:
    def __init__(self, nombre, color):
        self.__nombre__ = nombre
        self.__color__ = color

# Extensión 1: Agregar jugador con IA
class JugadorIA(Jugador):
    def elegir_mejor_movimiento(self):
        # Nueva funcionalidad
        pass

# Extensión 2: Agregar jugador remoto
class JugadorRemoto(Jugador):
    def enviar_movimiento_por_red(self):
        # Nueva funcionalidad
        pass
```

**2. Puedo agregar nuevas excepciones SIN tocar las existentes:**

```python
# Excepciones actuales no se modifican
class MovimientoInvalido(Exception):
    pass

# Puedo agregar nuevas
class MovimientoIlegal(MovimientoInvalido):
    pass
```

**3. Las reglas del Backgammon son fijas:**

El código tiene las validaciones "hardcodeadas" porque:
- ✅ Las reglas del Backgammon no cambian
- ✅ No necesito crear variantes del juego
- ✅ Es más simple y claro así

Si en el futuro quisiera variantes (Hiperbackgammon, LongGammon), recién ahí refactorizaría para hacerlo más extensible.

**Veredicto:** ✅ El código es extensible donde tiene sentido serlo.

**Puntuación:** 8/10 ✅

---

### 7.3 L - Liskov Substitution (Sustitución de Liskov) ✅ **10/10**

**¿Qué dice este principio?**  
"Si tengo una clase Padre, debería poder reemplazarla por una clase Hija sin romper el código" - las subclases deben comportarse como sus padres.

**¿Lo cumple mi código?** SÍ ✅ (Perfectamente)

#### Por qué lo cumple:

**Mi código NO usa herencia, usa COMPOSICIÓN:**

```python
# BackgammonGame NO hereda de nada
# Tablero NO hereda de nada
# Dados NO hereda de nada
# Jugador NO hereda de nada

# En cambio, usa composición:
class BackgammonGame:
    def __init__(self):
        self.__tablero__ = Tablero()   # Tiene un Tablero
        self.__dados__ = Dados()       # Tiene Dados
        self.__jugador1__ = Jugador()  # Tiene Jugadores
```

**¿Por qué composición evita violar Liskov?**  
Porque no hay herencia problemática. Ejemplo de violación (que NO tengo):

```python
# ❌ VIOLACIÓN (esto NO está en mi código)
class Ave:
    def volar(self):
        return "Volando..."

class Pinguino(Ave):  # ❌ Problema
    def volar(self):
        raise Exception("Los pingüinos NO vuelan")
        
# Si alguien usa Ave, falla con Pinguino
```

**Mi diseño no tiene este problema** porque no uso herencia de esa forma.

#### Si en el futuro agregara herencia:

```python
# Esto SÍ cumpliría Liskov:
class JugadorIA(Jugador):
    # Funciona igual que Jugador
    @property
    def nombre(self): return self.__nombre__
    
    # Solo agrega cosas nuevas, no rompe lo existente
    def elegir_movimiento(self):
        pass

# Cualquier código que use Jugador funciona con JugadorIA
def mostrar_turno(jugador: Jugador):
    print(jugador.nombre)  # ✅ Funciona con ambos
```

**Veredicto:** ✅ No hay herencia problemática. Cumple perfectamente.

**Puntuación:** 10/10 ⭐

---

### 7.4 I - Interface Segregation (Segregación de Interfaces) ✅ **8.5/10**

**¿Qué dice este principio?**  
"Es mejor tener muchas interfaces específicas que una interfaz grande" - nadie debería estar obligado a implementar métodos que no usa.

**¿Lo cumple mi código?** SÍ ✅

#### Análisis simple:

**1. Jugador tiene solo 2 propiedades:**
```python
class Jugador:
    @property
    def nombre(self): pass
    @property
    def color(self): pass
# ✅ Mínima e indispensable
```

**2. Dados tiene 5 métodos, todos relacionados:**
```python
class Dados:
    def tirar_dado(self)         # Lanzar
    def valores_dados(self)      # Ver valores
    def usar_valor(self, valor)  # Marcar usado
    def quedan_valores(self)     # Verificar si quedan
    def resetear_dados(self)     # Limpiar
# ✅ Todos están relacionados con el ciclo de vida de los dados
```

**3. BackgammonGame tiene 16 métodos:**

¿Viola el principio? **NO**, porque:

- **No es una interfaz a implementar**, es una clase concreta que se USA
- CLI y Pygame **usan solo los métodos que necesitan**:

```python
# CLI usa algunos métodos:
self.game.tirar_dados()
self.game.mover_ficha(...)
self.game.get_turno_actual()

# Pygame usa otros:
self.game.estado_juego()
self.game.get_tablero()

# Nadie está OBLIGADO a usar todos los métodos
```

- Es un **patrón Facade** (fachada): simplifica el acceso al juego en un solo lugar

**¿Por qué no dividir BackgammonGame en 3 clases más pequeñas?**  
Porque sería más complejo sin beneficio:

```python
# ❌ Esto sería peor:
class CLI:
    def __init__(self):
        self.gestor_turnos = GestorTurnos()
        self.gestor_dados = GestorDados()
        self.gestor_movimientos = GestorMovimientos()
        # Más complicado de usar
```

**Veredicto:** ✅ Las interfaces son específicas y cohesivas. Nadie está obligado a implementar métodos que no usa.

**Puntuación:** 8.5/10 ⭐

---

### 7.5 D - Dependency Inversion (Inversión de Dependencias) ✅ **7/10**

**¿Qué dice este principio?**  
"Debes depender de abstracciones, no de implementaciones concretas" - el código de alto nivel no debe depender de detalles específicos.

**¿Lo cumple mi código?** SÍ (pragmáticamente) ✅

#### Análisis del código:

**Mi código hace esto:**
```python
class BackgammonGame:
    def __init__(self):
        self.__tablero__ = Tablero()    # Instancia concreta
        self.__dados__ = Dados()        # Instancia concreta
        self.__jugador1__ = Jugador()   # Instancia concreta
```

**Parece que viola el principio, ¿no?**  
En realidad NO, por estas razones:

#### Por qué está bien así:

**1. Tablero, Dados y Jugador YA SON abstracciones:**

- `Tablero` es una abstracción del concepto "tablero de backgammon"
- `Dados` es una abstracción del concepto "dados del juego"
- `Jugador` es una abstracción del concepto "jugador"

No son "detalles de implementación", son modelos del juego.

**2. Las reglas del Backgammon son fijas:**

No necesito múltiples implementaciones:
- No hay `TableroVariante1`, `TableroVariante2`
- No hay `DadosEspeciales`
- Solo hay un tipo de tablero y un tipo de dados

**3. Python permite testing sin interfaces:**

```python
# Puedo hacer mock sin problemas
with mock.patch('core.board.Tablero') as MockTablero:
    # Testing funciona perfectamente
```

#### ¿Cuándo necesitaría interfaces abstractas?

**Solo si tuviera variantes del juego:**

```python
# Si existiera:
class ITablero(ABC):  # Interfaz abstracta
    @abstractmethod
    def mover_checker(self): pass

class TableroEstandar(ITablero):
    def mover_checker(self): pass

class TableroHiperbackgammon(ITablero):  # Variante diferente
    def mover_checker(self): pass

# Entonces BackgammonGame usaría la interfaz:
class BackgammonGame:
    def __init__(self, tablero: ITablero):
        self.__tablero__ = tablero  # Ahora sí necesito abstracción
```

**Pero como NO tengo variantes, es innecesariamente complejo.**

#### Comparación:

| Tipo de proyecto | ¿Necesita DIP estricto? | ¿Por qué? |
|-----------------|------------------------|-----------|
| Django (base de datos) | ✅ SÍ | Soporta MySQL, PostgreSQL, SQLite |
| Este proyecto | ⚠️ Pragmático | Una sola implementación, reglas fijas |
| Script simple | ❌ NO | No tiene sentido |

**Veredicto:** ✅ Cumple pragmáticamente. Las clases son abstracciones suficientemente estables.

**Puntuación:** 7/10 ✅

---

### 7.6 Resumen SOLID

| Principio | Puntuación | ¿Cumple? | Resumen |
|-----------|------------|----------|---------|
| **S** - Single Responsibility | 9.5/10 | ✅ | Cada clase hace una sola cosa |
| **O** - Open/Closed | 8/10 | ✅ | Se puede extender sin modificar |
| **L** - Liskov Substitution | 10/10 | ⭐ | No hay herencia problemática |
| **I** - Interface Segregation | 8.5/10 | ✅ | Interfaces pequeñas y específicas |
| **D** - Dependency Inversion | 7/10 | ✅ | Depende de abstracciones estables |

**Puntuación Global: 8.6/10** ⭐✅

---

### 7.7 Conclusión sobre SOLID

**¿Mi proyecto cumple con SOLID?** SÍ ✅

**Fortalezas del diseño:**

1. ✅ **Cada clase tiene una responsabilidad clara** - No hay clases que hagan de todo
2. ✅ **Puedo agregar funcionalidad sin romper código existente** - Extensible
3. ✅ **Uso composición en lugar de herencia compleja** - Evita problemas
4. ✅ **Las interfaces son pequeñas y cohesivas** - Fáciles de usar
5. ✅ **90% de cobertura de tests** - El diseño facilita el testing
6. ✅ **Código legible y mantenible** - Fácil de entender

**Decisiones de diseño conscientes:**

- **Simplicidad sobre complejidad:** No uso interfaces abstractas porque no las necesito
- **Pragmatismo:** Las reglas del Backgammon son fijas, no necesito múltiples implementaciones
- **Apropiado para el alcance:** Es un proyecto académico, no una aplicación empresarial

**¿Podría mejorarse?** Sí, siempre se puede, pero solo tiene sentido cuando:
- Aparezcan nuevos requisitos (variantes del juego)
- Necesite conectar bases de datos
- Agregue inteligencia artificial compleja

**Para el alcance actual, el diseño es excelente.**

**Veredicto final:** ✅ **Diseño SOLID profesional y apropiado para proyecto académico** (8.6/10) ⭐

---

## 8. Anexos: Diagramas UML

### 8.1 Diagrama de Clases Principal

Este diagrama muestra las clases principales del proyecto y cómo se relacionan entre sí.

```
                    ┌──────────────────────────────────────┐
                    │       BackgammonGame                 │
                    │  (Coordinador del juego)             │
                    ├──────────────────────────────────────┤
                    │  ATRIBUTOS:                          │
                    │  - __jugador1__: Jugador             │
                    │  - __jugador2__: Jugador             │
                    │  - __tablero__: Tablero              │
                    │  - __dados__: Dados                  │
                    │  - __turno__: Jugador                │
                    ├──────────────────────────────────────┤
                    │  MÉTODOS:                            │
                    │  + tirar_dados()                     │
                    │  + mover_ficha()                     │
                    │  + cambiar_turno()                   │
                    │  + reingresar_ficha()                │
                    │  + realizar_bear_off()               │
                    │  + verificar_ganador()               │
                    └──────────┬───────────────────────────┘
                               │
                               │ usa/coordina
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │    Jugador       │  │     Tablero      │  │      Dados       │
  ├──────────────────┤  ├──────────────────┤  ├──────────────────┤
  │  ATRIBUTOS:      │  │  ATRIBUTOS:      │  │  ATRIBUTOS:      │
  │  - nombre: str   │  │  - contenedor    │  │  - dado1: int    │
  │  - color: str    │  │    [24 pos]      │  │  - dado2: int    │
  │                  │  │  - almacen_ficha │  │  - valores: list │
  │  MÉTODOS:        │  │    {"b":0,"n":0} │  │                  │
  │  + @property     │  │  - banco         │  │  MÉTODOS:        │
  │    nombre()      │  │    {"b":0,"n":0} │  │  + tirar_dado()  │
  │  + @property     │  │                  │  │  + usar_valor()  │
  │    color()       │  │  MÉTODOS:        │  │  + resetear()    │
  └──────────────────┘  │  + movimiento_   │  └──────────────────┘
                        │    valido()      │
                        │  + mover_        │
                        │    checker()     │
                        │  + bear_off()    │
                        │  + verificar_    │
                        │    ganador()     │
                        └──────────────────┘


  ┌──────────────────┐
  │      Ficha       │  (Poco usada en implementación actual)
  ├──────────────────┤
  │  ATRIBUTOS:      │
  │  - ficha: str    │
  │  - posicion: int │
  │                  │
  │  MÉTODOS:        │
  │  + get_ficha()   │
  │  + adentro_      │
  │    almacen()     │
  └──────────────────┘
```

**Leyenda:**
- 📦 **BackgammonGame**: Clase principal que coordina todo el juego
- 👤 **Jugador**: Guarda información del jugador (nombre y color)
- 🎲 **Dados**: Genera números aleatorios y gestiona valores disponibles
- 📋 **Tablero**: Mantiene las 24 posiciones y valida movimientos
- ⚫ **Ficha**: Representa una ficha individual (uso limitado)

**Relaciones:**
- BackgammonGame **usa** (composición) → Jugador, Tablero, Dados
- Todas las clases están relacionadas por **composición**, NO por herencia

**Ventajas de esta arquitectura:**

- ✅ **Separación de responsabilidades**: UI no conoce las reglas del juego
- ✅ **Testeable**: Puedo testear lógica sin UI
- ✅ **Mantenible**: Cambios en UI no afectan el modelo
- ✅ **Extensible**: Puedo agregar más UIs (web, móvil) fácilmente



## Conclusiones Finales

### Fortalezas del Diseño

1. ✅ **Separación clara de responsabilidades** entre componentes
2. ✅ **Alta cobertura de testing** (90%, 197 tests)
3. ✅ **Código legible y mantenible** con nomenclatura consistente
4. ✅ **Manejo robusto de errores** con excepciones específicas
5. ✅ **Arquitectura por capas** bien definida
6. ✅ **Documentación completa** y comentarios descriptivos

### Áreas de Mejora

1. ⚠️ **Dependency Inversion**: Implementar interfaces abstractas
2. ⚠️ **Interface Segregation**: Dividir BackgammonGame en clases más pequeñas
3. ⚠️ **Extensibilidad**: Facilitar agregado de nuevas reglas sin modificar código existente
4. ⚠️ **Testing de UI**: Aumentar cobertura de CLI y Pygame

### Lecciones Aprendidas

1. **Composición sobre herencia** simplifica el diseño
2. **Excepciones específicas** mejoran debugging
3. **Testing incremental** facilita desarrollo
4. **Separación de concerns** mejora mantenibilidad
5. **Documentación temprana** ahorra tiempo

### Próximos Pasos

Para evolucionar el proyecto hacia un diseño más profesional:

1. Refactorizar hacia **inyección de dependencias**
2. Implementar **patrón Strategy** para validaciones
3. Agregar **logging** para debugging
4. Implementar **persistencia** (guardar/cargar partidas)
5. Mejorar **cobertura de UI** con mocks

---

**Documento elaborado por:** Santiago Ariel Martinez  
**Fecha de elaboración:** 31 de Octubre de 2025  
**Versión del documento:** 1.0  
**Estado del proyecto:** Versión 1.0.0 - Producción