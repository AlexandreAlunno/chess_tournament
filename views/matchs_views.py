class MatchView:
    @staticmethod
    def get_results(match):
        print("Match fini. Entrer les résultats de chaque joueur."
              " 1 pour le gagnant, 0 pour le perdant et 0.5 pour chaque joueurs si match nul.")
        resulat_joueur1 = input(f"Resultat de {match.joueur1.prenom}: ")
        resulat_joueur2 = input(f"Resultat de {match.joueur2.prenom}: ")
        return [resulat_joueur1, resulat_joueur2]

    @staticmethod
    def fin_match():
        match_fini = False
        while match_fini == False:
            suivant = int(input("Match fini ? (1 = oui / 2 = non) "))
            if suivant == 1:
                match_fini = True
            elif suivant == 2:
                match_fini = False
            else:
                print("1 = oui / 2 = non")


if __name__ == "__main__":
    MatchView.fin_match()
