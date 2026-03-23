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
        self.colored_cells = set()  

    def place(self, row, col):
        
        if self.board[row][col] != 0 or self.game_over:
            return False
        self.board[row][col] = self.current_player
        joueur_qui_a_joue = self.current_player
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
        win = self.check_win(row, col)
        if win:
            win_set = set(win)
            already_scored = False
            for existing_line in self.colored_lines:
                if len(set(win) & set(existing_line)) >= 4:
                    already_scored = True
                    break

            if not already_scored:
                self.colored_lines.append(win)
                self.colored_cells.update(set(win))
                if joueur_qui_a_joue == 1:
                    self.score_j1 += 1
                else:
                    self.score_j2 += 1
        return True
    def check_win(self, row, col):
        directions = [(0,1), (1,0), (1,1), (1,-1)]
        player = self.board[row][col]
        max_range = max(self.config.rows, self.config.cols)
        
        for dr, dc in directions:
            cells = [(row, col)]
            
            for i in range(1, max_range):  # ← toute la grille
                r = row + dr * i
                c = col + dc * i
                if 0 <= r < self.config.rows and 0 <= c < self.config.cols and self.board[r][c] == player:
                    cells.append((r, c))
                else:
                    break
            
            for i in range(1, max_range):  # ← toute la grille
                r = row - dr * i
                c = col - dc * i
                if 0 <= r < self.config.rows and 0 <= c < self.config.cols and self.board[r][c] == player:
                    cells.append((r, c))
                else:
                    break
            
            if len(cells) >= 5:
                return cells
        
        return None
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