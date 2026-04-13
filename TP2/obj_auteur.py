from obj_couleur import Couleur

class Auteur(Couleur):
    """Classe gérant les auteurs de la bibliothèque."""
    nombre_total_auteurs = 0
    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteurs += 1
        self.id = Auteur.nombre_total_auteurs
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        if pays is None:
            self.pays = "inconnu"
        else:
            self.pays = pays
        if date_naissance is None:
            self.date_naissance = "inconnue"
        else:
            self.date_naissance = date_naissance


    def __str__(self):
        # Retourne la f-string selon le format : ID. : Prenom NOM (né(e) le ... en ...)
        return f"{Auteur.MAGENTA}{self.id}. : {Auteur.NO_COLOR}{self.prenom} {self.nom}{Auteur.MAGENTA} (né(e) le {self.date_naissance} en {self.pays}){Auteur.NO_COLOR}"


print("Création de 3 instances de Auteur et affichage...")
follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
verne = Auteur("VERNE", "Jules", "France", "08/02/1828")
bridou = Auteur("BRIDOU", "Justin", None, None)
print(follett)
print(verne)
print(bridou)
print(bridou.pays)
print(bridou.date_naissance)