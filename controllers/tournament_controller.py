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
        for nb in range(tournois.nombre_de_joueur):
            joueur = info_joueur[nb]
            #joueur = PlayerController.build_joueur()
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

    fin_tournois = False

    while fin_tournois == False:

        tournois = TournamentController.build_tournois()
        serialized_tournois = tournois.serialized_tournament()

        participant = TournamentController.build_participant_list(tournois)
        round_list = TournamentController.build_turn(tournois)
        print(round_list)

        actual_turn = 0
        for turn in round_list:
            TurnController.date_heure_debut(turn)
            seriallized_round = turn.serializer_tour()
            match_list = TurnController.build_match_list(participant, turn)

            for match in match_list:
                MatchController.resultat(match)
                seriallized_round["match_list"].append(match.serializer_match())

            TurnController.date_heure_fin(turn)
            serialized_tournois["tours"].append(seriallized_round)
            actual_turn += 1
            if actual_turn != tournois.nombre_de_tour:
                fin_tour = ViewTournament.continuer()
                if fin_tour == 0:
                    pass
                elif fin_tour == 1:
                    for joueur in participant:
                        serialized_tournois["player_list"].append(joueur.serializer_joueur())
                    TournamentController.save_tournament(serialized_tournois)
                    fin_tournois = True
                    break
            else:
                for joueur in participant:
                    serialized_tournois["player_list"].append(joueur.serializer_joueur())
                TournamentController.save_tournament(serialized_tournois)
                fin_tournois = True
                print("tournois fini")
                break


    """db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
    table_tournois = db.table("tournois")
    serializied_tournaments = table_tournois.all()

    #nom = input("nom ddu tournoi ")
    nom_tournois = "test_unfinished"
    loaded_tournament = []
    while loaded_tournament == []:
        for index in range(0, len(serializied_tournaments)):
            if serializied_tournaments[index]["nom"] == nom_tournois:
                loaded_tournament = serializied_tournaments[index]

    tournament = TournamentController.deserialized_tournois(loaded_tournament)
    serialized_tournois = tournament.serialized_tournament()

    participant = tournament.players_list

    nb_turn = len(tournament.turns)

    actual_turn = 0
    while len(tournament.turns) < tournament.nombre_de_tour:
        round_list = TurnController.build_turns(tournament, nb_turn)

        for round in round_list:
            match_list = TurnController.build_match_list(participant, round)
            TurnController.date_heure_debut(round)
            seriallized_round = round.serializer_tour()

            for match in match_list:
                MatchController.resultat(match)
                seriallized_round["match_list"].append(match.serializer_match())

            TurnController.date_heure_fin(round)
            serialized_tournois["tours"].append(seriallized_round)

            actual_turn += 1
            if actual_turn != tournament.nombre_de_tour:
                fin_tour = ViewTournament.continuer()
                if fin_tour == 0:
                    pass
                elif fin_tour == 1:
                    for joueur in participant:
                        serialized_tournois["player_list"].append(joueur.serializer_joueur())
                    TournamentController.save_tournament(serialized_tournois)
                    fin_tournois = True
                    break
            else:
                for joueur in participant:
                    serialized_tournois["player_list"].append(joueur.serializer_joueur())
                table_tournois.remove(where("nom")==f"{nom_tournois}")
                TournamentController.save_tournament(serialized_tournois)
                fin_tournois = True
                print("tournois fini")
                break"""

    """nom_tournois = "test_unfinished"
    db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
    table_tournois = db.table("tournois")
    table_tournois.remove(where("nom") == f"{nom_tournois}")"""
















