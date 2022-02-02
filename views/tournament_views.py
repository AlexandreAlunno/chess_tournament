

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


if __name__ == "__main__":
    ViewTournament.get_data_tournois()