from views.matchs_views import MatchView
from controllers.player_controller import PlayerController
from controllers.turn_controller import TurnController
from models.match_model import Match
from models.player_model import Joueur


class MatchController:

    def build_match(self):
        joueur1 = Joueur
        joueur2 = Joueur
        match = Match(joueur1, joueur2)
        return match

    def resultat(self):
        MatchView.get_results()
        resultat_match = ([self.match.joueur1.prenom, resulat_joueur1], [self.match.joueur2.prenom, resulat_joueur2])
        self.match.joueur1.point += int(resulat_joueur1)
        self.match.joueur2.point += int(resulat_joueur2)
        self.match.resultat = resultat_match
