
class ViewJoueur:
    @staticmethod
    def get_data_joueur():
        nom = input("Nom du joueur: ")
        prenom = input("Prenom du joueur: ")
        date_de_naissance = input("Date de naissance du joueur : ")
        sexe = input("Sexe du joueur: ")
        classement = int(input("Classement du joueur: "))

        data_joueur = [nom, prenom, date_de_naissance, sexe, classement]

        return data_joueur

if __name__ == "__main__":
    ViewJoueur.get_data_joueur()