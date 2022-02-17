from models.tournament_model import Tournois
from models.player_model import Joueur
from models.turn_model import Tours
from models.match_model import Match
from views.tournament_views import ViewTournament
from views.player_views import ViewJoueur
from views.matchs_views import MatchView
from controllers.player_controller import PlayerController
from controllers.turn_controller import TurnController
from controllers.tournament_controller import TournamentController
from controllers.match_controller import MatchController


class MainController:
    @classmethod
    def new_tournament(cls):
        tournois = TournamentController.build_tournois()  # create tournament

        serialized_tournois = tournois.serialized_tournament()  # serialized the tournament

        participants = TournamentController.build_participant_list(
            tournois)  # create players in number set in tournament

        turn_list = TournamentController.build_turn(tournois)  # create the list of rounds

        for turn in turn_list:  # iterate on each round
            seriallized_round = turn.serializer_tour()  # serialized the ongoing turn

            match_list = TurnController.build_match_list(participants, turn)  # create the matchs within the round

            for match in match_list:  # iterate on each match
                MatchController.resultat(match)  # inpute the results for each mmatch, save in the match instance
                seriallized_round["match_list"].append(
                    match.serializer_match())  # serialized the mactch+results and add to the turn

            serialized_tournois["tours"].append(seriallized_round)  # add the ongoing turn to the serialized tournois

        return serialized_tournois

    @classmethod
    def load_tournament(cls):
        pass