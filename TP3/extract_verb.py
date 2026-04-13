import re

def extraire_verbes(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8', errors='replace') as f:
            contenu = f.read()

        motif = r"^(\w+)\s+.*$"
        remplacement = r"\1, "

        resultat = re.sub(motif, remplacement, contenu, flags=re.MULTILINE)

        print(resultat)

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    extraire_verbes("verb.txt")