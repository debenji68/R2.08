from obj_couleur import Couleur
from obj_auteur import Auteur

class Livre(Couleur):
    nombre_total_livres = 0
    def __init__(self, titre, auteur, isbn=None, annee_publication=None):
        Livre.nombre_total_livres += 1
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur
        self.isbn = "Inconnu" if isbn is None else isbn
        self.annee_publication = "Inconnu" if annee_publication is None else annee_publication
        self.disponible = True


    def __str__(self):
        etat = f"{Livre.VERT}Dispo" if self.disponible else f"{Livre.ROUGE}NON Dispo"
        return (f"{Livre.MAGENTA}{self.id}. : {Auteur.NO_COLOR}'{self.titre}' de {self.auteur.prenom} {self.auteur.nom} "
                f"{Livre.MAGENTA}(ISBN: {self.isbn}, publié en {self.annee_publication}){Livre.NO_COLOR} - {etat}")



if __name__ == "__main__":
    # On doit d'abord créer les auteurs pour les lier aux livres
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")

    print("Création de 3 instances de Livre et affichage...")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
    livre_2.disponible = False
    livre_3 = Livre("Vingt Mille Lieues sous les mers", verne, "9782070364234", "1870")
    print(livre_1)
    print(livre_2)
    print(livre_3)