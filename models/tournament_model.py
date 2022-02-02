class Tournois:

    def __init__(self, nom, lieu, date, nombre_de_joueur, nombre_de_tour=4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_joueur = nombre_de_joueur
        self.nombre_de_tour = nombre_de_tour

    def __str__(self):
        return f"{self.nom, self.lieu, self.date, self.nombre_de_joueur, self.nombre_de_tour}"
