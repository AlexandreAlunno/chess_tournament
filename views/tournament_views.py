import time


class ViewTournament:
    @staticmethod
    def get_data_tournois():
        nom_tournois = input("Nom du tournois: ")
        lieu = input("Lieu du tournois: ")
        date = input("Date du tournois(JJ/MM/AAAA): ")
        nombre_joueurs = int(input("Nombre de joueur: "))
        nombre_tours = int(input("Nombre de tour: "))
        print("---------------------------")
        data_tournois = [nom_tournois, lieu, date, nombre_joueurs, nombre_tours]

        return data_tournois

    @staticmethod
    def new_player():
        choose = False

        print("Voulez-vous créer un nouveau joueur ou en charger un existant ?")
        print("1 = Créer nouveau joueur.")
        print("2 = Charger joueur.")

        while choose == False:
            choice = input("Créer ou charger: ")

            if choice == "1":
                choose = True

            elif choice == "2":
                choose = True

            else:
                print("Entrer 1 / 2")

            return choice

    @staticmethod
    def get_raport_tournois():
        print("Ajouter un commentaire au tournois.")
        commentaire = input("Commentaire: ")
        return commentaire

    @staticmethod
    def get_tournament_name():
        loaded_tournament = input("Entrer le nom du tournois: ")
        return loaded_tournament

    @staticmethod
    def next_turn():
        turn_over = False
        while turn_over == False:
            next_turn = input("Passer au tour suivant ?(oui/non) ")
            if next_turn == "oui":
                turn_over = True
                time.sleep(1)
                return turn_over
            elif next_turn == "non":
                input("Passer au tour suivant ?(oui/non) ")
            else:
                print("Réponse attendus: oui/non")

    @staticmethod
    def continuer():
        choice = False
        menu = 0

        print("Fin du tour")
        print("Voulez-vous continuer le tournois ou le sauvegarder ? ")
        print("1 = Continuer.")
        print("2 = Sauvegarder.")

        while choice == False:
            save_tournament = int(input("Choix: "))
            if save_tournament == 1:
                menu = 1
                choice = True

            elif save_tournament == 2:
                menu = 1
                choice = True

            else:
                print("1 = continuer, 2 = sauvegarder")

        return menu


if __name__ == "__main__":
    ViewTournament.get_raport_tournois()
