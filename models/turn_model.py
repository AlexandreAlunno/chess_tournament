class Tours:
    def __init__(self, nom_tours):
        self.nom_tours = nom_tours
        self.match_list = []

    def __str__(self):
        return f"{self.nom_tours}, {self.match_list}"