from controllers.main_controller import MainController
from views.tournament_views import ViewTournament



debut = ViewTournament.debut_tournoi()
if debut == 1:
    MainController.new_tournament()
elif debut == 2:
    loaded_tournament = MainController.load_tournament()



else:
    print("Veuillez choisir entre créer et charger un tournoi. (1 ou 2)")

