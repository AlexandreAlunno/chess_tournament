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
    def debut_tournoi():
        debut = False
        while debut == False:
            start_tournament = input("Charger un tournois existant ou créer un tournoi ?"
                                     "(Taper 1 pour charger 2 pour créer) ")
            if start_tournament == "1":
                debut = True
            elif start_tournament == "2":
                debut = True
            else:
                print("Entrer 1 ou 2")

    @staticmethod
    def next_turn():
        turn_over = False
        while turn_over == False:
            next_turn = input("Commencer le tour ?(oui/non) ")
            if next_turn == "oui":
                turn_over = True
                time.sleep(1)
                return turn_over
            elif next_turn == "non":
                input("Passer au tour suivant ?(oui/non) ")
            else:
                print("Réponse attendus: oui/non")


if __name__ == "__main__":
    #ViewTournament.get_data_tournois()
    ViewTournament.debut_tournoi()
    #ViewTournament.next_turn()