
class Config:
    def __init__(self):
        self.cols = int(input("Nombre de colonnes (défaut 15) : ") or 15)
        self.rows = int(input("Nombre de lignes (défaut 15) : ") or 15)
        self.cell_size = 40
        self.padding = 10
   
        self.screen_width = self.cols * self.cell_size + self.padding * 2 + 100
        self.screen_height = self.rows * self.cell_size + self.padding * 2 + 100
        self.bg_color   = (185, 122, 87)   # bois clair
        self.grid_color = (101, 67, 33)    # bois foncé
        self.p1_color   = (20, 20, 20)     # noir (pierre noire)
        self.p2_color   = (240, 235, 220)  # blanc cassé (pierre blanche)
        self.text_color = (50, 30, 10)     # brun foncé
