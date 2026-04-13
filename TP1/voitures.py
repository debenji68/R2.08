class Voitures():
    # Constructeur avec 3 arguments...
    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010):
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"




car = Voitures("Renault", "Clio", 2018) # Création d’une instance.
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !") # Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")
print(car)

car_2 = Voitures("Ford", "Mustang", 2017)
print(car_2)
v3 = Voitures("Bugatti", "Veyron")
print(v3)
v4 = Voitures()
print(v4)
v5 = Voitures("F40")
print(v5)
v6 = Voitures(modele="296 GTS")
print(v6)

print(type(v6))
print(vars(v6))
print(dir(v6))