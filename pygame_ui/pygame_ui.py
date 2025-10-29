"""
Módulo de interfaz gráfica con Pygame para el juego de Backgammon.
"""
import sys
import pygame_ui
from core.backgammongame import BackgammonGame

# Configuración
WIDTH, HEIGHT = 1000, 700
BG_COLOR = (139, 90, 43)
POINT_COLOR_1, POINT_COLOR_2 = (205, 133, 63), (101, 67, 33)
WHITE_CHECKER, BLACK_CHECKER = (255, 255, 255), (50, 50, 50)
BORDER_COLOR, TEXT_COLOR = (70, 40, 20), (255, 255, 255)
BOARD_MARGIN, POINT_WIDTH, POINT_HEIGHT = 50, 60, 200
CHECKER_RADIUS, BAR_WIDTH = 25, 50

def draw_point(screen, x, y, width, height, color, direction='up'):
    """Dibuja un punto triangular del tablero"""
    if direction == 'up':
        points = [(x, y), (x + width // 2, y + height), (x + width, y)]
    else:
        points = [(x, y + height), (x + width // 2, y), (x + width, y + height)]
    pygame_ui.draw.polygon(screen, color, points)
    pygame_ui.draw.polygon(screen, BORDER_COLOR, points, 2)

def draw_checker(screen, x, y, color):
    """Dibuja una ficha"""
    pygame_ui.draw.circle(screen, color, (x, y), CHECKER_RADIUS)
    pygame_ui.draw.circle(screen, BORDER_COLOR, (x, y), CHECKER_RADIUS, 2)

def render_board(screen, game, font):
    """Renderiza el tablero"""
    screen.fill(BG_COLOR)
    hitmap = {}
    tablero = game.get_tablero().estado_tablero()
    
    for i in range(24):
        is_top = i >= 12
        col = (23 - i) if is_top else i
        x = BOARD_MARGIN + BAR_WIDTH + (col % 6) * POINT_WIDTH
        if col >= 6:
            x += POINT_WIDTH * 6
        y = BOARD_MARGIN if is_top else HEIGHT - BOARD_MARGIN - POINT_HEIGHT
        direction = 'down' if is_top else 'up'
        
        color = POINT_COLOR_1 if i % 2 == 0 else POINT_COLOR_2
        draw_point(screen, x, y, POINT_WIDTH, POINT_HEIGHT, color, direction)
        hitmap[i] = pygame_ui.Rect(x, y, POINT_WIDTH, POINT_HEIGHT)
        
        if tablero[i]:
            checker_color = WHITE_CHECKER if tablero[i][0] == "blanco" else BLACK_CHECKER
            for j in range(min(len(tablero[i]), 5)):
                cy = y + 30 + j * 55 if direction == 'down' else y + POINT_HEIGHT - 30 - j * 55
                draw_checker(screen, x + POINT_WIDTH // 2, cy, checker_color)
    
    screen.blit(font.render(game.obtener_turno(), True, TEXT_COLOR), (WIDTH - 250, 20))
    return hitmap

def hit_test(hitmap, pos):
    """Detecta clic"""
    for idx, rect in hitmap.items():
        if rect.collidepoint(pos):
            return idx
    return None

def main():
    """Función principal"""
    pygame_ui.init()
    screen = pygame_ui.display.set_mode((WIDTH, HEIGHT))
    pygame_ui.display.set_caption("Backgammon")
    clock = pygame_ui.time.Clock()
    font = pygame_ui.font.SysFont(None, 24)
    
    game = BackgammonGame(input("Jugador 1: "), input("Jugador 2: "))
    selected = None
    hitmap = {}
    
    while True:
        for e in pygame_ui.event.get():
            if e.type == pygame_ui.QUIT:
                pygame_ui.quit()
                sys.exit()
            elif e.type == pygame_ui.KEYDOWN and e.key == pygame_ui.K_ESCAPE:
                pygame_ui.quit()
                sys.exit()
            elif e.type == pygame_ui.KEYDOWN and e.key == pygame_ui.K_SPACE:
                game.tirar_dados()
            elif e.type == pygame_ui.MOUSEBUTTONDOWN:
                idx = hit_test(hitmap, e.pos)
                if idx is not None:
                    if selected is None:
                        selected = idx
                    else:
                        jugador = game.get_turno_actual()
                        dados = game.tirar_dados().valores_dados()
                        if dados:
                            game.mover_ficha(jugador, selected, idx, dados[0])
                        selected = None
        
        hitmap = render_board(screen, game, font)
        if selected is not None and selected in hitmap:
            pygame_ui.draw.rect(screen, (255, 255, 0), hitmap[selected], 3)
        pygame_ui.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()