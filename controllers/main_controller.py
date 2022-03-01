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
from tinydb import TinyDB


class MainController:
    @classmethod
    def new_tournament(cls):
        tournois = TournamentController.build_tournois()  # create tournament

        serialized_tournois = tournois.serialized_tournament()  # serialized the tournament

        participants = TournamentController.build_participant_list(
            tournois)  # create players in number set in tournament

        turn_list = TournamentController.build_turn(tournois)  # create the list of rounds

        for turn in turn_list:  # iterate on each round
            seriallized_round = turn.serializer_tour()  # serialized the ongoing turn

            match_list = TurnController.build_match_list(participants, turn)  # create the matchs within the round

            for match in match_list:  # iterate on each match
                MatchController.resultat(match)  # inpute the results for each mmatch, save in the match instance
                seriallized_round["match_list"].append(
                    match.serializer_match())  # serialized the mactch+results and add to the turn

            serialized_tournois["tours"].append(seriallized_round)  # add the ongoing turn to the serialized tournois

        return serialized_tournois

    @classmethod
    def load_tournament(cls):
        db = TinyDB("D:\\Formation python\\chess_tournament v2\\db.json")
        table_tournois = db.table("tournois")
        serializied_tournaments = table_tournois.all()
        nom = input("nom ddu tournoi ")
        loaded_tournament = []
        while loaded_tournament == []:
            for index in range(0, len(serializied_tournaments)):
                if serializied_tournaments[index]["nom"] == nom:
                    loaded_tournament = serializied_tournaments[index]

        loaded_tours = loaded_tournament["tours"]
        deserialized_tournois = TournamentController.deserialized_tournois(loaded_tournament)
        deserialized_tours_list = []
        deserialized_match_list = []

        for tour in loaded_tours:
            deserialized_tour = TurnController.deserialized_turn(tour)
            for match in deserialized_tour.match_list:
                deserialized_match = MatchController.deserialized_match(match)
                deserialized_match_list.append(deserialized_match)
                deserialized_tour.match_list = deserialized_match_list
            deserialized_tours_list.append(deserialized_tour)
        deserialized_tournois.turns = deserialized_tours_list

        return deserialized_tournois

if __name__ == "__main__":
    loaded_tournament = MainController.load_tournament()
    while len(loaded_tournament.turns) < loaded_tournament.nombre_de_tour:
        participant = loaded_tournament.players_list
        tours = TournamentController.build_turn(loaded_tournament)
        for turn in tours:
            match_list = TurnController.build_match_list(participant, turn)
            for match in match_list:
                MatchController.resultat(match)

