from views.tournament_views import ViewTournament
from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.turn_controller import TurnController
from controllers.tournament_controller import TournamentController
from controllers.match_controller import MatchController
from tinydb import TinyDB, where


class MainController:
    @classmethod
    def new_tournament(cls):
        fin_tournois = False

        while fin_tournois == False:

            tournois = TournamentController.build_tournois()
            serialized_tournois = tournois.serialized_tournament()

            participant = TournamentController.build_participant_list(tournois)
            round_list = TournamentController.build_turn(tournois)

            actual_turn = len(tournois.turns)
            for turn in round_list:
                TurnController.date_heure_debut(turn)
                seriallized_round = turn.serializer_tour()
                match_list = TurnController.build_match_list(participant, turn)

                for match in match_list:
                    MatchController.resultat(match)
                    seriallized_round["match_list"].append(match.serializer_match())

                TurnController.date_heure_fin(turn)
                serialized_tournois["tours"].append(seriallized_round)

                actual_turn += 1
                if actual_turn != tournois.nombre_de_tour:
                    fin_tour = ViewTournament.continuer()
                    if fin_tour == 0:
                        pass
                    elif fin_tour == 1:
                        for joueur in participant:
                            PlayerController.modify_classement(joueur)
                            serialized_tournois["player_list"].append(joueur.serializer_joueur())

                        TournamentController.write_report(tournois)
                        TournamentController.save_tournament(serialized_tournois)
                        fin_tournois = True
                        print("Tournois fini et sauvegardé")
                        break
                else:
                    for joueur in participant:
                        PlayerController.modify_classement(joueur)
                        serialized_tournois["player_list"].append(joueur.serializer_joueur())

                    TournamentController.write_report(tournois)
                    TournamentController.save_tournament(serialized_tournois)
                    fin_tournois = True
                    print("Tournois fini et sauvegardé")
                    break

    @classmethod
    def load_tournament(cls):
        fin_tournois = False

        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        table_tournois = db.table("tournois")

        player_list = []

        while fin_tournois == False:

            loaded_tournament = TournamentController.load_tournament()
            nom_tournois = loaded_tournament["nom"]
            tournament = TournamentController.deserialized_tournois(loaded_tournament)

            participant = tournament.players_list

            nb_turn = len(tournament.turns)
            actual_turn = len(tournament.turns)
            while len(tournament.turns) < tournament.nombre_de_tour:
                round_list = TurnController.build_turns(tournament, nb_turn)

                for round in round_list:
                    TurnController.date_heure_debut(round)
                    match_list = TurnController.build_match_list(participant, round)
                    TurnController.date_heure_debut(round)
                    seriallized_round = round.serializer_tour()

                    for match in match_list:
                        MatchController.resultat(match)
                        seriallized_round["match_list"].append(match.serializer_match())

                    TurnController.date_heure_fin(round)
                    loaded_tournament["tours"].append(seriallized_round)

                    actual_turn += 1

                    if actual_turn != tournament.nombre_de_tour:
                        fin_tour = ViewTournament.continuer()

                        if fin_tour == 1:
                            for joueur in participant:
                                PlayerController.modify_classement(joueur)
                                serialized_player = joueur.serializer_joueur()
                                player_list.append(serialized_player)
                                loaded_tournament["player_list"] = player_list

                            TournamentController.write_report(tournament)
                            table_tournois.remove(where("nom") == f"{nom_tournois}")
                            TournamentController.save_tournament(loaded_tournament)
                            fin_tournois = True
                            break
                    else:
                        for joueur in participant:
                            PlayerController.modify_classement(joueur)
                            serialized_player = joueur.serializer_joueur()
                            player_list.append(serialized_player)
                            loaded_tournament["player_list"] = player_list

                        TournamentController.write_report(tournament)
                        table_tournois.remove(where("nom") == f"{nom_tournois}")
                        TournamentController.save_tournament(loaded_tournament)
                        fin_tournois = True
                        print("tournois fini")
                        break

    @classmethod
    def manage_player(cls):
        menu = MainView.manage_player_db()
        if menu == 1:
            PlayerController.modify_saved_player()
        elif menu == 2:
            PlayerController.save_player()
        elif menu == 3:
            PlayerController.erase_player()

    @classmethod
    def reports(cls):
        menu = MainView.menu_repports()

        if menu == 1:
            PlayerController.display_players()

        elif menu == 2:
            TournamentController.displayer_tournament_player()

        elif menu == 3:
            TournamentController.display_tournaments()

        elif menu == 4:
            TournamentController.display_matchs()

        elif menu == 5:
            pass


if __name__ == "__main__":
    MainController.new_tournament()
