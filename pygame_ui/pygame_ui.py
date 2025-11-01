"""Interfaz gráfica del juego de Backgammon usando Pygame."""
import sys
import pygame
from core.backgammongame import BackgammonGame


class BoardRenderer:
    """Renderiza el tablero de Backgammon en Pygame."""

    def __init__(self, pantalla, alto_tablero=None):
        """Inicializa el renderizador del tablero."""
        self.pantalla = pantalla
        self.ancho = self.pantalla.get_width()
        self.alto = alto_tablero if alto_tablero else self.pantalla.get_height()
        self.ancho_triangulo = self.ancho // 14
        self.ancho_barra = self.ancho_triangulo
        self.alto_triangulo = self.alto // 2.2
        self.radio_ficha = (self.ancho_triangulo // 2) - 8
        self.COLOR_FONDO_GENERAL = (245, 239, 230); self.COLOR_TRI_A = (170, 120, 90); self.COLOR_TRI_B = (210, 170, 130); self.COLOR_BARRA_CENTRAL = (180, 140, 100); self.COLOR_BARRA_LATERAL = (200, 180, 150); self.COLOR_BORDE = (60, 60, 60); self.COLOR_LINEA_FICHA = (0, 0, 0); self.COLOR_FICHA_BLANCA = (245, 245, 245); self.COLOR_FICHA_NEGRA = (30, 30, 30); self.COLOR_TEXTO_GENERAL = (0, 0, 0); self.COLOR_MENSAJE_ERROR = (200, 0, 0); self.COLOR_MENSAJE_INFO = (0, 100, 0); self.COLOR_HIGHLIGHT = (100, 200, 100, 180); self.COLOR_SELECTED = (255, 200, 0, 180)

    def dibujar_tablero(self):
        """Dibuja el tablero base con triángulos y barras."""
        self.pantalla.fill(self.COLOR_FONDO_GENERAL); x_barra_centro = (self.ancho / 2) - (self.ancho_barra / 2); pygame.draw.rect(self.pantalla, self.COLOR_BARRA_CENTRAL, pygame.Rect(x_barra_centro, 0, self.ancho_barra, self.alto)); pygame.draw.rect(self.pantalla, self.COLOR_BORDE, pygame.Rect(x_barra_centro, 0, self.ancho_barra, self.alto), 2)
        for i in range(6):
            x_izq = self.ancho_barra // 2 + i * self.ancho_triangulo; pygame.draw.polygon(self.pantalla, self.COLOR_TRI_A if (i % 2 == 0) else self.COLOR_TRI_B, [(x_izq, 0), (x_izq + self.ancho_triangulo, 0), (x_izq + self.ancho_triangulo // 2, self.alto_triangulo)]); pygame.draw.polygon(self.pantalla, self.COLOR_TRI_B if (i % 2 == 0) else self.COLOR_TRI_A, [(x_izq, self.alto), (x_izq + self.ancho_triangulo, self.alto), (x_izq + self.ancho_triangulo // 2, self.alto - self.alto_triangulo)])
            x_der = x_barra_centro + self.ancho_barra + i * self.ancho_triangulo; pygame.draw.polygon(self.pantalla, self.COLOR_TRI_B if (i % 2 == 0) else self.COLOR_TRI_A, [(x_der, 0), (x_der + self.ancho_triangulo, 0), (x_der + self.ancho_triangulo // 2, self.alto_triangulo)]); pygame.draw.polygon(self.pantalla, self.COLOR_TRI_A if (i % 2 == 0) else self.COLOR_TRI_B, [(x_der, self.alto), (x_der + self.ancho_triangulo, self.alto), (x_der + self.ancho_triangulo // 2, self.alto - self.alto_triangulo)])
        pygame.draw.rect(self.pantalla, self.COLOR_BARRA_LATERAL, pygame.Rect(0, 0, self.ancho_barra // 2, self.alto)); pygame.draw.rect(self.pantalla, self.COLOR_BORDE, pygame.Rect(0, 0, self.ancho_barra // 2, self.alto), 2); pygame.draw.rect(self.pantalla, self.COLOR_BARRA_LATERAL, pygame.Rect(self.ancho - self.ancho_barra // 2, 0, self.ancho_barra // 2, self.alto)); pygame.draw.rect(self.pantalla, self.COLOR_BORDE, pygame.Rect(self.ancho - self.ancho_barra // 2, 0, self.ancho_barra // 2, self.alto), 2)

    def _get_coords_from_point(self, punto_idx):
        punto = punto_idx + 1; x_barra_pos = self.ancho / 2 - self.ancho_barra / 2
        if 1 <= punto <= 12: y_base, step = self.radio_ficha + 5, (self.radio_ficha * 2) + 2; x = x_barra_pos + self.ancho_barra + (6 - punto) * self.ancho_triangulo + self.ancho_triangulo // 2 if 1 <= punto <= 6 else self.ancho_barra // 2 + (12 - punto) * self.ancho_triangulo + self.ancho_triangulo // 2
        else: y_base, step = self.alto - self.radio_ficha - 5, -((self.radio_ficha * 2) + 2); x = self.ancho_barra // 2 + (punto - 13) * self.ancho_triangulo + self.ancho_triangulo // 2 if 13 <= punto <= 18 else x_barra_pos + self.ancho_barra + (punto - 19) * self.ancho_triangulo + self.ancho_triangulo // 2
        return int(x), int(y_base), int(step)

    def dibujar_fichas(self, estado_tablero, seleccionado=None, movimientos_validos=None):
        """Dibuja las fichas en el tablero."""
        fuente, max_visibles = pygame.font.Font(None, 22), 5
        if seleccionado is not None and isinstance(seleccionado, int):
            self._resaltar_triangulo(seleccionado, self.COLOR_SELECTED)
        if movimientos_validos:
            for destino, _ in movimientos_validos:
                if isinstance(destino, int): self._resaltar_triangulo(destino, self.COLOR_HIGHLIGHT)
        for punto_idx, cell in enumerate(estado_tablero):
            if not cell: continue
            color = self.COLOR_FICHA_BLANCA if cell[0] == "blanco" else self.COLOR_FICHA_NEGRA; cantidad = len(cell); x, y_base, step = self._get_coords_from_point(punto_idx); visibles = min(cantidad, max_visibles)
            for i in range(visibles): y = y_base + step * i; pygame.draw.circle(self.pantalla, color, (x, y), self.radio_ficha); pygame.draw.circle(self.pantalla, self.COLOR_LINEA_FICHA, (x, y), self.radio_ficha, 2)
            if cantidad > max_visibles: y_texto = y_base + step * (max_visibles - 1); texto_color = self.COLOR_TEXTO_GENERAL if color == self.COLOR_FICHA_BLANCA else self.COLOR_FICHA_BLANCA; texto = fuente.render(f"+{cantidad - max_visibles}", True, texto_color); self.pantalla.blit(texto, texto.get_rect(center=(x, y_texto)))

    def _resaltar_triangulo(self, punto_idx, color):
        x_centro, y_base, _ = self._get_coords_from_point(punto_idx); x_esquina_izq = x_centro - self.ancho_triangulo // 2
        pts = [(x_esquina_izq, 0), (x_esquina_izq + self.ancho_triangulo, 0), (x_centro, self.alto_triangulo)] if y_base < self.alto / 2 else [(x_esquina_izq, self.alto), (x_esquina_izq + self.ancho_triangulo, self.alto), (x_centro, self.alto - self.alto_triangulo)]; surf = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA); pygame.draw.polygon(surf, color, pts); self.pantalla.blit(surf, (0, 0))

    def dibujar_barra(self, almacen):
        """Dibuja la barra central con fichas capturadas."""
        x_centro = self.ancho // 2
        for color in ["blanco", "negro"]:
            cantidad = almacen.get(color, 0)
            if cantidad == 0: continue
            y_start = (self.alto / 4) if color == "blanco" else (self.alto * 3 / 4); step = -self.radio_ficha * 2 if color == "blanco" else self.radio_ficha * 2
            for j in range(cantidad): y = y_start + j * step; ficha_color = self.COLOR_FICHA_BLANCA if color == "blanco" else self.COLOR_FICHA_NEGRA; pygame.draw.circle(self.pantalla, ficha_color, (x_centro, int(y)), self.radio_ficha); pygame.draw.circle(self.pantalla, self.COLOR_LINEA_FICHA, (x_centro, int(y)), self.radio_ficha, 2)

    def dibujar_barra_lateral(self, banco):
        """Dibuja la barra lateral con fichas sacadas del tablero."""
        fuente, x_centro = pygame.font.Font(None, 36), self.ancho - self.ancho_barra // 4
        for color, y_pos in [("blanco", 40), ("negro", self.alto - 40)]:
            texto_color = self.COLOR_TEXTO_GENERAL if color == "blanco" else self.COLOR_FICHA_BLANCA; fondo_color = self.COLOR_FICHA_BLANCA if color == "blanco" else self.COLOR_FICHA_NEGRA; texto = fuente.render(f"{banco.get(color, 0)}", True, texto_color); rect = texto.get_rect(center=(x_centro, y_pos)); pygame.draw.rect(self.pantalla, fondo_color, rect.inflate(16, 10), border_radius=6); self.pantalla.blit(texto, rect)

    def dibujar_info_turno(self, turno, dados, mensaje):
        """Dibuja información del turno, dados disponibles y mensajes."""
        fuente_grande, fuente_media = pygame.font.Font(None, 36), pygame.font.Font(None, 28)
        self.pantalla.blit(fuente_grande.render(f"Turno de: {turno}", True, self.COLOR_TEXTO_GENERAL), (self.ancho_barra // 2 + 10, 10))
        
        # Mostrar dados disponibles
        if dados:
            dados_texto = f"Dados disponibles: {dados}"
            self.pantalla.blit(fuente_media.render(dados_texto, True, (0, 100, 200)), (self.ancho_barra // 2 + 10, 50))
        
        if mensaje: color = self.COLOR_MENSAJE_ERROR if "Error" in mensaje or "válido" in mensaje else self.COLOR_MENSAJE_INFO; texto_msg = fuente_media.render(mensaje, True, color); self.pantalla.blit(texto_msg, texto_msg.get_rect(midbottom=(self.ancho // 2, self.alto - 20)))

    def obtener_punto_desde_click(self, pos):
        """Convierte coordenadas de click en número de punto del tablero."""
        x_click, y_click = pos; x_barra_start = (self.ancho / 2) - (self.ancho_barra / 2)
        if x_click > self.ancho - self.ancho_barra // 2: return 'bear_off'
        if x_click < self.ancho_barra // 2 or x_barra_start <= x_click <= x_barra_start + self.ancho_barra: return None
        if y_click < self.alto / 2: punto = 6 - int((x_click - (x_barra_start + self.ancho_barra)) // self.ancho_triangulo) if x_click > x_barra_start + self.ancho_barra else 12 - int((x_click - self.ancho_barra // 2) // self.ancho_triangulo)
        else: punto = 19 + int((x_click - (x_barra_start + self.ancho_barra)) // self.ancho_triangulo) if x_click > x_barra_start + self.ancho_barra else 13 + int((x_click - self.ancho_barra // 2) // self.ancho_triangulo)
        return (punto - 1) if 1 <= punto <= 24 else None


class PygameUI:
    """Interfaz gráfica principal del juego usando Pygame."""
    def __init__(self):
        pygame.init()
        self.ANCHO_PANTALLA, self.ALTO_PANTALLA = 1200, 750
        self.pantalla = pygame.display.set_mode((self.ANCHO_PANTALLA, self.ALTO_PANTALLA))
        pygame.display.set_caption("Backgammon")
        self.clock = pygame.time.Clock()
        self.game = BackgammonGame(
            input("Jugador 1 (Negras, van 24 -> 1): "),
            input("Jugador 2 (Blancas, van 1 -> 24): ")
        )
        self.renderer = BoardRenderer(self.pantalla, alto_tablero=self.ALTO_PANTALLA)
        self.running = True
        self.origen_seleccionado = None
        self.movimientos_validos = []
        self.mensaje_ui = f"Turno de {self.game.get_turno_actual().nombre}. ¡Tira los dados!"
        self.dados_tirados = False
        self.mensaje_timer = 0
        self.fuente_boton = pygame.font.Font(None, 32)
        self.COLOR_BOTON = (80, 130, 180)
        self.COLOR_BOTON_TEXTO = (255, 255, 255)
        self.rect_tirar_dados = pygame.Rect(self.ANCHO_PANTALLA - 220, self.ALTO_PANTALLA - 120, 200, 50)
        self.rect_finalizar_turno = pygame.Rect(self.ANCHO_PANTALLA - 220, self.ALTO_PANTALLA - 60, 200, 50)

    def _obtener_movimientos_validos(self, pos_inicial):
        jugador, valid_moves = self.game.get_turno_actual(), []
        dados = self.game.__dados__.valores_dados()
        if self.game.hay_fichas_en_almacen(jugador): return []

        if self.game.get_tablero().bear_off_permitido(jugador.color):
            for dado in dados:
                distancia_real = (24 - pos_inicial) if jugador.color == "blanco" else (pos_inicial + 1)
                if dado >= distancia_real:
                    puede_sacar = True
                    if dado > distancia_real:
                        rango_superior = range(18, pos_inicial) if jugador.color == "blanco" else range(pos_inicial + 1, 6)
                        for i in rango_superior:
                            if self.game.get_tablero().estado_tablero()[i] and self.game.get_tablero().estado_tablero()[i][0] == jugador.color:
                                puede_sacar = False; break
                    if puede_sacar: valid_moves.append(('bear_off', dado))

        for dado in dados:
            pos_final = pos_inicial + dado if jugador.color == "blanco" else pos_inicial - dado
            if (0 <= pos_final < 24) and self.game.get_tablero().movimiento_valido(pos_inicial, pos_final, jugador):
                valid_moves.append((pos_final, dado))
        return list(set(valid_moves))

    def _finalizar_turno_ui(self):
        self.game.finalizar_turno()
        self.dados_tirados, self.origen_seleccionado, self.movimientos_validos = False, None, []
        self.mensaje_ui = f"Turno de {self.game.get_turno_actual().nombre}. ¡Tira los dados!"
        self.mensaje_timer = 300

    def _handle_click(self, pos):
        jugador_actual = self.game.get_turno_actual()

        if not self.dados_tirados:
            if self.rect_tirar_dados.collidepoint(pos):
                self.game.tirar_dados(); self.dados_tirados = True
                self.mensaje_ui = f"Mueve {jugador_actual.nombre}."
                self.mensaje_timer = 180
            return

        if self.dados_tirados and self.rect_finalizar_turno.collidepoint(pos):
            self._finalizar_turno_ui(); return

        punto_click = self.renderer.obtener_punto_desde_click(pos)

        if self.game.hay_fichas_en_almacen(jugador_actual):
            if isinstance(punto_click, int):
                dado_necesario = (punto_click + 1) if jugador_actual.color == "blanco" else (24 - punto_click)
                if dado_necesario in self.game.__dados__.valores_dados():
                    if self.game.reingresar_ficha(jugador_actual, dado_necesario): self.mensaje_ui = "Ficha reingresada."
                    else: self.mensaje_ui = "Punto de entrada bloqueado."
                    self.mensaje_timer = 120
            else: self.mensaje_ui = "Debes reingresar tu ficha."
            return

        if self.origen_seleccionado is None:
            if isinstance(punto_click, int) and self.game.get_tablero().estado_tablero()[punto_click] and self.game.get_tablero().estado_tablero()[punto_click][0] == jugador_actual.color:
                self.origen_seleccionado = punto_click
                self.movimientos_validos = self._obtener_movimientos_validos(punto_click)
                if self.movimientos_validos: self.mensaje_ui = f"Columna {punto_click + 1} seleccionada."
                else: self.mensaje_ui, self.origen_seleccionado = "No hay movimientos válidos.", None
                self.mensaje_timer = 180
        else:
            movimiento_exitoso = False
            for destino, dado in self.movimientos_validos:
                if (destino == 'bear_off' and punto_click == 'bear_off') or (destino == punto_click):
                    if destino == 'bear_off':
                        if self.game.realizar_bear_off(jugador_actual, self.origen_seleccionado, dado):
                            self.mensaje_ui, movimiento_exitoso = "¡Ficha fuera!", True
                    else:
                        if self.game.mover_ficha(jugador_actual, self.origen_seleccionado, destino, dado):
                            self.mensaje_ui, movimiento_exitoso = "Movimiento exitoso.", True
                    if movimiento_exitoso: break

            if not movimiento_exitoso: self.mensaje_ui = "Movimiento no válido."
            self.mensaje_timer = 120
            self.origen_seleccionado, self.movimientos_validos = None, []

    def _update_game_state(self):
        if self.mensaje_timer > 0: self.mensaje_timer -= 1
        ganador = self.game.verificar_ganador()
        if ganador: self.mensaje_ui = f"¡GANADOR: {ganador}!"; self._draw(); pygame.time.wait(5000); self.running = False; return
        if self.dados_tirados and not self.game.__dados__.valores_dados():
            self._finalizar_turno_ui()

    def _draw(self):
        """Dibuja toda la interfaz del juego."""
        self.renderer.dibujar_tablero()
        self.renderer.dibujar_fichas(self.game.get_tablero().__contenedor__, self.origen_seleccionado, self.movimientos_validos)
        self.renderer.dibujar_barra(self.game.get_tablero().estado_almacenamiento())
        self.renderer.dibujar_barra_lateral(getattr(self.game.get_tablero(), '__banco__', {}))

        dados = self.game.__dados__.valores_dados() if self.dados_tirados else []
        mensaje = self.mensaje_ui if self.mensaje_timer > 0 else ""
        self.renderer.dibujar_info_turno(self.game.get_turno_actual().nombre, dados, mensaje)

        self._draw_buttons()
        pygame.display.flip()

    def _draw_buttons(self):
        """Dibuja los botones de la interfaz."""
        if not self.dados_tirados:
            pygame.draw.rect(self.pantalla, self.COLOR_BOTON, self.rect_tirar_dados, border_radius=8)
            texto_surf = self.fuente_boton.render("Tirar Dados", True, self.COLOR_BOTON_TEXTO)
            self.pantalla.blit(texto_surf, texto_surf.get_rect(center=self.rect_tirar_dados.center))
        if self.dados_tirados:
            pygame.draw.rect(self.pantalla, self.COLOR_BOTON, self.rect_finalizar_turno, border_radius=8)
            texto_surf = self.fuente_boton.render("Finalizar Turno", True, self.COLOR_BOTON_TEXTO)
            self.pantalla.blit(texto_surf, texto_surf.get_rect(center=self.rect_finalizar_turno.center))

    def run(self):
        """Ejecuta el loop principal del juego."""
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key in (pygame.K_ESCAPE, pygame.K_q)):
                    self.running = False
                elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    self._handle_click(e.pos)
            self._update_game_state(); self._draw(); self.clock.tick(60)
        pygame.quit(); sys.exit()

if __name__ == "__main__":
    ui = PygameUI()
    ui.run()
