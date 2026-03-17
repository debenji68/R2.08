import base64

class Voitures():
    prix_litre = 1.70
    # Constructeur avec 3 arguments...
    def __init__(self, marque, modele, annee, prix = None, couleur = "Blanc", conso = 6.0, id_serie="A123 B456 C789", audio_code="0000") :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso
        self._id_serie = id_serie
        self.__audio_code = base64.b64encode(audio_code.encode()).decode()


    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture : {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso} l/100km - {self.prix} - {self._id_serie} - {self.get_audio_code()}"


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


    def calcul_co2(self, distance):
        # Calcule la quantité de CO2 dégagée pour une distance donnée.
        litres = self.calcul_consommation(distance)
        kg_co2 = litres * 2.3
        return kg_co2


    def affiche_prot_priv(self):
        # Affiche les attributs protégés et pseudo-privés de l'instance.
        print(f"ID Série (protégé) : {self._id_serie}")
        code_chiffre = self.__audio_code
        code_clair = self.get_audio_code()
        print(f"Code Audio chiffré : {code_chiffre}")
        print(f"Code Audio décodé  : {code_clair}")


    def get_id_serie(self):
        # Retourne le numéro de série.
        return self._id_serie


    def set_id_serie(self, num_serie):
        # Modifie le numéro de série.
        self._id_serie = num_serie


    def get_audio_code(self):
        #Déchiffre et retourne le code audio en clair.
        return base64.b64decode(self.__audio_code).decode()


    def set_audio_code(self, code):
        # Chiffre et stocke le nouveau code audio.
        self.__audio_code = base64.b64encode(code.encode()).decode()