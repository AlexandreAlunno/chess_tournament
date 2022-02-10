class Tours:
    def __init__(self, nom_tours):
        self.nom_tours = nom_tours
        self.match_list = []

    def serializer_tour(self):
        serialized_turn = {
            "nom_tour": self.nom_tours,
            "match_list": []
        }
        return serialized_turn

    def __str__(self):
        return f"{self.nom_tours}, {self.match_list}"