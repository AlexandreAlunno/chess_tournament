from controllers.main_controller import MainController
from views.main_view import MainView

end_program = False

while end_program == False:

    menu = MainView.debut_tournoi()
    if menu == 1:
        MainController.new_tournament()
        end_program = MainView.end_program()

    elif menu == 2:
        MainController.load_tournament()
        end_program = MainView.end_program()

    elif menu == 3:
        MainController.manage_player()

    elif menu == 4:
        MainController.reports()

    elif menu == 5:
        end_program = True

    else:
        print("Veuillez choisir une option valide:")
        print("1 = Créer un nouveau tournois.")
        print("2 = Charger un tournois existant.")
        print("3 = Gestion des joueurs.")
        print("4 = Gestion des rapports.")
        print("5 = Arreter le programme.")
