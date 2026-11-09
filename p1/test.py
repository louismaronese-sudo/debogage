mot_de_passe = input("C'est quoi le mot de passe ?")
if mot_de_passe != "1234":
    raise TypeError("Le mot de passe est une suite de chiffres normalement. Intrus !")
else:
    print("Bienvenue au club !")