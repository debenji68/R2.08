from obj_voitures import Voitures

car = Voitures("Renault", "Clio", 2018, "2000 €")
print(car)
v1 = Voitures("Renault", "Captur_TCE_90ch", 2017, "20 000 €", "Gris foncé", 7.2)
print(v1)
v2 = Voitures("Renault", "Clio_TCE_100ch", 2017, "17 000 €", "Bleu nuit", 5.5)
print(v2)

distance_trajet = 1060
conso_clio = v2.calcul_consommation(distance_trajet)
print(f"Pour la {v2.marque} {v2.modele} :")
print(f"Le trajet de {distance_trajet} km nécessitera {conso_clio:.2f} litres de carburant.")

conso_captur = v1.calcul_consommation(distance_trajet)
print(f"Pour la {v1.marque} {v1.modele} :")
print(f"Le trajet de {distance_trajet} km nécessitera {conso_captur:.2f} litres de carburant.")



prix_clio = v2.calcul_prix(distance_trajet)
print(f"Le coût en carburant pour la Clio est de : {prix_clio:.2f} €")


prix_captur = v1.calcul_prix(distance_trajet)
print(f"Le coût en carburant pour le Captur est de : {prix_captur:.2f} €")


print(f"Prix du litre pour la Clio : {v2.prix_litre} €")
print(f"Prix du litre pour le Captur : {v1.prix_litre} €")

v2.modif_prix_litre(1.95)

print(f"Après modification (Clio) : {v2.prix_litre} €")
print(f"Après modification (Captur) : {v1.prix_litre} €")


co2_clio = v2.calcul_co2(distance_trajet)
print(f"Émission CO2 pour la Clio : {co2_clio:.2f} kg")

co2_captur = v1.calcul_co2(distance_trajet)
print(f"Émission CO2 pour le Captur : {co2_captur:.2f} kg")

v2 = Voitures("Renault", "Clio_TCE_100ch", 2017, "17 000 €", "Bleu nuit", 5.5)
print(v2)

print("Appel de la méthode d'affichage des données protégées :")
v2.affiche_prot_priv()
