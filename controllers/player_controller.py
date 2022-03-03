from tinydb import TinyDB
from views.player_views import ViewJoueur
from models.player_model import Joueur


class PlayerController:
    @classmethod
    def build_joueur(cls):
        data = ViewJoueur.get_data_joueur()
        joueur = Joueur(data[0], data[1], data[2], data[3], data[4])
        return joueur

    @classmethod
    def deserialized_joueur(cls,serialized_joueur):
        nom = serialized_joueur["name"]
        prenom = serialized_joueur["prenom"]
        date_de_naissance = serialized_joueur["date_de_naissance"]
        sexe = serialized_joueur["sexe"]
        classement = serialized_joueur["classement"]
        score = serialized_joueur["score"]
        joueur = Joueur(nom=nom, prenom=prenom, date_de_naissance=date_de_naissance, sexe=sexe, classement=classement, point=score)
        return joueur


if __name__ == "__main__":
    db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
    """joueur = PlayerController.build_joueur()
    #print(joueur)
    db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
    players_table = db.table("players joueur")
    #players_table.truncate()
    serelized_player = joueur.serializer_joueur()
    players_table.insert(serelized_player)"""
    players_table = db.table("players joueur")
    serialized_players_table = players_table.all()
    #joueur1 = Joueur(serialized_players_table[0])
    #print(type(joueur1))
    participant = []
    for player in serialized_players_table:
        joueur = PlayerController.deserialized_joueur(player)
        participant.append(joueur)
        print(participant)

