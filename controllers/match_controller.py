from views.matchs_views import MatchView
from models.match_model import Match
from models.player_model import Joueur
from controllers.player_controller import PlayerController

class MatchController:
    @classmethod
    def build_match(cls, joueur1, joueur2):
        match = Match(joueur1, joueur2)
        return match

    @classmethod
    def resultat(cls, match):
        MatchView.fin_match()
        resultat = MatchView.get_results(match)
        match.joueur1.point += float(resultat[0])
        match.joueur2.point += float(resultat[1])
        resultat_match = [match.joueur1.prenom, resultat[0]], [match.joueur2.prenom, resultat[1]]
        match.resultat = resultat_match

    @classmethod
    def deserialized_match(cls, serialized_match):
        joueur1 = PlayerController.deserialized_joueur(serialized_match["joueur1"])
        joueur2 = PlayerController.deserialized_joueur(serialized_match["joueur2"])
        resultat = serialized_match["resultat"]
        match = Match(joueur1=joueur1, joueur2=joueur2)
        match.resultat = resultat
        return match



