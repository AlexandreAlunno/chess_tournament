class MainView:
    @staticmethod
    def debut_tournoi():
        choose = False
        menu = 0

        print("Bienvenue dans ce programme de gestion de tournois d'echec.")
        print("Menu principale:")
        print("1 = Créer un nouveau tournois.")
        print("2 = Charger un tournois existant.")
        print("3 = Gestion des joueurs.")
        print("4 = Afficher rapport.")
        print("5 = Arreter le programme.")

        while choose == False:

            choice = input("Choix de menu: ")
            if choice == "1":
                menu = 1
                choose = True
                return menu

            elif choice == "2":
                menu = 2
                choose = True
                return menu

            elif choice == "3":
                menu = 3
                choose = True
                return menu

            elif choice == "4":
                menu = 4
                choose = True
                return menu

            elif choice == "5":
                menu = 5
                choose = True
                return menu

            else:
                print("Entrer 1 / 2 / 3 / 4")

    @staticmethod
    def manage_player_db():
        choose = False
        menu = 0

        print("Gestion des joueurs enregistré:")
        print("1 = Modifier joueur.")
        print("2 = Enregistrer nouveau joueur.")
        print("3 = Supprimer joueur.")
        print("4 = Retour menu précedent")

        while choose == False:
            choice = int(input("Choix de menu: "))

            if choice == 1:
                menu = 1
                choose = True
                return menu

            elif choice == 2:
                menu = 2
                choose = True
                return menu

            elif choice == 3:
                menu = 3
                choose = True
                return menu

            elif choice == 4:
                choose = True
                pass

            else:
                print("Entrer 1 / 2 / 3")

    @staticmethod
    def menu_repports():
        choose = False
        menu = 0
        print("Affichage des rapports:")
        print("1 = Afficher tout les joueurs enregistrés.")
        print("2 = Afficher tout les joueurs d'un tournois.")
        print("3 = Afficher tout les tournois enregistrés")
        print("4 = Afficher les tours d'un tournois.")
        print("5 = Retour menu précedent")

        while choose == False:
            choice = int(input("Choix de menu: "))

            if choice == 1:
                menu = 1
                choose = True

            elif choice == 2:
                menu = 2
                choose = True

            elif choice == 3:
                menu = 3
                choose = True

            elif choice == 4:
                menu = 4
                choose = True

            elif choice == 5:
                menu = 5
                choose = True

            else:
                print("Entrer 1 / 2 / 3 / 4")

        return menu


    @staticmethod
    def end_program():
        end_program = False
        ask = None
        while ask != "1" and ask != "2":
            ask = input("Voulez-vous stopper le programme ?"
                        "(1=non/2=oui) ")
            if ask == "1":
                end_program = False
            elif ask == "2":
                end_program = True
            else:
                print("1=non/2=oui")
        return end_program

if __name__ == "__main__":
    MainView.end_program()