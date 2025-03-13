inventaire={}
while True:
    print ("Que souhaitez-vous faire ?\n1 - Ajouter un article\n2 - Supprimer un article\n3 - Afficher l'inventaire\n4 - Chercher un article\n5 - Quitter\n")
    choix=int(input("Entrez votre choix (1/2/3/4/5): "))
    if choix == 1:
        nom = input("Nom de l'article : ")
        quantite = int(input(f"Quantité de {nom} : "))
        # Ajouter ou mettre à jour l'article dans l'inventaire
        inventaire[nom] = quantite
        print(f"L'article '{nom}' a été ajouté avec une quantité de {quantite}.")
    
    elif choix == 2:
        nom = input("Nom de l'article à supprimer : ")
        # Vérifier si l'article existe dans l'inventaire
        if nom in inventaire:
            del inventaire[nom]
            print(f"L'article '{nom}' a été supprimé.")
        else:
            print(f"L'article '{nom}' n'existe pas dans l'inventaire.")
    
    elif choix == 3:
        # Afficher l'inventaire
        if not inventaire:
            print("L'inventaire est vide.")
        else:
            print("Inventaire actuel :")
            for nom, quantite in inventaire.items():
                print(f"- {nom} : {quantite}")
    
    elif choix == 4:
        nom = input("Nom de l'article à chercher : ")
        # Vérifier si l'article existe dans l'inventaire
        if nom in inventaire:
            print(f"L'article '{nom}' a une quantité de {inventaire[nom]}.")
        else:
            print(f"L'article '{nom}' n'existe pas dans l'inventaire.")
    
    elif choix == 5:
        print("Merci d'avoir utilisé le programme. À bientôt !")
        break

    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
