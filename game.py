from config import Config


class Game:
    def __init__(self, config):  # ← reçoit config
        self.config = config     # ✅
        self.board = [[0] * self.config.cols for _ in range(self.config.rows)]
        self.current_player = 1
        self.game_over = False
        self.score_j1 = 0
        self.score_j2 = 0
        self.colored_lines = []
        self.canon_actif = False
        self.canon_row = 0
        self.canon_jauge = 1

    def place(self, row, col):
        if self.board[row][col] != 0 or self.game_over:
            return False
        self.board[row][col] = self.current_player
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
        return True
    def terminer(self):
        self.game_over = True
        if self.score_j1 > self.score_j2:
            self.winner = "Player 1"
        elif self.score_j2 > self.score_j1:
            self.winner = "Player 2"
        else:
            self.winner = "It's a tie!"
    def fire_canon(self, row, jauge):
        col = self.config.cols * jauge // 9
        adverse = 2 if self.current_player == 1 else 1
        touche = False

        if self.board[row][col] == adverse:
            self.board[row][col] = 0
            touche = True

        self.current_player = 2 if self.current_player == 1 else 1
        return touche