class Joueur:

    def __init__(self, nom="Doe", prenom="John", date_de_naissance="JJ/MM/AAAA", sexe="n", classement=0, point=0):
        self.nom = nom
        self.prenom = prenom
        self.date = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        self.point = point

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.date}, {self.sexe}, {self.classement}, {self.point}"