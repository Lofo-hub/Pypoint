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
        if game.game_over:
            text = f"Game Over! {game.winner}"
        else:
            if game.canon_actif:
                text = f"Canon active! Player {game.current_player}'s turn (Row: {game.canon_row}, Jauge: {game.canon_jauge})"
            else:
                text = f"Player {game.current_player}'s turn"
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(text, True, self.config.text_color)
        self.screen.blit(text_surface, (self.config.padding, self.config.screen_height - self.config.padding - 40))
    def draw(self, game):
        self.draw_grid()
        self.draw_pieces(game.board)
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
        canon_x = self.config.screen_width - self.config.padding - 20  # ← dans la fenêtre
        canon_y = y - 8
        pygame.draw.rect(self.screen, (80, 50, 20), (canon_x, canon_y, 18, 16), border_radius=3)

        # Canon tube
        pygame.draw.rect(self.screen, (60, 35, 10), (canon_x + 14, canon_y + 4, 10, 8), border_radius=2)

        # Jauge texte
        self.font        # dans draw_status
        self.font_small  # dans draw_canon
        jauge_text = font.render(f"jauge: {game.canon_jauge}", True, (50, 30, 10))
        self.screen.blit(jauge_text, (canon_x, canon_y - 16))