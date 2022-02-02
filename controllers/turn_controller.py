from models.turn_model import Tours
from models.match_model import Match
from models.player_model import Joueur
from views.matchs_views import MatchView


class TurnController:
    def __init__(self, tour: Tours):
        self.tour = Tours

    @classmethod
    def build_match_list(cls, participant):
        p1 = 0
        p2 = 0
        nb_paire = 0
        matchs_list = []
        middle_index = len(participant) // 2
        first_half = participant[:middle_index]
        second_half = participant[middle_index:]
        while nb_paire < len(participant) / 2:
            match = Match(first_half[p1], second_half[p2])
            matchs_list.append(match)
            p1 += 1
            p2 += 1
            nb_paire += 1
        return matchs_list


if __name__ == "__main__":
    tournois = TournamentController.build_tournois()
    participant = TournamentController.build_participant_list()
    matchs_list = TurnController.build_match_list(participant)
    print(matchs_list[1])
