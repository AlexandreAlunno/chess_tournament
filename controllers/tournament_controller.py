from models.tournament_model import Tournois
from models.player_model import Joueur
from models.turn_model import Tours
from models.match_model import Match
from views.tournament_views import ViewTournament
from views.player_views import ViewJoueur
from views.matchs_views import MatchView
from controllers.player_controller import PlayerController
from controllers.turn_controller import TurnController
from tinydb import TinyDB


class TournamentController:
    @classmethod
    def build_tournois(cls):
        data = ViewTournament.get_data_tournois()
        tournois = Tournois(data[0], data[1], data[2], data[3], data[4])
        return tournois

    @classmethod
    def build_participant_list(cls, tournois):
        participant = []
        info_joueur = [Joueur(nom="tri", prenom="J1", date_de_naissance="18/10", sexe="m", classement=2, point=0)
            , Joueur(nom="trre", prenom="J2", date_de_naissance="18/20/1997", sexe="f", classement=1, point=0)
            , Joueur(nom="ert", prenom="J3", date_de_naissance="10/17/1997", sexe="f", classement=4, point=0)
            , Joueur(nom="htgg", prenom="J4", date_de_naissance="10/21/1997", sexe="m", classement=3, point=0)
            , Joueur(nom="rtgr", prenom="J5", date_de_naissance="21/07/1997", sexe="m", classement=6, point=0)
            , Joueur(nom="fgrd", prenom="J6", date_de_naissance="22/02/1997", sexe="f", classement=5, point=0)
            , Joueur(nom="gfdfd", prenom="J7", date_de_naissance="21/25/1997", sexe="f", classement=8, point=0)
            , Joueur(nom="dfrg", prenom="J8", date_de_naissance="21/30/1997", sexe="f", classement=7, point=0)]
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

"""
   @classmethod
    def tournois(cls):
        for turn in turn_list:
            #print(turn)
            match_list = TurnController.build_match_list(participant)
            #print(match_list[0])
            for match in match_list:
                match.resultats()
            ViewTournament.next_turn()"""


if __name__ == "__main__":
    tournois = TournamentController.build_tournois()
    serialized_tournois = tournois.serialized_tournament()
    participant = TournamentController.build_participant_list(tournois)
    round_list = TournamentController.build_turn(tournois)
    print(serialized_tournois)
    for turn in round_list:
        seriallized_round = turn.serializer_tour()
        print(seriallized_round)
        match_list = TurnController.build_match_list(participant, turn)
        for match in match_list:
            match.resultats()
            seriallized_round["match_list"].append(match.serializer_match())
        serialized_tournois["tours"].append(seriallized_round)
    print(serialized_tournois)
    TournamentController.save_tournament(serialized_tournois)


