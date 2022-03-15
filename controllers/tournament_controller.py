from models.tournament_model import Tournois
from views.tournament_views import ViewTournament
from views.player_views import ViewJoueur
from controllers.player_controller import PlayerController
from controllers.turn_controller import TurnController
from tinydb import TinyDB


class TournamentController:
    @classmethod
    def build_tournois(cls):
        data = ViewTournament.get_data_tournois()
        tournois = Tournois(data[0], data[1], data[2], data[3], data[4])
        return tournois

    @classmethod
    def build_participant_list(cls, tournois):
        participant = []

        while len(tournois.players_list) < tournois.nombre_de_joueur:
                new_player = ViewTournament.new_player()

                if new_player == "1":
                    joueur = PlayerController.build_joueur()
                    tournois.players_list.append(joueur)
                    participant.append(joueur)

                elif new_player == "2":
                    joueur = PlayerController.load_player()
                    tournois.players_list.append(joueur)
                    participant.append(joueur)

        participant = sorted(participant, key=lambda joueur: joueur.classement)
        return participant

    @classmethod
    def write_report(cls, tournois):
        commentaire = ViewTournament.get_raport_tournois()
        tournois.report.append(commentaire)

    @classmethod
    def trie_score(cls, participant):
        participant = sorted(participant, key=lambda joueur: joueur.point, reverse=True)
        return participant

    @classmethod
    def build_turn(cls, tournois):
        round_list = TurnController.build_turns(tournois)
        return round_list

    @classmethod
    def save_tournament(cls, serialized_tournament):
        db = TinyDB("D:\\Formation python\\chess_tournamentv2\\db.json")
        tournament_table = db.table("tournois")
        tournament_table.insert(serialized_tournament)
        return tournament_table

    @classmethod
    def load_tournament(cls):
        db = TinyDB("D:\\Formation python\\chess_tournamentv2\\db.json")
        table_tournois = db.table("tournois")
        serializied_tournaments = table_tournois.all()

        nom_tournois = ViewTournament.get_tournament_name()
        # nom_tournois = "test_unfinished"
        loaded_tournament = []
        while loaded_tournament == []:
            for index in range(0, len(serializied_tournaments)):
                if serializied_tournaments[index]["nom"] == nom_tournois:
                    loaded_tournament = serializied_tournaments[index]

        return loaded_tournament

    @classmethod
    def deserialized_tournois(cls, serialized_tournament):
        nom = serialized_tournament["nom"]
        lieu = serialized_tournament["lieu"]
        date = serialized_tournament["date"]
        nombre_de_joueur = serialized_tournament["nombre de joueur"]
        nombre_de_tour = serialized_tournament["nombre de tour"]
        rapport = serialized_tournament["Raport"]
        player_list = []
        for joueur in serialized_tournament["player_list"]:
            deserialized_joueur = PlayerController.deserialized_joueur(joueur)
            player_list.append(deserialized_joueur)
        deserialized_tours_list = []
        for tour in serialized_tournament["tours"]:
            deserialized_tour = TurnController.deserialized_turn(tour)
            deserialized_tours_list.append(deserialized_tour)
        tournois = Tournois(nom=nom, lieu=lieu, date=date, nombre_de_joueur=nombre_de_joueur,
                            nombre_de_tour=nombre_de_tour)

        tournois.report = rapport
        tournois.turns = deserialized_tours_list
        tournois.players_list = player_list
        return tournois

    @classmethod
    def display_tournaments(cls):
        db = TinyDB("D:\\Formation python\\chess_tournamentv2\\db.json")
        table_tournois = db.table("tournois")
        serializied_tournaments = table_tournois.all()

        for tournois in serializied_tournaments:
            print(f'Nom: {tournois["nom"]}, Lieu: {tournois["lieu"]}, Date: {tournois["date"]}, '
                  f'Nombre de joueurs: {tournois["nombre de joueur"]}')

    @classmethod
    def displayer_tournament_player(cls):
        loaded_tournament = TournamentController.load_tournament()
        trie = ViewJoueur.alphabetical_numeral()
        if trie == 1:
            player_list = loaded_tournament["player_list"]
            players_list = sorted(player_list, key=lambda player: player["name"], reverse=False)

            for player in players_list:
                print(f'Nom : {player["name"]}, Prenom: {player["prenom"]}, Classement: {player["classement"]}')

        elif trie == 2:
            player_list = loaded_tournament["player_list"]
            players_list = sorted(player_list, key=lambda player: player["classement"], reverse=False)

            for player in players_list:
                print(f'Nom : {player["name"]}, Prenom: {player["prenom"]}, Classement: {player["classement"]}')

    @classmethod
    def display_matchs(cls):
        loaded_tournament = TournamentController.load_tournament()
        tours = loaded_tournament["tours"]

        for round in tours:
            match = round["match_list"]
            print(f'{round["nom_tour"]}:')
            for resultat in match:
                resultat = resultat["resultat"]
                print(resultat)
