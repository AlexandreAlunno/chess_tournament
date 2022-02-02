from views.player_views import ViewJoueur
from models.player_model import Joueur

class PlayerController:
    @classmethod
    def build_joueur(cls):
        data = ViewJoueur.get_data_joueur()
        joueur = Joueur(data[0], data[1], data[2], data[3], data[4])
        return joueur

if __name__ == "__main__":
    joueur = PlayerController.build_joueur()
    print(joueur)