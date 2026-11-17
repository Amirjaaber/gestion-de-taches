# Projet : Application de gestion des taches
# Module : Outils collaboratifs avec Git / GitHub

# Liste qui contient les taches (chaque tache est un titre)
taches = []


def ajouter_tache(titre):
    """Ajoute une tache a la liste."""
    taches.append(titre)
    print("Tâche ajoutée avec succès.")


def afficher_taches():
    """Affiche toutes les taches avec leur numero."""
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        print("--- Liste des tâches ---")
        for i in range(len(taches)):
            print(str(i + 1) + " - " + taches[i])


# Programme principal
while True:
    print()
    print("=== GESTION DES TACHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("0. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tâche : ")
        if titre == "":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            ajouter_tache(titre)
    elif choix == "2":
        afficher_taches()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Option invalide, veuillez réessayer.")
