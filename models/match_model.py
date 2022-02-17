class Match:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = ()

    def serializer_match(self):
        serialized_match = {
            "resultat": self.resultat
        }
        return serialized_match

    def __str__(self):
        return f"{self.joueur1.prenom} / {self.joueur2.prenom}, {self.resultat}"

