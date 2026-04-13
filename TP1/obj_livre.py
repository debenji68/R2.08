from obj_couleur import Couleur
from obj_auteur import Auteur

class Livre(Couleur):
    """Classe représentant un livre de la bibliothèque."""
    nombre_total_livres = 0
    def __init__(self, titre, auteur, isbn=None, annee_publication=None):
        """
        Initialise une instance de Livre.
        L'attribut 'disponible' est initialisé par défaut à True.
        """
        Livre.nombre_total_livres += 1
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur
        self.isbn = "Inconnu" if isbn is None else isbn
        self.annee_publication = "Inconnu" if annee_publication is None else annee_publication
        self.disponible = True

    def __str__(self):
        """
        Méthode optionnelle (pour test) afin de visualiser le livre et son auteur.
        Utilise l'affichage de l'objet Auteur grâce à la méthode __str__ de ce dernier.
        """
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"Livre n°{self.id} : '{self.titre}' par {self.auteur.prenom} {self.auteur.nom} ({statut})"


follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
verne = Auteur("VERNE","Jules","France", "08/02/1828")
print("Création de 3 instances de Livre et affichage...")
livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
livre_2.disponible = False
livre_3 = Livre("Vingt Mille Lieues sous les mers", verne, "9782070364234", "1870")
print(livre_1)
print(livre_2)
print(livre_3)