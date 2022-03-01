from datetime import datetime, date
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
        participant = sorted(participant, key=lambda joueur: joueur.point, reverse=True)
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

    @classmethod
    def date_heure_debut(cls, tour):
        heure_debut = datetime.now().strftime("%HH%M")
        date_debut = date.today().strftime("%d/%m/%Y")
        debut_tour = [date_debut, heure_debut]
        tour.date_debut.append(heure_debut)
        tour.date_debut.append(date_debut)
        return debut_tour

    @classmethod
    def date_heure_fin(cls, tour):
        heure_fin = datetime.now().strftime("%HH%M")
        date_fin = date.today().strftime("%d/%m/%Y")
        fin_tour = [date_fin, heure_fin]
        tour.date_fin.append(heure_fin)
        tour.date_fin.append(date_fin)
        return fin_tour

    @classmethod
    def deserialized_turn(cls, serialized_turn):
        nom_tour = serialized_turn["nom_tour"]
        match_list = serialized_turn["match_list"]
        date_debut = serialized_turn["début"]
        date_fin = serialized_turn["fin"]
        deserialized_match_list = []
        for match in serialized_turn["match_list"]:
            deserialized_match = MatchController.deserialized_match(match)
            deserialized_match_list.append(deserialized_match)
        tour = Tours(nom_tours=nom_tour)
        tour.match_list = deserialized_match_list
        tour.date_debut = date_debut
        tour.date_fin = date_fin
        return tour


if __name__ == "__main__":
    tournois = TournamentController.build_tournois()
    round_list = TurnController.build_turns(tournois)


