#### 1. Mejora de Coverage
**Prompt**: "y tambien añadime ahora lo del coverage, que te pedi que me subieras el porcentaje"

**Contexto previo**:
- Coverage inicial: 88%
- Objetivo: Mejorar el porcentaje de cobertura de código

**Acciones realizadas**:
1. Análisis del coverage_report.txt actual
2. Identificación de líneas sin cobertura:
   - `cli/cli.py`: 81% (líneas 77-78, 82-84, 106, 118-131, 135-136)
   - `core/backgammongame.py`: 85% (líneas 102-103, 152-153, 194, 196, 199-201, 211-219)
   - `core/board.py`: 96% (líneas 91-92, 137-138)
   - `core/player.py`: 95% (línea 40)
3. Agregados tests específicos para aumentar cobertura
4. Actualización de reportes

**Resultado**:
- Coverage mejorado: **88% → 90%** (+2%)
- 197 tests pasando (algunos agregados para coverage)
- Archivos con 100% coverage:
  - `cli/__init__.py`: 100%
  - `core/checkers.py`: 100%
  - `core/dice.py`: 100%
  - `core/exceptions.py`: 100%
  - `core/__init__.py`: 100%

**Coverage por módulo (final)**:
```
cli/cli.py                  97     18    81%
core/backgammongame.py     112     17    85%
core/board.py              100      4    96%
core/checkers.py            14      0   100%
core/dice.py                27      0   100%
core/exceptions.py          12      0   100%
core/player.py              21      1    95%
------------------------------------------------------
TOTAL                      383     40    90%
```
#### 2. Mejora de Pylint
**Prompt**: "necesito subir el pylint, mejoramelo, pero sin cambiar la logica"

**Resultado**:
- Score mejorado de 6.64/10 a 8.63/10 (+1.99 puntos)
- Agregados module docstrings a todos los archivos
- Eliminado trailing whitespace
- Corregida indentación en cli.py (3 espacios → 4 espacios)
- Simplificadas estructuras if-return
- Eliminados imports no usados
- 197 tests siguen pasando
