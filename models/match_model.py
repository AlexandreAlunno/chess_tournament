class Match:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = ()

    def resultats(self):
        self.resultatJ1 = input(f"Veuillez rentrez les resultats de {self.joueur1.prenom}: ")
        self.resultatJ2 = input(f"Veuillez rentrez les resultats de {self.joueur2.prenom}: ")
        resultat_match = [self.joueur1.prenom, self.resultatJ1], [self.joueur2.prenom, self.resultatJ2]
        self.joueur1.point += int(self.resultatJ1)
        self.joueur2.point += int(self.resultatJ2)
        self.resultat = resultat_match
        print("---------------------------")

    def serializer_match(self):
        serialized_match = {
            "resultat": self.resultat
        }
        return serialized_match

    def __str__(self):
        return f"{self.joueur1.prenom} / {self.joueur2.prenom}, {self.resultat}"

