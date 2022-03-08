from models.tournament_model import Tournois
from models.player_model import Joueur
from models.turn_model import Tours
from models.match_model import Match
from views.tournament_views import ViewTournament
from views.player_views import ViewJoueur
from views.matchs_views import MatchView
from controllers.player_controller import PlayerController
from controllers.turn_controller import TurnController
from controllers.match_controller import MatchController
from tinydb import TinyDB, Query, where
from tinydb.operations import delete


class TournamentController:
    @classmethod
    def build_tournois(cls):
        data = ViewTournament.get_data_tournois()
        tournois = Tournois(data[0], data[1], data[2], data[3], data[4])
        return tournois

    @classmethod
    def build_participant_list(cls, tournois):
        participant = []
        info_joueur = [Joueur(nom="J1", prenom="J1", date_de_naissance="18/10", sexe="m", classement=2, point=0)
            , Joueur(nom="J2", prenom="J2", date_de_naissance="18/20/1997", sexe="f", classement=1, point=0)
            , Joueur(nom="J3", prenom="J3", date_de_naissance="10/17/1997", sexe="f", classement=4, point=0)
            , Joueur(nom="J4", prenom="J4", date_de_naissance="10/21/1997", sexe="m", classement=3, point=0)
            , Joueur(nom="J5", prenom="J5", date_de_naissance="21/07/1997", sexe="m", classement=6, point=0)
            , Joueur(nom="J6", prenom="J6", date_de_naissance="22/02/1997", sexe="f", classement=5, point=0)
            , Joueur(nom="J7", prenom="J7", date_de_naissance="21/25/1997", sexe="f", classement=8, point=0)
            , Joueur(nom="J8", prenom="J8", date_de_naissance="21/30/1997", sexe="f", classement=7, point=0)]

        while len(tournois.players_list) < tournois.nombre_de_joueur:
            #for nb in range(tournois.nombre_de_joueur):
                new_player = ViewTournament.new_player()

                if new_player == "1":
                    #joueur = info_joueur[nb]
                    joueur = PlayerController.build_joueur()
                    tournois.players_list.append(joueur)
                    participant.append(joueur)

                elif new_player == "2":
                    #joueur = info_joueur[nb]
                    joueur = PlayerController.load_player()
                    tournois.players_list.append(joueur)
                    participant.append(joueur)

        participant = sorted(participant, key=lambda joueur: joueur.classement)
        return participant

    @classmethod
    def trie_score(cls, participant):
        participant = sorted(participant, key=lambda joueur: joueur.point, reverse=True)
        return participant

    @classmethod
    def build_turn(cls, tournois):
        round_list = TurnController.build_turns(tournois)
        return round_list

    @classmethod
    def save_tournament(cls, serialized_tournament):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        tournament_table = db.table("tournois")
        tournament_table.insert(serialized_tournament)
        return tournament_table

    @classmethod
    def load_tournament(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        table_tournois = db.table("tournois")
        serializied_tournaments = table_tournois.all()

        nom_tournois = input("nom ddu tournoi ")
        # nom_tournois = "test_unfinished"
        loaded_tournament = []
        while loaded_tournament == []:
            for index in range(0, len(serializied_tournaments)):
                if serializied_tournaments[index]["nom"] == nom_tournois:
                    loaded_tournament = serializied_tournaments[index]

        return loaded_tournament

    @classmethod
    def deserialized_tournois(cls, serialized_tournament):
        nom = serialized_tournament["nom"]
        lieu = serialized_tournament["lieu"]
        date = serialized_tournament["date"]
        nombre_de_joueur = serialized_tournament["nombre de joueur"]
        nombre_de_tour = serialized_tournament["nombre de tour"]
        player_list = []
        for joueur in serialized_tournament["player_list"]:
            deserialized_joueur = PlayerController.deserialized_joueur(joueur)
            player_list.append(deserialized_joueur)
        deserialized_tours_list = []
        for tour in serialized_tournament["tours"]:
            deserialized_tour = TurnController.deserialized_turn(tour)
            deserialized_tours_list.append(deserialized_tour)
        tournois = Tournois(nom=nom, lieu=lieu, date=date, nombre_de_joueur=nombre_de_joueur, nombre_de_tour=nombre_de_tour)
        tournois.turns = deserialized_tours_list
        tournois.players_list = player_list
        return tournois


if __name__ == "__main__":
    tournois = TournamentController.build_tournois()
    participant = TournamentController.build_participant_list(tournois)
