from models.tournament_model import Tournois
from models.player_model import Joueur
from models.turn_model import Tours
from models.match_model import Match
from views.tournament_views import ViewTournament
from views.player_views import ViewJoueur
from views.matchs_views import MatchView
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
                            serialized_tournois["player_list"].append(joueur.serializer_joueur())

                        TournamentController.save_tournament(serialized_tournois)
                        fin_tournois = True
                        print("Tournois fini et sauvegardé")
                        break
                else:
                    for joueur in participant:
                        serialized_tournois["player_list"].append(joueur.serializer_joueur())
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
                                serialized_player = joueur.serializer_joueur()
                                player_list.append(serialized_player)
                                loaded_tournament["player_list"] = player_list

                            table_tournois.remove(where("nom") == f"{nom_tournois}")
                            TournamentController.save_tournament(loaded_tournament)
                            fin_tournois = True
                            break
                    else:
                        for joueur in participant:
                            serialized_player = joueur.serializer_joueur()
                            player_list.append(serialized_player)
                            loaded_tournament["player_list"] = player_list

                        table_tournois.remove(where("nom") == f"{nom_tournois}")
                        TournamentController.save_tournament(loaded_tournament)
                        fin_tournois = True
                        print("tournois fini")
                        break


if __name__ == "__main__":
    #MainController.new_tournament()
    MainController.load_tournament()


