from models.player_model import Joueur

class Match:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = ()

    def serializer_match(self):
        serialized_match = {
            "joueur1": Joueur.serializer_joueur(self.joueur1),
            "joueur2": Joueur.serializer_joueur(self.joueur2),
            "resultat": self.resultat
        }
        return serialized_match

    def __str__(self):
        return f"{self.joueur1.prenom} / {self.joueur2.prenom}, {self.resultat}"

