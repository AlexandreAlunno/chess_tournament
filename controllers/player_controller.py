from tinydb import TinyDB

from views.player_views import ViewJoueur
from models.player_model import Joueur

class PlayerController:
    @classmethod
    def build_joueur(cls):
        data = ViewJoueur.get_data_joueur()
        joueur = Joueur(data[0], data[1], data[2], data[3], data[4])
        return joueur


if __name__ == "__main__":
    joueur = PlayerController.build_joueur()
    print(joueur)
    db = TinyDB("db.json")
    players_table = db.table("players")
    players_table.truncate()
    serelized_player = joueur.serializer_joueur()
    players_table.insert(serelized_player)
    print(players_table.all)