class Voitures():
    prix_litre = 1.70
    # Constructeur avec 3 arguments...
    def __init__(self, marque, modele, annee, prix = None, couleur = "Blanc", conso = 6.0) :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso
    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture : {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso} l/100km - {self.prix}"
    def calcul_consommation(self, distance) :
        # Calcule la quantité de carburant nécessaire pour une distance donnée.
        litres_utilises = (distance * self.conso) / 100
        return litres_utilises
    def calcul_prix(self, distance) :
        #Calcule le coût total du carburant pour une distance donnée.
        litres_necessaires = self.calcul_consommation(distance)
        prix_total = litres_necessaires * Voitures.prix_litre
        return prix_total
    def modif_prix_litre(self, nouveau_prix) :
        # Modifie la valeur de l'attribut de classe prix_litre.
         Voitures.prix_litre = nouveau_prix