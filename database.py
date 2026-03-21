from pymongo import MongoClient
from datetime import datetime

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["puissance5"]
        self.parties = self.db["parties"]
    def sauvegarder(self, game, nom):
        partie = {
            "nom": nom,
            "date": datetime.now(),          # date et heure actuelle
            "board": game.board,         # le plateau
            "current_player": game.current_player,
            "score_j1": game.score_j1,
            "score_j2": game.score_j2,
        }
        self.parties.insert_one(partie)
    def charger(self, nom):
        return self.parties.find_one({"nom": nom})
    def liste_parties(self):
        return list(self.parties.find({}, {"_id": 0, "nom": 1, "date": 1}))