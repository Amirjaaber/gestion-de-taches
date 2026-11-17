taches = []


def ajouter_tache(titre):
    taches.append(titre)
    print("Tache ajoutee avec succes")

def rechercher_taches(mot_cle):
    print("--- Resultats de la recherche")
    trouve = False
    for i in range(len(taches)):
        if mot_cle.lower() in taches[i].lower():
            print(str(i + 1) + " - " + taches[i])
            trouve = True
    if trouve == False:
        print("Aucune tache ne contient ce mot.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tache pour le moment.")
    else:
        print("Liste des tâches")
        for i in range(len(taches)):
            print(str(i + 1) + " - " + taches[i])


while True:
    print()
    print("GESTION DES TACHES")
    print("1 ajouter une tache")
    print("2 afficher les tâches")
    print("3 rechercher une tâche")
    print("0 quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tache : ")
        if titre == "":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            ajouter_tache(titre)
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        mot = input("Mot cle a rechercher : ")
        rechercher_taches(mot)
    elif choix == "0":
        print("Au revoir")
        break
    else:
        print("Option invalide, veuillez resessayer.")
