from models.turn_model import Tours
from models.match_model import Match
from models.player_model import Joueur
from views.matchs_views import MatchView
from controllers.match_controller import MatchController


class TurnController:

    @classmethod
    def build_turns(cls, tournois):
        round_list = []
        for nb_turn in range(tournois.nombre_de_tour):
            round = Tours(f"Round {nb_turn + 1}")
            round_list.append(round)
            tournois.turns.append(round)
        return round_list

    @classmethod
    def build_match_list(cls, participant, tour):
        p1 = 0
        p2 = 0
        nb_paire = 0
        matchs_list = []
        middle_index = len(participant) // 2
        first_half = participant[:middle_index]
        second_half = participant[middle_index:]
        while nb_paire < len(participant) / 2:
            match = MatchController.build_match(first_half[p1], second_half[p2])
            tour.match_list.append(match)
            matchs_list.append(match)
            p1 += 1
            p2 += 1
            nb_paire += 1
        return matchs_list


if __name__ == "__main__":
    tournois = TournamentController.build_tournois()
    round_list = TurnController.build_turns(tournois)


