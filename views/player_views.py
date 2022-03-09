
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

    @staticmethod
    def get_player_name():
        nom_joueur = input("Nom du joueur: ")
        return nom_joueur

    @staticmethod
    def modify_data_joueur():
        choose = False
        menu = 0

        print("Quelle donnée voulez-vous modifier ?")
        print("1 = Nom")
        print("2 = Prenom")
        print("3 = Date de naissance")
        print("4 = sexe")
        print("5 = classement")

        while choose == False:
            choice = int(input("Choix de menu: "))

            if choice == 1:
                menu = "name"
                choose = True
                return menu

            elif choice == 2:
                menu = "prenom"
                choose = True
                return menu

            elif choice == 3:
                menu = "date_de_naissance"
                choose = True
                return menu

            elif choice == 4:
                menu = "sexe"
                choose = True
                return menu

            elif choice == 5:
                menu = "classement"
                choose = True
                return menu

            else:
                print("Entrer 1 / 2 / 3 / 4 / 5")

    @staticmethod
    def alphabetical_numeral():
        choose = False
        menu = 0

        print("Trie alphabetique ou par classement ?")
        print("1 = Alphabetique")
        print("2 = Classement")

        while choose == False:
            choice = int(input("Choix de menu: "))

            if choice == 1:
                menu = 1
                choose = True

            elif choice == 2:
                menu = 2
                choose =True

            else:
                print("Entrer 1 / 2")

        return menu

if __name__ == "__main__":
    ViewJoueur.get_data_joueur()