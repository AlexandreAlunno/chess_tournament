class Match:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = ()

    def resultats(self):
        resulat_joueur1 = input(f"Veuillez rentrez les resultats de {self.joueur1.prenom}: ")
        resulat_joueur2 = input(f"Veuillez rentrez les resultats de {self.joueur2.prenom}: ")
        resultat_match = [self.joueur1.prenom, resulat_joueur1], [self.joueur2.prenom, resulat_joueur2]
        self.joueur1.point += int(resulat_joueur1)
        self.joueur2.point += int(resulat_joueur2)
        self.resultat = resultat_match

    def __str__(self):
        return f"{self.joueur1} / {self.joueur2}"