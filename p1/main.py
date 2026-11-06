def direBonjourOuBonsoir(nombreDeFois, prenom):
    choix = input("Tapez 1 pour dire Bonjour et 2 pour dire Bonsoir")
    if choix == str(1):
        i = 1
        while i < nombreDeFois:
            print(f"Bonjour {prenom} | {prenom}")
            i = i + 1
    elif choix == str(2):
        for i in range(1, nombreDeFois):
            print(f"Bonsoir {prenom}")
    else:
        print("Je n'ai pas compris votre choix")

direBonjourOuBonsoir(5, "Bob")