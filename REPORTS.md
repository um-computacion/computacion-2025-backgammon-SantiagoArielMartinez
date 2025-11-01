# Automated Reports
## Coverage Report
```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
assets/__init__.py           0      0   100%
cli/__init__.py              0      0   100%
cli/cli.py                  97     18    81%   77-78, 82-84, 106, 118-131, 135-136
core/__init__.py             0      0   100%
core/backgammongame.py     112     10    91%   102-103, 152-153, 194, 199-201, 214-215
core/board.py              100      0   100%
core/checkers.py            14      0   100%
core/dice.py                27      0   100%
core/exceptions.py           6      0   100%
core/player.py              21      1    95%   40
pygame_ui/__init__.py        0      0   100%
------------------------------------------------------
TOTAL                      377     29    92%

```
## Pylint Report
```text
************* Module core.backgammongame
core/backgammongame.py:234:0: C0305: Trailing newlines (trailing-newlines)
core/backgammongame.py:191:4: R0912: Too many branches (13/12) (too-many-branches)
************* Module core.board
core/board.py:44:4: R0911: Too many return statements (8/6) (too-many-return-statements)
************* Module cli.cli
cli/cli.py:138:0: C0305: Trailing newlines (trailing-newlines)
cli/cli.py:61:8: C0415: Import outside toplevel (core.exceptions.NoEsTuTurno, core.exceptions.SinDados, core.exceptions.PosicionInvalida, core.exceptions.PosicionVacia) (import-outside-toplevel)
************* Module pygame_ui.pygame_ui
pygame_ui/pygame_ui.py:19:0: C0301: Line too long (564/100) (line-too-long)
pygame_ui/pygame_ui.py:23:0: C0301: Line too long (347/100) (line-too-long)
pygame_ui/pygame_ui.py:25:0: C0301: Line too long (494/100) (line-too-long)
pygame_ui/pygame_ui.py:26:0: C0301: Line too long (506/100) (line-too-long)
pygame_ui/pygame_ui.py:27:0: C0301: Line too long (510/100) (line-too-long)
pygame_ui/pygame_ui.py:31:0: C0301: Line too long (305/100) (line-too-long)
pygame_ui/pygame_ui.py:32:0: C0301: Line too long (308/100) (line-too-long)
pygame_ui/pygame_ui.py:45:0: C0301: Line too long (214/100) (line-too-long)
pygame_ui/pygame_ui.py:46:0: C0301: Line too long (215/100) (line-too-long)
pygame_ui/pygame_ui.py:47:0: C0301: Line too long (326/100) (line-too-long)
pygame_ui/pygame_ui.py:50:0: C0301: Line too long (122/100) (line-too-long)
pygame_ui/pygame_ui.py:51:0: C0301: Line too long (404/100) (line-too-long)
pygame_ui/pygame_ui.py:59:0: C0301: Line too long (160/100) (line-too-long)
pygame_ui/pygame_ui.py:60:0: C0301: Line too long (334/100) (line-too-long)
pygame_ui/pygame_ui.py:66:0: C0301: Line too long (423/100) (line-too-long)
pygame_ui/pygame_ui.py:71:0: C0301: Line too long (136/100) (line-too-long)
pygame_ui/pygame_ui.py:72:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/pygame_ui.py:76:0: C0301: Line too long (119/100) (line-too-long)
pygame_ui/pygame_ui.py:77:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/pygame_ui.py:78:0: C0301: Line too long (277/100) (line-too-long)
pygame_ui/pygame_ui.py:84:0: C0301: Line too long (119/100) (line-too-long)
pygame_ui/pygame_ui.py:85:0: C0301: Line too long (242/100) (line-too-long)
pygame_ui/pygame_ui.py:86:0: C0301: Line too long (221/100) (line-too-long)
pygame_ui/pygame_ui.py:112:0: C0301: Line too long (105/100) (line-too-long)
pygame_ui/pygame_ui.py:113:0: C0301: Line too long (108/100) (line-too-long)
pygame_ui/pygame_ui.py:122:0: C0301: Line too long (103/100) (line-too-long)
pygame_ui/pygame_ui.py:126:0: C0301: Line too long (123/100) (line-too-long)
pygame_ui/pygame_ui.py:128:0: C0301: Line too long (143/100) (line-too-long)
pygame_ui/pygame_ui.py:134:0: C0301: Line too long (116/100) (line-too-long)
pygame_ui/pygame_ui.py:161:0: C0301: Line too long (110/100) (line-too-long)
pygame_ui/pygame_ui.py:163:0: C0301: Line too long (121/100) (line-too-long)
pygame_ui/pygame_ui.py:170:0: C0301: Line too long (187/100) (line-too-long)
pygame_ui/pygame_ui.py:173:0: C0301: Line too long (105/100) (line-too-long)
pygame_ui/pygame_ui.py:174:0: C0301: Line too long (101/100) (line-too-long)
pygame_ui/pygame_ui.py:179:0: C0301: Line too long (101/100) (line-too-long)
pygame_ui/pygame_ui.py:181:0: C0301: Line too long (103/100) (line-too-long)
pygame_ui/pygame_ui.py:184:0: C0301: Line too long (106/100) (line-too-long)
pygame_ui/pygame_ui.py:195:0: C0301: Line too long (129/100) (line-too-long)
pygame_ui/pygame_ui.py:202:0: C0301: Line too long (128/100) (line-too-long)
pygame_ui/pygame_ui.py:216:0: C0301: Line too long (101/100) (line-too-long)
pygame_ui/pygame_ui.py:220:0: C0301: Line too long (105/100) (line-too-long)
pygame_ui/pygame_ui.py:222:0: C0301: Line too long (104/100) (line-too-long)
pygame_ui/pygame_ui.py:228:0: C0301: Line too long (114/100) (line-too-long)
pygame_ui/pygame_ui.py:19:8: C0103: Attribute name "COLOR_FONDO_GENERAL" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:52: C0103: Attribute name "COLOR_TRI_A" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:87: C0103: Attribute name "COLOR_TRI_B" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:123: C0103: Attribute name "COLOR_BARRA_CENTRAL" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:167: C0103: Attribute name "COLOR_BARRA_LATERAL" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:211: C0103: Attribute name "COLOR_BORDE" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:244: C0103: Attribute name "COLOR_LINEA_FICHA" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:280: C0103: Attribute name "COLOR_FICHA_BLANCA" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:323: C0103: Attribute name "COLOR_FICHA_NEGRA" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:362: C0103: Attribute name "COLOR_TEXTO_GENERAL" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:400: C0103: Attribute name "COLOR_MENSAJE_ERROR" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:440: C0103: Attribute name "COLOR_MENSAJE_INFO" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:479: C0103: Attribute name "COLOR_HIGHLIGHT" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:19:524: C0103: Attribute name "COLOR_SELECTED" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:7:0: R0902: Too many instance attributes (21/7) (too-many-instance-attributes)
pygame_ui/pygame_ui.py:19:52: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:23:54: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:25:70: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:26:82: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:27:120: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:30:31: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:31:29: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:32:94: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:35:4: R0914: Too many local variables (20/15) (too-many-locals)
pygame_ui/pygame_ui.py:42:45: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:44:25: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:45:96: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:46:38: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:47:40: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:50:70: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:51:268: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:58:30: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:59:85: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:60:38: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:66:102: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:78:20: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:82:32: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:83:57: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:84:108: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:85:36: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:94:8: C0103: Attribute name "ANCHO_PANTALLA" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:94:29: C0103: Attribute name "ALTO_PANTALLA" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:110:8: C0103: Attribute name "COLOR_BOTON" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:111:8: C0103: Attribute name "COLOR_BOTON_TEXTO" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/pygame_ui.py:90:0: R0902: Too many instance attributes (17/7) (too-many-instance-attributes)
pygame_ui/pygame_ui.py:118:53: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:129:53: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:120:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
pygame_ui/pygame_ui.py:130:36: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:149:41: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:155:40: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:163:83: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:173:45: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:186:43: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:188:39: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:144:4: R0912: Too many branches (21/12) (too-many-branches)
pygame_ui/pygame_ui.py:193:35: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:195:20: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:232:39: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:233:23: C0321: More than one statement on a single line (multiple-statements)
pygame_ui/pygame_ui.py:90:0: R0903: Too few public methods (1/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 8.29/10


```
