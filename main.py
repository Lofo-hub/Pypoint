import pygame
from config import Config
from game import Game
from database import Database
from renderer import Renderer

def main():
    database = Database()
    config = Config()  
    game = Game(config)
    renderer = Renderer(game)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                col = (mx - renderer.config.padding) // renderer.config.cell_size
                row = (my - renderer.config.padding) // renderer.config.cell_size
                game.place(row, col)
            if event.type == pygame.KEYDOWN:
                if game.canon_actif and not game.game_over:
                    if event.key == pygame.K_UP:
                        game.canon_row = max(0, game.canon_row - 1)
                    if event.key == pygame.K_DOWN:
                        game.canon_row = min(game.config.rows - 1, game.canon_row + 1)
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, 
                 pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        game.canon_jauge = int(pygame.key.name(event.key))
                        game.fire_canon(game.canon_row, game.canon_jauge)
                if event.key == pygame.K_SPACE:
                    game.canon_actif = not game.canon_actif
                if event.key == pygame.K_t:  
                    game.terminer()
                if event.key == pygame.K_s:
                    nom = input("Nom de la sauvegarde : ")
                    database.sauvegarder(game, nom)
                    print("Partie sauvegardée !")
                if event.key == pygame.K_l:
                    parties = database.liste_parties()
                    for p in parties:
                        print(p["nom"], "-", p["date"])
                    nom = input("Nom de la partie à charger : ")
                    partie = database.charger(nom)
                    if partie:
                        game.board = partie["board"]
                        game.current_player = partie["current_player"]
                        game.score_j1 = partie["score_j1"]
                        game.score_j2 = partie["score_j2"]
                        print("Partie chargée !")
                    else:
                        print("Partie introuvable !")        
        renderer.draw(game)
        renderer.clock.tick(60)
if __name__ == "__main__":
    main()