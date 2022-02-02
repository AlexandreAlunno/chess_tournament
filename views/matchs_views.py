from models.match_model import Match


class MatchView:

    def get_results(self):
        resulat_joueur1 = input(f"Veuillez rentrez les resultats de {match.joueur1.prenom}: ")
        resulat_joueur2 = input(f"Veuillez rentrez les resultats de {match.joueur2.prenom}: ")
        return [resulat_joueur1, resulat_joueur2]


if __name__ == "__main__":
    MatchView.get_results()