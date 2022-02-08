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

tournois = TournamentController.build_tournois()  # create tournament

participants = TournamentController.build_participant_list(tournois)  # create players in number set in tournament

turn_list = TournamentController.build_turn(tournois)  # create the list of rounds

for turn in turn_list:  # iterate on each round
    match_list = TurnController.build_match_list(participants, turn)  # create the matchs within the round
    for match in match_list:  # iterate on each match
        match.resultats()  # inpute the results for each mmatch, save in the match instance