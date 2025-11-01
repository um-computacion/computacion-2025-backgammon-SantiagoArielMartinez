# Automated Reports
## Coverage Report
```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
assets/__init__.py           0      0   100%
cli/__init__.py              0      0   100%
cli/cli.py                  97     18    81%   77-78, 82-84, 106, 118-131, 135-136
core/__init__.py             0      0   100%
core/backgammongame.py     112     17    85%   102-103, 152-153, 194, 196, 199-201, 211-215, 217-219
core/board.py              100      4    96%   91-92, 137-138
core/checkers.py            14      0   100%
core/dice.py                27      0   100%
core/exceptions.py          12      0   100%
core/player.py              21      1    95%   40
pygame_ui/__init__.py        0      0   100%
------------------------------------------------------
TOTAL                      383     40    90%

```
## Pylint Report
```text
************* Module computacion-2025-backgammon-SantiagoArielMartinez.core.exceptions
core/exceptions.py:7:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:11:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:15:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:19:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:23:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/exceptions.py:27:4: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module computacion-2025-backgammon-SantiagoArielMartinez.core.board
core/board.py:188:0: C0304: Final newline missing (missing-final-newline)
core/board.py:4:0: E0401: Unable to import 'core.player' (import-error)
core/board.py:5:0: E0401: Unable to import 'core.exceptions' (import-error)
core/board.py:44:4: R0911: Too many return statements (8/6) (too-many-return-statements)
************* Module computacion-2025-backgammon-SantiagoArielMartinez.core.dice
core/dice.py:36:25: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:36:15: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module computacion-2025-backgammon-SantiagoArielMartinez.core.backgammongame
core/backgammongame.py:233:0: C0305: Trailing newlines (trailing-newlines)
core/backgammongame.py:5:0: E0401: Unable to import 'core.player' (import-error)
core/backgammongame.py:6:0: E0401: Unable to import 'core.board' (import-error)
core/backgammongame.py:7:0: E0401: Unable to import 'core.dice' (import-error)
core/backgammongame.py:8:0: E0401: Unable to import 'core.exceptions' (import-error)
core/backgammongame.py:191:4: R0912: Too many branches (13/12) (too-many-branches)
************* Module computacion-2025-backgammon-SantiagoArielMartinez.cli.cli
cli/cli.py:137:0: C0305: Trailing newlines (trailing-newlines)
cli/cli.py:4:0: E0401: Unable to import 'core.backgammongame' (import-error)
cli/cli.py:61:8: E0401: Unable to import 'core.exceptions' (import-error)
cli/cli.py:61:8: C0415: Import outside toplevel (core.exceptions.NoEsTuTurno, core.exceptions.SinDados, core.exceptions.PosicionInvalida, core.exceptions.PosicionVacia) (import-outside-toplevel)

------------------------------------------------------------------
Your code has been rated at 8.58/10

```

