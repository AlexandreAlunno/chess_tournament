from tinydb import TinyDB, where
from views.player_views import ViewJoueur
from models.player_model import Joueur


class PlayerController:
    @classmethod
    def build_joueur(cls):
        data = ViewJoueur.get_data_joueur()
        joueur = Joueur(data[0], data[1], data[2], data[3], data[4])
        return joueur

    @classmethod
    def load_player(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        players_table = db.table("players_list")
        serialized_players = players_table.all()
        nom_joueur = ViewJoueur.get_player_name()
        loaded_player = []

        while loaded_player == []:
            for index in range(0, len(serialized_players)):
                if serialized_players[index]["name"] == nom_joueur:
                    loaded_player = serialized_players[index]

        player = PlayerController.deserialized_joueur(loaded_player)
        return player


    @classmethod
    def modify_classement(cls, joueur):
        joueur.classement = input(f"Nouveau classement de {joueur.nom}: ")

    @classmethod
    def save_player(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        players_table = db.table("players_list")
        joueur = PlayerController.build_joueur()
        nom_joueur = joueur.nom
        serialized_player = Joueur.serializer_joueur(joueur)
        players_table.remove(where("name") == f"{nom_joueur}")
        players_table.insert(serialized_player)

    @classmethod
    def modify_saved_player(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        player_table = db.table("players_list")
        serialized_players = player_table.all()

        nom_joueur = ViewJoueur.get_player_name()
        loaded_player = []

        while loaded_player == []:
            for index in range(0, len(serialized_players)):
                if serialized_players[index]["name"] == nom_joueur:
                    loaded_player = serialized_players[index]

        menu = ViewJoueur.modify_data_joueur()
        new_data = input("Entrer nouvelle donnée: ")

        loaded_player[f"{menu}"] = new_data
        player_table.remove(where("name") == f"{nom_joueur}")
        player_table.insert(loaded_player)

    @classmethod
    def erase_player(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        player_table = db.table("players_list")
        serialized_players = player_table.all()
        nom_joueur = ViewJoueur.get_player_name()
        loaded_player = []

        while loaded_player == []:
            for index in range(0, len(serialized_players)):
                if serialized_players[index]["name"] == nom_joueur:
                    loaded_player = serialized_players[index]

        player_table.remove(where("name") == f"{nom_joueur}")

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

    @classmethod
    def display_players_alphabethical(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        player_table = db.table("players_list")
        players_list = player_table.all()
        players_list = sorted(players_list, key=lambda player: player["name"], reverse=False)
        for player in players_list:
            print(f'Nom : {player["name"]}, Prenom: {player["prenom"]}, Classement: {player["classement"]}')

    @classmethod
    def display_players_classement(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        player_table = db.table("players_list")
        players_list = player_table.all()
        players_list = sorted(players_list, key=lambda player: player["classement"], reverse=False)
        for player in players_list:
            print(f'Nom : {player["name"]}, Prenom: {player["prenom"]}, Classement: {player["classement"]}')

    @classmethod
    def display_players(cls):
        menu = ViewJoueur.alphabetical_numeral()

        if menu == 1:
            PlayerController.display_players_alphabethical()

        elif menu == 2:
            PlayerController.display_players_classement()


if __name__ == "__main__":
    PlayerController.display_players_alphabethical()
    PlayerController.display_players_classement()

