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
    def get_tournament_name():
        loaded_tournament = input("Entrer le nom du tournois à charger")
        return loaded_tournament

    @staticmethod
    def debut_tournoi():
        print("Bienvenue dans ce programme de gestion de tournois d'echec.")
        charger = 0
        nouveau = 0
        while nouveau == False:
            start_tournament = input("Charger un tournois existant ou créer un tournoi ?"
                                     "(Taper 1 pour céer 2 pour charger) ")
            if start_tournament == "1":
                nouveau = 1
                return nouveau
            elif start_tournament == "2":
                charger = 2
                return charger
            else:
                print("Entrer 1 ou 2")

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


if __name__ == "__main__":
    #ViewTournament.get_data_tournois()
    debut = ViewTournament.debut_tournoi()
    print(debut)
    #ViewTournament.next_turn()