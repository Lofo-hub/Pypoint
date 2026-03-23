from config import Config
import pygame


class Renderer:
    def __init__(self, game):
        pygame.init()
        self.config = game.config
        self.screen = pygame.display.set_mode(
    (self.config.screen_width, self.config.screen_height),
    pygame.RESIZABLE   # ← ajoute ce flag
)
        pygame.display.set_caption("TEST Point")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)    # ← ici
        self.font_small = pygame.font.SysFont(None, 22)  # ← pour le canon
    def draw_grid(self):
        self.screen.fill(self.config.bg_color)
        for i in range(self.config.rows + 1):
            pygame.draw.line(self.screen, self.config.grid_color, (self.config.padding, self.config.padding + i * self.config.cell_size), (self.config.screen_width - self.config.padding, self.config.padding + i * self.config.cell_size))
        for j in range(self.config.cols + 1):
            pygame.draw.line(self.screen, self.config.grid_color, (self.config.padding + j * self.config.cell_size, self.config.padding), (self.config.padding + j * self.config.cell_size, self.config.screen_height - self.config.padding))
    def draw_pieces(self, board):
        for i in range(self.config.rows):
            for j in range(self.config.cols):
                if board[i][j] == 0:
                    continue
                if board[i][j] == 1:
                    color = self.config.p1_color
                elif board[i][j] == 2:
                    color = self.config.p2_color
                pygame.draw.circle(self.screen, color, (self.config.padding + j * self.config.cell_size + self.config.cell_size // 2, self.config.padding + i * self.config.cell_size + self.config.cell_size // 2), self.config.cell_size // 2 - 2)
    def draw_status(self, game):
        y_scores = self.config.screen_height - self.config.padding - 25  # ligne basse
        y_statut = self.config.screen_height - self.config.padding - 60  # ligne haute

        # Ligne haute — statut/canon
        if game.game_over:
            text = f"Game Over! {game.winner}"
        elif game.canon_actif:
            text = f"🎯 Canon actif | Ligne: {game.canon_row} | Jauge: {game.canon_jauge}"
        else:
            text = f"Joueur {game.current_player} joue"
        
        surface_statut = self.font.render(text, True, self.config.text_color)
        x_centre = (self.config.screen_width - surface_statut.get_width()) // 2
        self.screen.blit(surface_statut, (x_centre, y_statut))

        # Ligne basse — scores
        # Score J1 à gauche
        surface_j1 = self.font.render(f"J1 : {game.score_j1} pts", True, self.config.p1_color)
        self.screen.blit(surface_j1, (self.config.padding, y_scores))

        # Score J2 à droite
        surface_j2 = self.font.render(f"J2 : {game.score_j2} pts", True, self.config.p2_color)
        x_j2 = self.config.screen_width - self.config.padding - surface_j2.get_width()
        self.screen.blit(surface_j2, (x_j2, y_scores))
      
    def draw(self, game):
        self.draw_grid()
        self.draw_pieces(game.board)
        self.draw_colored_lines(game)
        self.draw_canon(game)
        self.draw_status(game)
        pygame.display.flip()
    def draw_canon(self, game):
        if not game.canon_actif:
            return
        y = self.config.padding + game.canon_row * self.config.cell_size
        pygame.draw.line(self.screen, (180, 50, 50),
            (self.config.padding, y),
            (self.config.screen_width - self.config.padding, y), 1)

        # Corps du canon
        canon_x = self.config.screen_width - self.config.padding - 20   
        canon_y = y - 8
        pygame.draw.rect(self.screen, (80, 50, 20), (canon_x, canon_y, 18, 16), border_radius=3)

        pygame.draw.rect(self.screen, (60, 35, 10), (canon_x + 14, canon_y + 4, 10, 8), border_radius=2)

        self.font        
        self.font_small 
        jauge_text = self.font.render(f"jauge: {game.canon_jauge}", True, (50, 30, 10))
        self.screen.blit(jauge_text, (canon_x, canon_y - 16))

    def draw_colored_lines(self, game):
        for line in game.colored_lines:
            debut = line[0]
            fin = line[-1]
            x1 = self.config.padding + debut[1] * self.config.cell_size + self.config.cell_size // 2
            y1 = self.config.padding + debut[0] * self.config.cell_size + self.config.cell_size // 2
            x2 = self.config.padding + fin[1] * self.config.cell_size + self.config.cell_size // 2
            y2 = self.config.padding + fin[0] * self.config.cell_size + self.config.cell_size // 2
            pygame.draw.line(self.screen, (255, 215, 0), (x1, y1), (x2, y2), 4)
